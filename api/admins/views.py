from rest_framework                import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions    import IsAuthenticated
from rest_framework.viewsets       import ModelViewSet
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


from api.publics.models      import User_APT
from api.publics.serializers import UserSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset               = User_APT.objects.all()
    serializer_class       = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes     = [IsAuthenticated]
    
