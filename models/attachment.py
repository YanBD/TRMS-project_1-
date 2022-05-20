class Attachment:
    def __init__(self, attach_id=0, request_id='',file_type=''):
        self.attach_id = attach_id
        self.request_id = request_id
        self.file_type = file_type

    def __repr__(self):
        return str({
            'attach_id': self.attach_id,
            'request_id': self.request_id,
            'file_type': self.file_type
        })
        