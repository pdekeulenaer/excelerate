from django.contrib import admin
from models import Registration



class RegistrationAdmin(admin.ModelAdmin):
	readonly_fields=('email_hash',)


# Register your models here.
admin.site.register(Registration, RegistrationAdmin)