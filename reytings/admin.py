from django.contrib import admin

from .models import Comments,Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
  list_display=['id','name']

admin.site.register(Company,CompanyAdmin)
admin.site.register(Comments)
