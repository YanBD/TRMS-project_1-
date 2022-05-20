from exceptions.resource_not_found import ResourceNotFound
from models.info_request import InfoRequest
from repository.info_request_repo import InfoRequestRepo
from utility.db_conn import connection


def _build_info_request(query):
    return InfoRequest(info_id=query[0], related_id=query[1], destination_id=query[2], sender_id=query[3],
                       sender=query[4], description=query[5], request_date=query[6], request_time=query[7])


class InfoRequestImpl(InfoRequestRepo):
    def create_info_request(self, info_request):
        sql = 'insert into info_request values (default,%s,%s,%s,%s,%s) returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [info_request.related_id, info_request.destination_id, info_request.sender_id,
                             info_request.sender, info_request.description])
        connection.commit()
        query = cursor.fetchone()
        if query:
            return _build_info_request(query)
        else:
            return ResourceNotFound(f'No Information request match search criteria')

    def update_info_request(self, update):
        sql = 'update info_request set related_id=%s, destination_id=%s,description=%s where info_id=%s returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [update.related_id, update.destination_id, update.description, update.info_id])
        connection.commit()
        query = cursor.fetchone()
        return _build_info_request(query)

    def get_info_request(self, info_id):
        sql = 'select * from info_request where info_id=%s'
        cursor = connection.cursor()
        cursor.execute(sql, [info_id])
        query = cursor.fetchone()
        if query:
            return _build_info_request(query)
        else:
            return ResourceNotFound(f'No Information request match search criteria')

    def delete_info_request(self, info_id):
        sql = 'delete from info_request where info_id=%s'
        cursor = connection.cursor()
        test = self.get_info_request(info_id)
        if test:
            cursor.execute(sql, [info_id])
        else:
            return ResourceNotFound(f'No Information request match search criteria')
