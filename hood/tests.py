from django.test import TestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class NeighbourHoodTestClass(TestCase):
    """tests to test if NeighbourHood class is been instansiated correctly"""
    def setUp(self):

        self.new_user = User(username = "wati", email = "moringaprojects@gmail.com",password = "123456789")
        self.new_user.save()

class UserTestClass(TestCase):
    """tests to test if User class is been instansiated correctly"""
    def setUp(self):
        self.new_user = User(username = "wati", email = "moringaprojects@gmail.com",password = "123456789")
        self.new_user.save()

class NeighbourHoodTestClass(TestCase):
    """tests to test if Business class is been instansiated correctly"""
    def setUp(self):
        self.new_user = User(username = "wati", email = "moringaprojects@gmail.com",password = "123456789")
        self.new_user.save()
