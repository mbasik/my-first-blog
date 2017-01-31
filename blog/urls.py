from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.category_list, name='category_list'),
    url(r'^post', views.post_list, name='post_list'),
    url(r'^place', views.place_list, name='place_list'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^place/new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^(?P<pk>\d+)/edit_place/$', views.place_edit, name='place_edit'),
]