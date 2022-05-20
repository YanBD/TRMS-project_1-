class Reimbursement:
    def __init__(self, request_id=0, emp_id='', ev_location='', ev_cost=0, ev_type='', description='',
                 justification='', grading_format='', grade=''):
        self.request_id = request_id
        self.emp_id = emp_id
        self.ev_location = ev_location
        self.ev_cost = ev_cost
        self.ev_type = ev_type
        self.description = description
        self.justification = justification
        self.grading_format = grading_format
        self.grade = grade

    def __repr__(self):
        return str({
            'request_id': self.request_id,
            'emp_id': self.emp_id,
            'ev_location': self.ev_location,
            'ev_cost': self.ev_cost,
            'ev_type': self.ev_type,
            'description': self.description,
            'justification': self.justification,
            'grading_format': self.grading_format,
            'grade': self.grade
        })

    def json(self):
        return {
            'requestId': self.request_id,
            'empId': self.emp_id,
            'evLocation': self.ev_location,
            'evCost': self.ev_cost,
            'evType': self.ev_type,
            'description': self.description,
            'justification': self.justification,
            'gradingFormat': self.grading_format,
            'grade': self.grade
        }
    