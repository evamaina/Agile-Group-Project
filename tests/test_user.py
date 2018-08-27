"""
This module collects the tests for the normal user
"""
# standard imports
import
import unittest
from ..user import User

class TestUser(unittest.TestCase):
    """This class collects the test for the regular user"""

    def test_user_can_be_created(self):
        """Test that a user can be created"""
        params = {
            'username':'testuser',
            'password':'password'
        }
        new_user = User(**params)
        self.assertEqual(new_user.username, params['username'])
        self.assertEqual(new_user.password, params['password'])
        # check that the new user does not have any comments
        self.assertEqual(0, len(new_user.comments))

    def test_user_log_in(self):
        """
        Test that a user can log
        """   
        user_one = {
            "username":"salimia",
            "password":"salam123"
        }
        user = User(**user_one)
        user.login()
        self.assertTrue(user.lastLoggedInAt < datetime.now())



