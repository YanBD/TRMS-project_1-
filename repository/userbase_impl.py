from exceptions.resource_not_found import ResourceNotFound
from models.userbase import UserBase
from repository.userbase_repo import UserbaseRepo
from utility.db_conn import connection


def _build_userbase(query):
    return UserBase(user_id=query[0], emp_id=query[int(1)], username=query[2], passphrase=query[3])


class UserbaseImpl(UserbaseRepo):
    def create_userbase(self, userbase):
        sql = 'insert into userbase values (default, %s,%s,%s) returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [userbase.emp_id, userbase.username, userbase.passphrase])
        connection.commit()
        query = cursor.fetchone()
        if query:
            return _build_userbase(query)
        else:
            return ResourceNotFound(f'Employee ID({userbase.emp_id}) not found could not create user credentials')

    def authenticate_user(self, userbase):
        sql = 'select * from userbase where username=%s and passphrase=%s'
        cursor = connection.cursor()
        cursor.execute(sql, [userbase.username, userbase.passphrase])
        query = cursor.fetchone()
        if query:
            return _build_userbase(query)
        else:
            raise ResourceNotFound(f'User could not be authenticated')

    def update_user(self, update):
        sql = 'update userbase set username = %s , passphrase=%s where emp_id =%s returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [update.username, update.passphrase, update.emp_id])
        connection.commit()
        query = cursor.fetchone()
        if query:
            return _build_userbase(query)
        else:
            return ResourceNotFound(f'Employee ID({update.emp_id}) missmatch')

    def delete_user(self, emp_id):
        try:
            sql = 'delete from userbase where emp_id=%s'
            cursor = connection.cursor()
            cursor.execute(sql, [emp_id])
            connection.commit()
            return f'Employee ID({emp_id}) user credential successfully deleted'
        except ResourceNotFound:
            raise f'Could not process User{emp_id} does not have credentials'


def _test():
    user = UserBase(username='dwatson', passphrase='password')
    user = UserbaseImpl().authenticate_user(user)
    print(user)


if __name__ == '__main__':
    _test()
