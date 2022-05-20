class Status:
    def __init__(self, status_id='',status_desc=''):
        self.status_id = status_id
        self.status_desc = status_desc

    def __repr__(self):
        return str({
            'status_id': self.status_id,
            'status_desc': self.status_desc
        })
