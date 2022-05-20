import flask
from flask import jsonify, request
from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee
from repository.employee_impl import EmployeeImpl
from services.employye_serv import EmployeeServ

er = EmployeeImpl()
es = EmployeeServ(er)


def route(app):
    @app.route('/employee/<emp_id>', methods=['Get'])
    def get_employee(emp_id):
        try:
            employee = es.get_employee(int(emp_id))
            # response = flask.Response(repr(employee))
            # response.headers['Content-Type'] = 'application/json'
            if employee:
                return employee.json()
        except ValueError:
            return f'{emp_id} no a valid Employee Id Type'
        except ResourceNotFound as r:
            return r.message, 404

    @app.route('/employee', methods=['get'])
    def all_employee():
        employee = [emp.json() for emp in es.all_employees()]
        return jsonify(employee)

    @app.route('/employee', methods=['post'])
    def add_employee():
        body = request.json
        employee = Employee(last_name=body['lastName'], first_name=body['firstName'], title=body['title'],
                            supervisor=body['supervisor'], department=body['department'], dept_head=['deptHead'])
        nemployee = es.create_employee(employee)
        return nemployee.json(), 201

    @app.route('/employee/<emp_id>', methods=['put'])
    def update_employee(emp_id):
        body = request.json
        employee = Employee(emp_id=emp_id, last_name=body['lastName'], first_name=body['firstName'],
                            title=body['title'], supervisor=body['supervisor'], department=body['department'],
                            dept_head=body['deptHead'])
        try:
            nemployee = es.update_employee(employee)
            response = flask.Response(repr(nemployee))
            response.headers['Content-Type'] = 'application/json'
            return response
        except ResourceNotFound as r:
            return r.message, 404

    @app.route('/employee/<emp_id>', methods=['delete'])
    def delete_employee(emp_id):
        try:
            es.delete_employee(emp_id)
            return f'Employee {emp_id} successfully deleted'
        except ResourceNotFound as r:
            return r.message, 404
