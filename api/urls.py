from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()

urlpatterns = [
    path('v1/', include(router.urls)),
]

urlpatterns += [
        path('v1/api-token-auth/', views.obtain_auth_token),
    ]