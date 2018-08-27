"""
This module collects the tests for the normal user
"""
# standard imports
import unittest
from datetime import datetime
from models.user import User

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


    def test_user_can_create_comment(self):
        """Test that a user can comment"""
        params = {
            'username':'testuser',
            'password':'password'
        }

        
        new_user = User(**params)
        comments = "comments"
        self.assertEqual(new_user.create_comment(comments)['comment'], comments)
        
        self.assertEqual(1, len(new_user.comments))

    
    def test_user_logout(self):
        """test that a logged in user can logout"""
        params = {
            'username':'userlogout',
            'password':'password'
        }
        new_user = User(**params)
        new_user.login()
        self.assertTrue(new_user.lastLoggedInAt <= datetime.now())
        self.assertEqual(new_user.logout(), 'Logged out')
        self.assertFalse(new_user.online)
        

    def test_user_log_in(self):
        """
        Test that a user can log in
        """   
        user_one = {
            "username":"salimia",
            "password":"salam123"
        }
        user = User(**user_one)
        user.login()
        self.assertTrue(user.lastLoggedInAt <= datetime.now())
    
    def test_edit_comment(self):
        params = {
            'username':'testuser',
            'password':'password'
        }

        new_user = User(**params)
        comments = "comments"
        self.assertEqual(new_user.edit_comment(comments)['comment'], comments)
        
        


