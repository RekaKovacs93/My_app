import unittest
from models.user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user = User("Reka", 1, 0, 0)
    
    
    def test_user_has_name(self):
        self.assertEqual("computer", self.user.name)