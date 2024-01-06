from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from apps.base.models import Settings
from apps.base.serializers import SettingsSerializer

class SettingsCreateAPIView(CreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class SettingsListAPIView(ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class SettingsUpdateAPIView(UpdateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer

class SettingsDestroyAPIView(DestroyAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
