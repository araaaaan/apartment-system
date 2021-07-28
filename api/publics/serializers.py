from rest_framework import serializers

from api.publics.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('floor','password',)