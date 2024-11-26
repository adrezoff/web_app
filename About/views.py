from .models import About
from django.views.generic import ListView


class AboutPageView(ListView):
    model = About
    template_name = "about-us.html"
    context_object_name = 'about_us'

