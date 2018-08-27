"""
This module collects the tests for the normal user
"""
# standard imports
import unittest
<<<<<<< HEAD
from ..user import User
from datetime import datetime
=======
from models.user import User
>>>>>>> 72910cc8abe4119e43d45c4683bff369c301fb19

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
<<<<<<< HEAD
    
    def test_user_logout(self):
        """test that a logged in user can logout"""
        params = {
            'username':'userlogout',
            'password':'password'
        }
        new_user = User(**params)
        self.assertTrue(new_user.lastLoggedInAt < datetime.now())
        self.assertEqual(new_user.logout(), 'logged out')
        self.assertFalse(new_user.online)
=======
        
>>>>>>> 72910cc8abe4119e43d45c4683bff369c301fb19
