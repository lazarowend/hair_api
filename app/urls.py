from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('barbershops.urls')),
    path('api/v1/', include('users.urls')),
]
