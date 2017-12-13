from django.contrib import admin
from .models import WebSite
# Register your models here.

@admin.register(WebSite)
class WebSiteAdmin(admin.ModelAdmin):
	pass