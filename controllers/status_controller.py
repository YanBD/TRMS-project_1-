from flask import jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from models.status import Status
from repository.status_impl import StatusImpl
from services.status_serv import StatusServ

sr = StatusImpl()
serv = StatusServ(sr)


def route(app):
    @app.route('/status', methods=['get'])
    def all_status():
        status = [status for status in serv.all_status()]
        return jsonify(status)

    @app.route('/status/<status_id>', methods=['get'])
    def get_status(status_id):
        try:
            status = serv.get_status(int(status_id))
            if status:
                return jsonify(status)
        except ValueError:
            return f'{status_id} not valid status type'
        except ResourceNotFound as r:
            return r.message

    @app.route('/status/<status_id>', methods=['put'])
    def update_status(status_id):
        body = request.json
        status = Status(status_id=status_id, status_desc=body['statusDesc'])
        nstatus = serv.update_status(status)
        if nstatus:
            return jsonify(nstatus), 200
        else:
            return nstatus, 404

    @app.route('/status/<status_id>', methods=['delete'])
    def delete_status(status_id):
        try:
            serv.delete_status(status_id)
            return f'Status {status_id} successfully deleted', 200
        except ResourceNotFound as r:
            return r.message
