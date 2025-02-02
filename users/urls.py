from django.urls import path

from users.apps import UsersConfig
from users.views import user_register_view, user_login_view, user_logout_view, user_profile_view, user_update_view

app_name = UsersConfig.name
urlpatterns = [
    path('', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('register/', user_register_view, name='register'),
    path('profile/', user_profile_view, name='profile'),
    path('update/', user_update_view, name='update_user'),
]
