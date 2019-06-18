from django.test import TestCase
from django.urls import reverse, resolve
from app.views import home, about, user_login, user_register, user_logout, make_drink

class TestUrlsFunc(TestCase):
 
    def test_home_url_is_resolved(self):
        url = reverse('app-home')
        self.assertEquals(resolve(url).func, home)

    def test_about_url_is_resolved(self):
        url = reverse('app-about')
        self.assertEquals(resolve(url).func, about)   

    def test_user_login_url_is_resolved(self):
        url = reverse('app-login')
        self.assertEquals(resolve(url).func, user_login)

    def test_user_register_url_is_resolved(self):
        url = reverse('app-register')
        self.assertEquals(resolve(url).func, user_register)

    def test_user_logout_url_is_resolved(self):
        url = reverse('app-logout')
        self.assertEquals(resolve(url).func, user_logout) 

    def test_make_drink_url_is_resolved(self):
        url = reverse('app-makeDrink')
        self.assertEquals(resolve(url).func, make_drink)

class TestUrlsRouts(TestCase):
 
    def test_home_url_is_resolved(self):
        url = reverse('app-home')
        self.assertEquals(resolve(url).route, "")
    
    def test_about_url_is_resolved(self):
        url = reverse('app-about')
        self.assertEquals(resolve(url).route, "about/")

    def test_user_login_url_is_resolved(self):
        url = reverse('app-login')
        self.assertEquals(resolve(url).route, "login/")

    def test_user_register_url_is_resolved(self):
        url = reverse('app-register')
        self.assertEquals(resolve(url).route, "register/")

    def test_user_logout_url_is_resolved(self):
        url = reverse('app-logout')
        self.assertEquals(resolve(url).route, "logout")

    def test_make_drink_url_is_resolved(self):
        url = reverse('app-makeDrink')
        self.assertEquals(resolve(url).route, "make_drink/")