from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ActivateEmailForm
from .models import Registration
# Create your views here.

def activate(request):
	if request.method == 'POST':
		form = ActivateEmailForm(request.POST)
		if form.is_valid():
			registration = Registration(email=form.cleaned_data['email'], active=True)
			if registration.activate_if_exists():
				messages.info(request, "We have reactivated your account, thanks!")
				#print "HELLO"
				# no further action, reactivated
			else:
				messages.info(request, "You are successfully registered!")
				registration.save()

			# set session so the box is not displayed next time
			request.session['registered_email'] = True
			return HttpResponseRedirect(request.POST.get('next'))
	
	return HttpResponseRedirect('/blog/')


def cancel(request):
	# get the email hash
	email_hash = request.GET.get('h')
	# TODO add a response message
	if email_hash is None:
		return HttpResponseRedirect('/mailing/')		

	try:
		res = Registration.objects.get(email_hash=email_hash)
	except Registration.DoesNotExist:
		# TODO add error message
		messages.error(request, 'Email address does not exist')
		return HttpResponseRedirect('/blog/') 
	except:
		return HttpResponseRedirect('/blog/') 

	res.disable()
	messages.info(request, "You unsubscribed from our mailinglist with email address: %s " % (res.email))
	return HttpResponseRedirect('/blog/')