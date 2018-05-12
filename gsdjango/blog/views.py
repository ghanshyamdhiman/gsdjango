from django.views.generic import TemplateView

from . models import Blog

class HomePageView(TemplateView):
  model = Blog
  template_name = 'home.html'
  
  

# Create your views here.
