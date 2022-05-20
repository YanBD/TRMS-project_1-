import datetime


class InfoRequest:
    def __init__(self, info_id=0, related_id='', destination_id='', sender_id='', sender='', description='',
                 request_date='', request_time=''):
        self.info_id = info_id
        self.related_id = related_id
        self.destination_id = destination_id
        self.sender_id = sender_id
        self.sender = sender
        self.description = description
        self.request_date = request_date
        self.request_time = request_time

        if self.info_id:
            self.request_date = datetime.datetime.now().strftime('%x')
            self.request_time = datetime.datetime.now().strftime('%X')

    def __repr__(self):
        return str({
            'info_id': self.info_id,
            'related_id': self.related_id,
            'destination_id': self.destination_id,
            'sender_id': self.sender_id,
            'sender': self.sender,
            'description': self.description,
            'request_date': self.request_date,
            'request_time': self.request_time
        })
