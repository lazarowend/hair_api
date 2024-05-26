from django.urls import path
from . views import ListCreateUserView, RetriveUpdateDestroyUserView, LoginUserView, LogoutUserView


urlpatterns = [
    path('user/', ListCreateUserView.as_view(), name='list_create_user_view'),
    path('user/<int:pk>', RetriveUpdateDestroyUserView.as_view(), name='retrive_update_destroy_user_view'),
    path('user/login/', LoginUserView.as_view(), name='login_user_view'),
    path('user/logout/', LogoutUserView.as_view(), name='logout_user_view'),
]
