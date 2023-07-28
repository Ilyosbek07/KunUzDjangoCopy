from django.contrib import admin

from apps.common.models import User, Contact, FAQ

admin.site.register(User)
admin.site.register(Contact)
admin.site.register(FAQ)
