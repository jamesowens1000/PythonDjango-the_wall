from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^wall$', views.wall),
    url(r'edit_page$', views.edit_page),
    url(r'users/update$', views.update),
    url(r'logout$', views.logout),
    url(r'post_message$', views.post_message),
    url(r'post_comment/(?P<msg_id>\d+)$', views.post_comment),
    url(r'delete/(?P<msg_id>\d+)$', views.delete_msg),
    url(r'like_msg/(?P<msg_id>\d+)$', views.like_message),
    url(r'like_cmnt/(?P<cmnt_id>\d+)$', views.like_comment),
    url(r'user_posts/(?P<user_id>\d+)$', views.user_posts),
]