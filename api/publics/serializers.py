from rest_framework import serializers

from api.publics.models import User_APT

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User_APT
        fields = ('floor','cost',)