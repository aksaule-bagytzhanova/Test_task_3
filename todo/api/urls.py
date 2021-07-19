from django.urls import path, include
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

    path('todo/', views.TaskList.as_view()),
    path('todo/<int:pk>/', views.TaskDetail.as_view()),
    path('todo/<int:task_id>/execute', views.TaskExecute.as_view()),



]