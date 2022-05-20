from flask import jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from models.ev_type import EvType
from repository.ev_type_impl import EvTypeImpl
from services.ev_type_serv import EvTypeServ

er = EvTypeImpl()
serv = EvTypeServ(er)


def route(app):
    @app.route('/events', methods=['get'])
    def all_events():
        event = [event.json() for event in serv.all_ev_type()]
        return jsonify(event)

    @app.route('/events/<event_id>', methods=['get'])
    def get_event(event_id):
        try:
            event = serv.get_ev_type(event_id)
            return event, 200
        except ResourceNotFound as r:
            return r.message, 400

    @app.route('/events/<event_id>', methods=['put'])
    def update_event(event_id):
        body = request.json
        event = EvType(event_id=event_id, event_type=body['eventType'],
                       reimbursement_coverage=body['reimbursementCoverage'])
        event = serv.update_ev_type(event)
        if event:
            return event.json()
        else:
            return event

    @app.route('/events/<event_id>', methods=['delete'])
    def delete_event(event_id):
        try:
            serv.delete_ev_type(event_id)
            return f'Event {event_id} successfully deleted'
        except ResourceNotFound as r:
            return r.message
