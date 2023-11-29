from django.urls import path, re_path
from mysite.views import home, error, user

urlpatterns = [
    path('', home, name='home'),
    path('error/', error, name='error'),
    re_path(r'user/(?P<login>\w+)/(?P<folder>\w+)/(?P<post_num>\d+)/$', user, name='user'),
]
