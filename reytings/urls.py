

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('post-detail/<int:company_id>/', views.post_detail, name='post_detail'),
  path('company-save', views.company_save,name='company_save'),
  path('comment-save', views.comment_save,name='comment_save'), 
  path('search/', views.search,name='search'), 
  path('sort/', views.sort,name='sort'), 

]
