from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.stage import Stage
from repository.stage_impl import StageImpl
from services.stage_serv import StageServ

sr = StageImpl()
serv = StageServ(sr)


def route(app):
    @app.route('/stage/<stage_id>', methods=['put'])
    def update_stage(stage_id):
        body = request.json
        stage = Stage(stage_id=stage_id, stage_desc=body['stageDesc'])
        nstage = serv.update_stage(stage)
        if nstage:
            return jsonify(stage), 200
        else:
            return nstage, 404

    @app.route('/stage', methods=['get'])
    def all_stage():
        stage = [stage for stage in serv.all_stage()]
        return jsonify(stage)

    @app.route('/reimbursement/<request_id>', methods=['get'])
    def get_stage(request_id):
        try:
            stage = serv.get_stage(int(request_id))
            return jsonify(stage)
        except ValueError:
            return f'{request_id} not a valid format'
        except ResourceNotFound as r:
            return r.message

    @app.route('/reimbursement/<request_id>', methods=['delete'])
    def delete_stage(request_id):
        try:
            serv.delete_stage(request_id)
            return f'{request_id} stage successfully deleted'
        except ResourceNotFound as r:
            return r.message

