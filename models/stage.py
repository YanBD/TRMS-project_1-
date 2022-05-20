class Stage:
    def __init__(self, stage_id='', stage_desc=''):
        self.stage_id = stage_id
        self.stage_desc = stage_desc

    def __repr__(self):
        return str({
            'stage_id': self.stage_id,
            'stage_desc': self.stage_desc
        })
