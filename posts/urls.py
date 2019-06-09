from django.conf.urls import url
from django.contrib import admin


from .views import(
	post_create,
	post_detail,
	post_list,
	post_update,
	post_delete,
	post_drafts,
	login_user,
	logout_user,
	register_user,
	my_posts,
	) 


urlpatterns = [
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<id>\d+)/$', post_detail, name='details'),
    url(r'^list/$', post_list, name='list'),
    url(r'^drafts/$', post_drafts, name='drafts'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
##############
	url(r'^login/$', login_user, name="login"),
	url(r'^logout/$', logout_user, name="logout"),
	url(r'^register/$', register_user, name="register"),
	url(r'^myposts/$', my_posts, name="myposts"),
 #############

    #url(r'^posts/$', "appname.views.function_name"),
    
]
