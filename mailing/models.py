from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from datetime import datetime

import hashlib

# Create your models here.

class Registration(models.Model):
	email = models.EmailField(max_length=500, unique=True)
	email_hash = models.CharField(max_length=500, unique=False, blank=True, null=True, editable=False)
	registration_date = models.DateTimeField('Registration date', auto_now_add=True, blank=False)
	cancellation_date = models.DateTimeField('Cancellation date', default=None, blank=True, null=True)
	activation_date = models.DateTimeField('Activation date', default=None, blank=True, null=True)
	active = models.BooleanField(default=True, blank=False)
	user = models.ForeignKey(User, default=None, null=True, blank=True)

	def __str__(self):
		activestr = "Active"
		if not self.active : activestr = "Disabled"
		return self.email + " (" + activestr + ")"

	def save(self, *args, **kwargs):
		self.email_hash = hashlib.sha1(self.email).hexdigest()
		super(Registration, self).save(*args, **kwargs)

	def activate_if_exists(self):
		reg = Registration.objects.get(email=self.email)
		if reg is not None:
			# object already exists, need to set activation to True and resave
			reg.active = True
			reg.activation_date = datetime.now()
			reg.save()
			return True

		return False


	def disable(self):
		self.active = False
		self.cancellation_date = datetime.now()
		self.save()
		return True