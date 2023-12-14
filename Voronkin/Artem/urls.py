from django.urls import path, re_path
from .views import index, user, error

urlpatterns = [
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', index),
    path('user/<str:name>', index, name='home'),
    path('user', index, name='home'),
    path('username/<str:login>/<str:name_post>/<int:id_post>', user),
    path('username/<str:login>/<str:name_post>', user),
    path('username/<str:login>', user),
    path('username', user),
    path('error', error)
]
