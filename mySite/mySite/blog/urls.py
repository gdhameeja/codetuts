from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    #url(r'^search_results/$', search, name="search")
]