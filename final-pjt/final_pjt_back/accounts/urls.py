from django.urls import path
from .views import UserUpdateAPIView, get_current_user
from . import views
app_name = 'accounts'
urlpatterns = [
    path('update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('current-user/', views.get_current_user),
    path('delete/', views.delete_user)
]





