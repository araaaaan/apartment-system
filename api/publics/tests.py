import json
from rest_framework.test import APITestCase
from rest_framework      import status

from api.publics.models  import User_APT

class PublicTest(APITestCase):
    def setUp(self):
        User_APT.objects.create(
            floor    = "1004",
            password = "0101",
            cost     = "10000.00"
        )
    def test_public_authenticated(self):
        data     = {"floor":"1004", "password":"0101"}
        response = self.client.post('/api/publics', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            "floor":"1004",
            "cost":"10000.00"
          }) 
    def test_admin_authenticated_error(self):
        data     = {"floor":"1004", "password":"0000"}
        response = self.client.post('/api/publics',  data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)