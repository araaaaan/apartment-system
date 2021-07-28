# import json

# from django.contrib.auth.models import User

# from rest_framework                  import status
# from rest_framework.authtoken.models import Token
# from rest_framework.test             import APITestCase

# from api.publics.models import User
        
# class Admintest(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             username = "laran89",
#             password = "strong-password",
#             is_staff = True
#         )
#         self.token = Token.objects.create(user=self.user)
#         User.objects.create(
#             floor    = "1004",
#             password = "1234",
#             cost     = 10000.00
#             )
#         self.api_authentication()
    
#     def api_authentication(self):
#         self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token}")
        
#     def test_admin_authenticated(self):
#         response = self.client.get('/api/admin')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.json(), [{
#             "floor"   : "1004",
#             "password": "1234",
#             "cost"    : "10000.00"
#           }])
        
#     def test_admin_authenticated_error(self):
#         self.client.force_authenticate(user=None)
#         response = self.client.get('/api/admin')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)