from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.reimburse_status import ReimburseStatus
from repository.reimburse_status_impl import ReimburseStatusImpl
from services.reimburse_status_serv import ReimburseStatusServ

rs = ReimburseStatusImpl()
serv = ReimburseStatusServ(rs)


def route(app):
    @app.route('/reimburse_status', methods=['post'])
    def create_reimburse_status():
        body = request.json
        status = ReimburseStatus(projected_award=body['projectedAward'], status=body['status'], stage=body['stage'])
        nstatus = serv.create_reimburse_status(status)
        return jsonify(nstatus)

    @app.route('/reimburse_status/<request_id>', methods=['put'])
    def update_reimburse_status(request_id):
        body = request.json
        reim = ReimburseStatus(request_id=request_id, projected_award=body['projectedAward'], status=body['status'],
                               stage=body['stage'])
        nreim = serv.update_reimburse_status(reim)
        if nreim:
            return jsonify(nreim), 200
        else:
            return nreim, 404

    @app.route('/reimburse_status', methods=['get'])
    def all_reimburse_status():
        reim = [status for status in serv.all_reimburse_status()]
        return jsonify(reim)

    @app.route('/reimburse_status/<request_id>', methods=['get'])
    def get_reimburse_status(request_id):
        reim = serv.get_reimburse_status(request_id)
        if reim:
            return jsonify(reim)
        else:
            return reim

    @app.route('/reimburse_status/<request_id>', methods=['delete'])
    def delete_reimburse_status(request_id):
        try:
            serv.delete_reimburse_status(request_id)
            return f'Reimburse Status for {request_id} has been deleted', 204
        except ResourceNotFound as r:
            return r.message




