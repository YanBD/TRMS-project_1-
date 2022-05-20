from exceptions.resource_not_found import ResourceNotFound
from models.reimbursement import Reimbursement
from repository.reimbursement_repo import ReimbursementRepo
from utility.db_conn import connection


def _build_reimburs(query):
    return Reimbursement(request_id=query[0], emp_id=query[1], ev_location=query[2], ev_cost=query[3],
                         ev_type=query[4], description=query[5], justification=query[6], grading_format=query[7],
                         grade=query[8])


class ReimbursementImpl(ReimbursementRepo):
    def create_reimbursement(self, request):
        sql = 'insert into reimbursement values (default,%s,%s,%s,%s,%s,%s,%s,%s) returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [request.emp_id, request.ev_location, request.ev_cost, request.ev_type, request.description,
                             request.justification, request.grading_format, request.grade])
        connection.commit()
        query = cursor.fetchone()
        return _build_reimburs(query)

    def update_reimbursement(self, update):
        sql = 'update reimbursement set ev_location=%s,ev_cost=%s,ev_type=%s,description=%s, justification=%s,' \
              'grading_format=$s,grade=%s where request_id=%S'
        cursor = connection.cursor()
        cursor.execute(sql,
                       [update.ev_location, update.ev_cost, update.ev_type, update.description, update.justification,
                        update.grading_format, update.grade])
        connection.commit()
        query = cursor.fetchone()
        if query:
            _build_reimburs(query)
        else:
            raise ResourceNotFound(f'NO Reimbursement request found')

    def get_reimbursement(self, request_id):
        sql = 'select * from reimbursement where request_id=$s'
        cursor = connection.cursor()
        cursor.execute(sql, [request_id])
        query = cursor.fetchone()
        return _build_reimburs(query)

    def all_reimbursement(self):
        sql = 'select * from reimbursement'
        cursor = connection.cursor()
        cursor.execute(sql)
        querys = cursor.fetchall()
        r_list = [_build_reimburs(query) for query in querys]
        return r_list

    def delete_reimbursement(self, request_id):
        sql = 'delete from reimbursement where request_id=%s'
        cursor = connection.cursor()
        test = self.get_reimbursement(request_id)
        if test:
            cursor.execute(sql, [request_id])
        else:
            raise ResourceNotFound(f'NO Reimbursement request found')
