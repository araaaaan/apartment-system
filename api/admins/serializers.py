from rest_framework import serializers

from api.publics.models import User

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('floor','cost',)