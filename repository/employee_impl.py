from exceptions.resource_not_found import ResourceNotFound
from repository.employee_repo import EmployeeRepo
from utility.db_conn import connection
from models.employee import Employee


def _build_employee(query):
    return Employee(emp_id=query[0], last_name=query[1], first_name=query[2], title=query[3],
                    supervisor=query[4], department=query[5], dept_head=query[6])


class EmployeeImpl(EmployeeRepo):
    def create_employee(self, employee):
        sql = 'insert into employee values (default,%s,%s,%s,%s,%s,%s) returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [employee.last_name, employee.first_name, employee.title, employee.supervisor,
                             employee.department, employee.dept_head])
        connection.commit()
        query = cursor.fetchone()
        return _build_employee(query)

    def update_employee(self, update):
        sql = 'update employee set last_name = %s, first_name=%s, title=%s, supervisor =%s,' \
              'department =%s where emp_id=%s returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [update.last_name, update.first_name, update.title, update.supervisor, update.department,
                             update.emp_id])
        connection.commit()
        query = cursor.fetchone()
        if query:
            return _build_employee(query)
        else:
            raise ResourceNotFound(f'Employee {update.emp_id} not found in system')

    def all_employees(self):
        sql = 'select * from employee order by emp_id asc'
        cursor = connection.cursor()
        cursor.execute(sql)
        query = cursor.fetchall()
        emp_list = [_build_employee(employee) for employee in query]
        return emp_list

    def get_employee(self, emp_id):
        sql = 'select * from employee where emp_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [emp_id])
        query = cursor.fetchone()
        if query:
            return _build_employee(query)
        else:
            raise ResourceNotFound(f'Could not locate Employee with id {emp_id}')

    def delete_employee(self, emp_id):
        if self.get_employee(emp_id):
            sql = 'delete from employee where emp_id=%s'
            cursor = connection.cursor()
            cursor.execute(sql, [emp_id])
            connection.commit()
        else:
            raise ResourceNotFound(f'Could not process, Employee{emp_id} not found')


def _test():
    er = EmployeeImpl()
    # employee = Employee(last_name='Watson', first_name='Dean', title='Department Head',
    #                     department='Technology')
    # employee = er.create_employee(employee)
    # print(employee)
    # print('-Create Employee_')
    employee = er.get_employee(15)
    employee.supervisor = 11
    employee.first_name = 'Cassie'
    employee.last_name = 'Cupcake'
    employee.department = ['Technology', 'Public Relation']
    employee.title = 'Supervisor'
    employee = er.update_employee(employee)
    print(employee)
    print('--Update Employee--')
    for a in er.all_employees():
        print(a)


if __name__ == '__main__':
    _test()
