from models.user import User

class Admin(User):
    """
    This will hold admin related information
    """
    def __init__(self, username, password, role):
        User.__init__(self, username, password)
        self.role = role

    def edit_comments(self, comment_id, role):
        """Admin edit a comment"""
        edit_comment = {}
        if role == 'admin':

            for comment in comments:
                if comment["id"] = comment_id:
                    edit_comment = comment
        else:
            return "You must be an admin to edit a comment"

        return "The comment has been edited successfully"

    def delete_comments(self, comment_id, role):
        """Admin deletes a comment"""
        delete_comment = {}
        if role == 'admin':
            for dcomment in comments:
                if comment["id"] = comment_id:
                    delete_comment = dcomment

        


    

