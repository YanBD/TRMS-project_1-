from exceptions.resource_not_found import ResourceNotFound
from models.status import Status
from repository.status_repo import StatusRepo
from utility.db_conn import connection


def _build_status(query):
    return Status(status_id=query[0],status_desc=query[1])


class StatusImpl(StatusRepo):
    def update_status(self, update):
        sql = 'update status set status_desc=%s where status_id=%s returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [update.status_desc, update.status_id])
        connection.commit()
        query = cursor.fetchone()
        if query:
            return _build_status(query)
        else:
            return ResourceNotFound(f'Status Id({update.status_id}) does not represent a valid status')

    def all_status(self):
        sql = 'select * from status'
        cursor = connection.cursor()
        cursor.execute(sql)
        querys = cursor.fetchall()
        status_list = [_build_status(query) for query in querys]
        return status_list

    def get_status(self, status_id):
        sql = 'select * from status where status_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [status_id])
        query = cursor.fetchone()
        return _build_status(query)

    def delete_status(self, status_id):
        sql = 'delete from status where status_id =%s'
        cursor = connection.cursor()
        check = self.get_status(status_id)
        if check:
            cursor.execute(sql, [status_id])
            connection.commit()
        else:
            return ResourceNotFound(f'Status Id({status_id}) does not represent a valid status')

