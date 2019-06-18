from django.contrib.auth.models import User
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

    def test_makeDrink_coconut(self):
        url = reverse("app-makeDrink")
        resp = self.client.post(url, data={"ingredient1": "coconut"})

        self.assertEqual(resp.status_code, 200)

    def test_user_register_get(self):
        url = reverse("app-register")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_user_register_post_valid(self):
        url = reverse("app-register")
        resp = self.client.post(url, data={"username": "Lukaszek", "password": "ala"})

        self.assertEqual(resp.status_code, 200)

    def test_user_register_post_invalid(self):
        url = reverse("app-register")
        resp = self.client.post(url, data={"password": "ala"})

        self.assertEqual(resp.status_code, 200)

    def test_user_login_get(self):
        url = reverse("app-login")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_user_login_post_invalid(self):
        url = reverse("app-login")
        resp = self.client.post(url, data={"username": "Ala", "password": "lol"})

        self.assertEqual(resp.status_code, 200)

    def test_user_login_post_valid(self):
        User.objects.create_user(username='Ala', password='lol')
        url = reverse("app-login")
        resp = self.client.post(url, data={"username": "Ala", "password": "lol"})

        self.assertEqual(resp.status_code, 302)

    def test_user_logout(self):
        User.objects.create_user(username='Ala', password='lol')
        self.client.login(username='Ala', password='lol')
        url = reverse("app-logout")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 302)

    def test_profile_site(self):
        url = reverse("app-profile")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_profile_edition_post_valid(self):
        User.objects.create_user(username='Ala', password='lol')
        self.client.login(username='Ala', password='lol')
        url = reverse("app-profile_edition")
        resp = self.client.post(url, data={"username": "Ala", "password": "lol"})

        self.assertEqual(resp.status_code, 302)

    def test_profile_edition_get(self):
        User.objects.create_user(username='Ala', password='lol')
        self.client.login(username='Ala', password='lol')
        url = reverse("app-profile_edition")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
