from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns += doc
