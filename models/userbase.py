class UserBase:
    def __init__(self, user_id=0, emp_id=0, username='', passphrase=''):
        self.user_id = user_id
        self.emp_id = emp_id
        self.username = username
        self.passphrase = passphrase

    def __repr__(self):
        return str({
            "user_id": self.user_id,
            "emp_id": self.emp_id,
            "username": self.username,
            "passphrase": self.passphrase
        })

    def json(self):
        return {
            'userId': self.user_id,
            'empId': self.emp_id,
            'username': self.username,
            'passphrase': self.passphrase
        }

