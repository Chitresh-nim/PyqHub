from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Subject, PYQ, Bookmark

class BaseTest(TestCase):
    def setUp(self):
        self.user= User.objects.create_user(
            username="chitresh",
            email="test@gmail.com",
            password="password123"
        )

        self.subject = Subject.objects.create(
            title="DEEP LEARNING",
            code="BAI701",
            branch="CSE",
            semester=7
        )

        self.paper = PYQ.objects.create(
            subject= self.subject,
            year="2024-25",
            drive_link="https://drive.google.com/file/u/0/d/1SjIALhGozvFaTnBGMkFzTi8uji-rGgJ_/view?usp=drivesdk"
        )
class LoginPageTest(BaseTest):
    def test_login_page_loads(self):
        response = self.client.get(reverse("login"))

        self.assertEqual(response.status_code, 200)

class RegisterPageTest(BaseTest):
    def test_register_page_loads(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

class RegisterUserTest(BaseTest):
    def test_register_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username" : "newuser",
                "email": "new@gmail.com",
                "password1": "password123@",
                "password2": "password123@"
            }
        )
        self.assertTrue(
            User.objects.filter(username="newuser").exists()
        )

class LoginTest(BaseTest):
    def test_login(self):
        response= self.client.post(
            reverse("login"),
            {
                "email": "test@gmail.com",
                "password": "password123"
            }
            
        )
        self.assertRedirects(response,reverse("home"))

class LogoutTest(BaseTest):
    def test_logout(self):
        self.client.login(
            username="chitresh",
            password="password123"
        )
        response = self.client.get(reverse("logout"))

        self.assertEqual(response.status_code,302)

class DashhboardTest(BaseTest):
    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code,302)

class SearchApiTest(BaseTest):
    def test_search(self):
        response = self.client.get(reverse("search_subjects"),
                                   {
                                      "q": "Deep" 
                                   })
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()),0)

class FilterPaper(BaseTest):
    def test_filter (self):
        self.client.login(
            username="chitresh",
            password="password123"
        )
        response=self.client.get(
            reverse("filter_paper"),
            {
                "branch":"CSE"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("papers", response.json())

class BookmarkTest(BaseTest):
    def test_bookmark(self):
        self.client.login(
            username="chitresh",
            password="password123"
        )
        response=self.client.post(
            reverse("toggle_bookmark",
                    args=[self.paper.id])
        )
        self.assertEqual(response.status_code,200)
        self.assertTrue(Bookmark.objects.filter(
            user=self.user,
            paper=self.paper
        ).exists()
        )

class EditProfileTest(BaseTest):
    def test_change_username(self):
        self.client.login(
            username="chitresh",
            password="password123"
        )

        self.client.post(
            reverse("edit_profile"),
            {
                "username": "newname"
            }
        )

        self.user.refresh_from_db()
        self.assertEqual(
            self.user.username,
            "newname"
        )

class PermissionTest(BaseTest):
    def api_require_login(self):
        response = self.client.get(
            reverse("filter_paper")
        )
        self.assertIn(response.status_code,[401,403])

