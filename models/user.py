from datetime import datetime
from tests.test_user import *


class User(object):
    users = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.comments = []
        self.role = 'user'
        self.online = False
        self.lastLoggedInAt = None

    def create_user(self, username, password):
        self.users.append(User(username, password))

    def json(self):
        resp = {
            'username': self.username,
            'password': self.password,
            'comments': self.comments
            }
        return resp

    def create_comment(self, comment):
        new_comment = {
            'id': len(self.comments) + 1,
            'author': self.username,
            'comment': comment,
            'time_created': datetime.now()
        }
        self.comments.append(new_comment)
        return new_comment

    def logout(self):
        """logout a logged in user"""
        self.online = False
        return "Logged out"

    def login(self):
        """
        User log in
        """
        self.lastLoggedInAt = datetime.now()
        self.online = True
        return "User has logged in successfully"

        
        

