from django.test import TestCase

from app.models import UserProfileInfo
from django.contrib.auth.models import User


class UserProfileInfo_Test(TestCase):

    def create_UserProfileInfo(self, username):
        user = User.objects.create(username=username)
        return UserProfileInfo.objects.create(user=user)

    def test_UserProfileInfo_str(self):
        upi = self.create_UserProfileInfo("Jan")
        self.assertEqual(upi.__str__(), "Jan")

