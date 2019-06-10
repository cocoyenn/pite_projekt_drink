from django.test import TestCase
from django.test import Client
from app.forms import UserForm, UserProfileInfoForm

# class Setup_Class(TestCase):

#     def setUp(self):
#         self.user = User.objects.create(email="user@mp.com", password="user", first_name="user", phone=12345678)

class UserForm_Test(TestCase):
    def test_UserForm_valid(self):
        form = UserForm(data={'username':"user",'first_name': "user",'last_name': "user", 'password': "user",'email': "user@mp.com"})
        self.assertTrue(form.is_valid())

    def test_UserForm_valid_without_first_name(self):
        form = UserForm(data={'username':"user",'last_name': "user", 'password': "user",'email': "user@mp.com"})
        self.assertTrue(form.is_valid())

    def test_UserForm_valid_without_last_name(self):
        form = UserForm(data={'username':"user",'first_name': "user", 'password': "user",'email': "user@mp.com"})
        self.assertTrue(form.is_valid())

    def test_UserForm_valid_without_email(self):
        form = UserForm(data={'username':"user",'first_name': "user",'last_name': "user", 'password': "user"})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid_without_username(self):
        form = UserForm(data={'first_name': "user",'last_name': "user", 'password': "user",'email': "user@mp.com"})
        self.assertFalse(form.is_valid())

    def test_UserForm_invalid_without_password(self):
        form = UserForm(data={'username':"user",'first_name': "user",'last_name': "user", 'email': "user@mp.com"})
        self.assertFalse(form.is_valid())

class UserProfileInfoForm_Test(TestCase):
    def test_UserProfileInfoForm_valid_empty(self):
        form = UserProfileInfoForm(data={})
        self.assertTrue(form.is_valid())

    def test_UserProfileInfoForm_valid(self):
        form = UserProfileInfoForm(data={"portfolio_site":"", "profile_pic":""})
        self.assertTrue(form.is_valid())