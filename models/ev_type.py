class EvType:
    def __init__(self, event_id='', event_type='', reimbursement_coverage=''):
        self.event_id = event_id
        self.event_type = event_type
        self.reimbursement_coverage = reimbursement_coverage

    def __repr__(self):
        return str({
            'event_id': self.event_id,
            'event_type': self.event_type,
            'reimbursement_coverage': self.reimbursement_coverage
        })

    def json(self):
        return {
            'eventId': self.event_id,
            'eventType': self.event_type,
            'reimbursementCoverage': self.reimbursement_coverage
        }