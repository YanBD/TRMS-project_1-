from exceptions.resource_not_found import ResourceNotFound
from models.reimburse_status import ReimburseStatus
from repository.reimburse_status_repo import ReimburseStatusRepo
from utility.db_conn import connection


def _build_status(query):
    return ReimburseStatus(request_id=query[0], projected_award=query[1], status=query[2],stage=query[3],
                           request_date=query[4],request_time=query[5])


class ReimburseStatusImpl(ReimburseStatusRepo):
    def create_reimburse_status(self, status):
        sql = 'insert into reimburse_status values (default,%s,%s,%s) returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [status.projected_award, status.status, status.stage])
        connection.commit()
        query = cursor.fetchone()
        return _build_status(query)

    def update_reimburse_status(self, update):
        sql = 'update reimburse_status set projected_award=%s, status=%s,stage=%s where request_id=%s returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [update.projected_award, update.status, update.stage, update.request_id])
        connection.commit()
        query = cursor.fetchone()
        if query:
            return _build_status(query)
        else:
            return ResourceNotFound(f'No Information request match search criteria')

    def all_reimburse_status(self):
        sql = 'select * from reimburse_status'
        cursor = connection.cursor()
        cursor.execute(sql)
        querys = cursor.fetchall()
        status_list = [_build_status(query) for query in querys]
        return status_list

    def get_reimburse_status(self, request_id):
        sql = 'select * from reimburse_status where request_id=%s'
        cursor = connection.cursor()
        cursor.execute(sql, [request_id])
        query = cursor.fetchone()
        if query:
            return _build_status(query)
        else:
            return ResourceNotFound(f'No Information request match search criteria')

    def delete_reimburse_status(self, request_id):
        sql = 'delete from reimburse_status where request_id=%S'
        cursor = connection.cursor()
        if self.get_reimburse_status(request_id):
            cursor.execute(sql, request_id)
        else:
            return ResourceNotFound(f'No Information request match search criteria')