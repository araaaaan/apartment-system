from rest_framework.response  import Response
from rest_framework.views     import APIView
from rest_framework           import status

from api.admins.serializers   import AccountSerializer
from .models                  import User_APT

class RoomAPIView(APIView):
    def post(self, request):
        try:
            floor      = request.data['floor']
            password   = request.data['password']
            get_id     = User_APT.objects.get(floor=floor, password=password)
            serializer = AccountSerializer(get_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message":"CHECK_YOUR_NUMBER"},status=status.HTTP_400_BAD_REQUEST)
