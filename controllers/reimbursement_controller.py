from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.reimbursement import Reimbursement
from repository.reimbursement_impl import ReimbursementImpl
from services.reimbursemet_serv import ReimbursementServ

rr = ReimbursementImpl()
serv = ReimbursementServ(rr)


def route(app):
    @app.route('/reimbursement', methods=['post'])
    def create_reimburse():
        body = request.json
        reim = Reimbursement(emp_id=body['empId'], ev_location=body['evLocation'], ev_cost=body['evCost'],
                             ev_type=body['evType'], description=body['description'],
                             justification=body['justification'], grading_format=body['gradingFormat'],
                             grade=body['grade'])

        nreim = serv.create_reimbursement(reim)
        return nreim.json()

    @app.route('/reimbursement/<request_id>', methods=['put'])
    def update_reimburse(request_id):
        body = request.json
        reim = Reimbursement(request_id=request_id ,ev_location=body['evLocation'], ev_cost=body['evCost'],
                             ev_type=body['evType'],description=body['description'], justification=body['justification'],
                             grading_format=body['gradingFormat'], grade=body['grade'])
        nreim = serv.update_reimbursement(reim)
        if nreim:
            return nreim.json()
        else:
            return nreim

    @app.route('/reimbursement', methods=['get'])
    def all_reimburse():
        reim = [reimburse.json() for reimburse in serv.all_reimbursement()]
        return jsonify(reim)

    @app.route('/reimbursement/<request_id>', methods=['get'])
    def get_reimburse(request_id):
        reim = serv.get_reimbursement(request_id)
        if reim:
            return reim.json(), 200
        else:
            return reim, 400

    @app.route('/reimbursement/<request_id>', methods=['delete'])
    def delete_reimburse(request_id):
        try:
            serv.delete_reimbursement(request_id)
            return f'Reimbursement {request_id} successfully deleted', 204
        except ResourceNotFound as r:
            return r.message
