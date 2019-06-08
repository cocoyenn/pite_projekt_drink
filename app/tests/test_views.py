from django.test import TestCase

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


class ViewsTest(TestCase):

    def test_home(self):
        url = reverse("app-home")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_about(self):
        url = reverse("app-about")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)


    def test_user_register(self):
        url = reverse("app-register")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)


    def test_user_login(self):
        url = reverse("app-login")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)


    def test_makeDrink(self):
        url = reverse("app-makeDrink")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)


    def test_user_logout(self):
        url = reverse("app-logout")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
