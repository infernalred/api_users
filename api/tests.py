from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from api.models import User
from api.serializer import ReadOnlyUserSerializerSerializer


class UsersTest(APITestCase):
    """Test module for test users"""

    def setUp(self):
        self.user = User.objects.create(
            username='admin', password='Qwerty123!', is_active=True, is_superuser=True)
        self.user1 = User.objects.create(
            username='user1', password='Qwerty123!', is_active=True)
        User.objects.create(
            username='user2', password='Qwerty123!', is_active=True)
        Token.objects.create(user=self.user)
        token = Token.objects.get(user__username='admin')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_non_auth_user(self):
        client = APIClient()
        resp = client.get('/api/v1/users/')
        self.assertEqual(resp.status_code, 401)

    def test_get_all_users(self):
        resp = self.client.get('/api/v1/users/')
        users = User.objects.all()
        serializer = ReadOnlyUserSerializerSerializer(users, many=True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, serializer.data)

    def test_get_one_user(self):
        resp = self.client.get(f'/api/v1/users/{self.user1.pk}/')
        user = User.objects.get(pk=self.user1.pk)
        serializer = ReadOnlyUserSerializerSerializer(user)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, serializer.data)

    def test_create_one_user(self):
        data = {'username': 'user3', 'password': 'Qwerty123!', 'is_active': True}
        resp = self.client.post('/api/v1/users/', data, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(User.objects.count(), 4)
