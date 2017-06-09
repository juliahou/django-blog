from django.conf.urls import url
from . import views

urlpatterns = [
	# ^ denotes the beginning of a URL, $ denotes the end, so ^$ denotes the empty string
	url(r'^$', views.post_list, name='post_list'),
]