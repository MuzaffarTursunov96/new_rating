from django.contrib import admin

from .models import Comments,Company,User
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
  list_display=['id','name','address']

class UserAdmin(admin.ModelAdmin):
  list_display=['username']

class CommentAdmin(admin.ModelAdmin):
  list_display=['owner_name','email']

admin.site.register(Company,CompanyAdmin)
admin.site.register(Comments,CommentAdmin)
admin.site.register(User,UserAdmin)
