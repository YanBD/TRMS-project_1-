from models.userbase import UserBase
from repository.userbase_impl import UserbaseImpl
from repository.userbase_repo import UserbaseRepo


class UserbaseServ:
    def __init__(self, userbase_rep: UserbaseRepo):
        self.userbase_rep = userbase_rep

    def create_userbase(self, userbase):
        return self.userbase_rep.create_userbase(userbase)

    def authenticate_user(self, userbase):
        return self.userbase_rep.authenticate_user(userbase)

    def update_userbase(self, update):
        return self.userbase_rep.update_user(update)

    def delete_user(self, emp_id):
        return self.userbase_rep.delete_user(emp_id)

def _test():
    serv = UserbaseServ(UserbaseImpl())
    user = UserBase(username='dwatson', passphrase='password')
    user = serv.authenticate_user(user)
    print(user)


if __name__ == '__main__':
    _test()

