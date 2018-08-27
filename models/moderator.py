from models.user import User

class Moderator(User):
	def __init__(self):
		self.role = "moderator"

	def edit_comment(self, comment_id):
		edit_comment = [comment for comments in self.comments if comments['comment_id'] == comment_id]
        edit_comment['comment'] = comment
        
