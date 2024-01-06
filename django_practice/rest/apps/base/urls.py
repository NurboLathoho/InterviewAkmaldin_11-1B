from django.urls import path
from .views import SettingsCreateAPIView, SettingsListAPIView, SettingsUpdateAPIView, SettingsDestroyAPIView
urlpatterns = [
    path('', SettingsListAPIView.as_view(), name='settings'),
    path('create/', SettingsCreateAPIView.as_view(), name='settings_create'),
    path('update/<int:pk>/', SettingsUpdateAPIView.as_view(), name='settings_update'),
    path('destroy/<int:pk>/', SettingsDestroyAPIView.as_view(), name='settings_destroy'),
]