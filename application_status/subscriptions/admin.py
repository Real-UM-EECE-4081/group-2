from django.contrib import admin
from .models import Application, Subscription, Category

# Register your models here.
admin.site.register(Application)
admin.site.register(Subscription)
admin.site.register(Category)