from flask import jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from models.info_request import InfoRequest
from repository.info_request_impl import InfoRequestImpl
from services.info_request_serv import InfoRequestServ

ir = InfoRequestImpl()
serv = InfoRequestServ(ir)


def route(app):
    @app.route('/info_request/<info_id>', methods=['get'])
    def get_info_request(info_id):
        try:
            info_request = serv.get_info_request(int(info_id))
            if info_request:
                return jsonify(info_request), 200
        except ValueError:
            return f'{info_id} not a valid Info Request Id'
        except ResourceNotFound as r:
            return r.message

    @app.route('/info_request', methods=['post'])
    def create_info_request():
        body = request.json
        req = InfoRequest(related_id=body['relatedID'], destination_id=body['destinationId'],
                          sender_id=body['senderId'], sender=body['sender'], description=body['description'])
        nreq = serv.create_info_request(req)
        return jsonify(nreq), 200

    @app.route('/info_request/<info_id>', methods=['put'])
    def update_info_request(info_id):
        body = request.json
        req = InfoRequest(info_id=info_id, related_id=body['relatedId'], destination_id=body['destinationId'],
                          description=body['description'])
        nreq = serv.update_info_request(req)
        if nreq:
            return jsonify(nreq), 200
        else:
            return nreq, 404

    @app.route('/info_request/<info_id>', methods=['delete'])
    def delete_info_request(info_id):
        try:
            serv.delete_info_request(info_id)
            return f'Information request {info_id} successfully deleted', 204
        except ResourceNotFound as r:
            return r.message
