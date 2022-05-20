import datetime


class ReimburseStatus:
    def __init__(self, request_id='', projected_award='', status='', stage='', request_date='', request_time=''):
        self.request_id = request_id
        self.projected_award = projected_award
        self.status = status
        self.stage = stage
        self.request_date = request_date
        self.request_time = request_time

        # if self.request_id:
        self.request_date = datetime.datetime.now().strftime('%x')
        self.request_time = datetime.datetime.now().strftime('%X')

    def __repr__(self):
        return str({
            'request_id': self.request_id,
            'projected_award': self.projected_award,
            'status': self.status,
            'stage': self.stage,
            'request_date': self.request_date,
            'request_time': self.request_time
        })
