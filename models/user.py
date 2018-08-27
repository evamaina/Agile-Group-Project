from  tests.test_user import * 
class User(object):
	users = []
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.comments = []
		self.online = False

	def create_user(self, username,password):
		self.users.append(User(username,password))

	def json(self):
		return {'username':self.username,
    			'password':self.password,
    			'comments':self.comments}

	def logout(self):
		"""logout a logged in user"""
		self.online = False
		return "Logged out"

		