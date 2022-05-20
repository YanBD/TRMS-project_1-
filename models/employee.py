class Employee:
    def __init__(self, emp_id=0, last_name='', first_name='', title='', supervisor="", department='', dept_head=bool):
        self.emp_id = emp_id
        self.last_name = last_name
        self.first_name = first_name
        self.title = title
        self.supervisor = supervisor
        self.department = department
        self.dept_head = dept_head

        if self.title == 'Department Head':
            self.dept_head = True
            self.supervisor = self.emp_id
        elif self.title == 'Benefits Coordinator':
            self.supervisor = self.emp_id
            self.dept_head = False
        else:
            self.dept_head = False

    def __repr__(self):
        return str({
            'emp_id': self.emp_id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'title': self.title,
            'supervisor': self.supervisor,
            'department': self.department,
            'dept_head': self.dept_head
        })

    def json(self):
        return {
            'empId': self.emp_id,
            'lastName': self.last_name,
            'firstName': self.first_name,
            'title': self.title,
            'supervisor': self.supervisor,
            'department': self.department,
            'deptHead': self.dept_head
        }
