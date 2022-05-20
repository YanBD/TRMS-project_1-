from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.userbase import UserBase
from repository.userbase_impl import UserbaseImpl
from services.userbase_serv import UserbaseServ

ur = UserbaseImpl()
serv = UserbaseServ(ur)


def route(app):
    @app.route('/userbase', methods=['post'])
    def create_user():
        body = request.json
        user = UserBase(emp_id=body['empId'], username=body['username'], passphrase=body['passphrase'])
        nuser = serv.create_userbase(user)
        return nuser.json()

    @app.route('/userbase', methods=['patch'])
    def authenticate_user():
        args = request.args
        if 'username' and 'passphrase' in args:
            user = UserBase(username=args['username'], passphrase=args['passphrase'])
            nuser = (serv.authenticate_user(user))

            return str(nuser.emp_id)
        body = request.json
        auth = UserBase(username=body['username'], passphrase=body['passphrase'])
        try:
            auth = serv.authenticate_user(auth)
            if auth:
                return auth.json()
        except ResourceNotFound as r:
            return r.message, 404

    @app.route('/userbase/<emp_id>', methods=['put'])
    def update_user(emp_id):
        body = request.json
        user = UserBase(emp_id=emp_id, username=body['username'], passphrase=body['passphrase'])
        nuser = serv.update_userbase(user)
        if nuser:
            return jsonify(nuser)
        else:
            return nuser
