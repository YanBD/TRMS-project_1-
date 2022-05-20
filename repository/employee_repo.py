from abc import ABC, abstractmethod


class EmployeeRepo(ABC):
    @abstractmethod
    def create_employee(self, employee):
        pass

    @abstractmethod
    def update_employee(self, update):
        pass

    @abstractmethod
    def all_employees(self):
        pass

    @abstractmethod
    def get_employee(self, emp_id):
        pass

    @abstractmethod
    def delete_employee(self, emp_id):
        pass
