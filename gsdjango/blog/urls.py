from django.urls import path

from . import views

urlpatterns = [ 
  path('', HomeBlogView.as_view(), name='home'),
]
