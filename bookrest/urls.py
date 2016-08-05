from django.conf.urls import url, patterns
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns =[
	url(r'^books/$', views.book_list),
	url(r'^books/(?P<pk>[0-9]+)/$', views.book_detail),
]
