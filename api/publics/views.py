from rest_framework.response  import Response
from rest_framework.views     import APIView
from rest_framework           import status, generics

from api.admins.serializers   import AccountSerializer
from api.publics.serializers  import UserSerializer
from .models                  import User

# class RoomAPIView(APIView):
#     def post(self, request):
#         try:
#             floor      = request.data['floor']
#             password   = request.data['password']
#             get_id     = User.objects.get(floor=floor, password=password)
#             serializer = AccountSerializer(get_id)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except:
#             return Response({"message":"CHECK_YOUR_NUMBER"},status=status.HTTP_400_BAD_REQUEST)
        
    

#from indent_corp.auth import HouseHoldAuthentication
#from indent_corp.models import HouseHold, DoorUseLog
#from indent_corp.serializers import HouseHoldSerializer

FEE_PER_COUNT = 1

# custom authentication_classes
from rest_framework.authentication import BaseAuthentication

class PublicUserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print("++")
        print(f"request : {dir(request)}")
        authentication = request.META.get('HTTP_AUTH', 'default')

        params = request.query_params.get('key')
        print(f"auth : {authentication}")
        print(f"params : {params}")

        return 

class PublicUserDetailView(generics.RetrieveAPIView):
    authentication_classes = [PublicUserAuthentication, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer        