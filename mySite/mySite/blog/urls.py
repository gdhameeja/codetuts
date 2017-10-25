from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name= "index.html"), name="index"),
    url(r'^search/', views.search, name= "search"),
    url(r'^content/django/(?P<slug>[-\w]+)$', views.django_handler, name="content_urls")
]