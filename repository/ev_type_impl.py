from exceptions.resource_not_found import ResourceNotFound
from models.ev_type import EvType
from repository.ev_type_repo import EvTypeRepo
from utility.db_conn import connection


def _build_event(query):
    return EvType(event_id=query[0], event_type=query[1], reimbursement_coverage=query[2])


class EvTypeImpl(EvTypeRepo):
    def update_ev_type(self, update):
        sql = 'update ev_type set event_type = %s, reimbursement_coverage = %s where event_id = %s returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [update.ev_type, update.reimbursement_coverage, update.event_id])
        connection.commit()
        query = cursor.fetchone()
        if query:
            return _build_event(query)
        else:
            return ResourceNotFound(f'Event ID({update.event_id}) did not match list of known Event Types')

    def all_ev_type(self):
        sql = 'select * from ev_type'
        cursor = connection.cursor()
        cursor.execute(sql)
        querys = cursor.fetchall()
        ev_list = [_build_event(query) for query in querys]
        return ev_list

    def get_ev_type(self, event_id):
        sql = 'select * from ev_type where event_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [event_id])
        query = cursor.fetchone()
        if query:
            return _build_event(query).json()
        else:
            return ResourceNotFound(f'Event ID({event_id}) did not match list of known Event Types')

    def delete_ev_type(self, event_id):
        sql = 'delete from ev_type where event_id=%s'
        cursor = connection.cursor()
        check = self.get_ev_type(event_id)
        if check:
            cursor.execute(sql, [event_id])
            connection.commit()
        else:
            return ResourceNotFound(f'Event ID({event_id}) did not match list of known Event Types')
