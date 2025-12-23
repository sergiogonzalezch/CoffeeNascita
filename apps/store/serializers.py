from rest_framework.serializers import ModelSerializer
from .models import MenuItem

class MenuitemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'