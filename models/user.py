from  tests.test_user import * 
class User(object):
	users = []
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.comments = []

	def create_user(self, username,password):
		self.users.append(User(username,password))

	def json(self):
		return {'username':self.username,
    			'password':self.password,
    			'comments':self.comments}