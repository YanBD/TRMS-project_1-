from repository.employee_repo import EmployeeRepo


class EmployeeServ:

    def __init__(self, employee_repo: EmployeeRepo):
        self.employee_repo = employee_repo

    def create_employee(self, employee):
        return self.employee_repo.create_employee(employee)

    def update_employee(self, update):
        return self.employee_repo.update_employee(update)

    def all_employees(self):
        return self.employee_repo.all_employees()

    def get_employee(self, emp_id):
        return self.employee_repo.get_employee(emp_id)

    def delete_employee(self, emp_id):
        return self.employee_repo.delete_employee(emp_id)
