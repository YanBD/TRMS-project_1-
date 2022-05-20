from repository.ev_type_repo import EvTypeRepo


class EvTypeServ:
    def __init__(self, ev_type_repo: EvTypeRepo):
        self.ev_type_repo = ev_type_repo

    def update_ev_type(self, update):
        return self.ev_type_repo.update_ev_type(update)

    def all_ev_type(self):
        return self.ev_type_repo.all_ev_type()

    def get_ev_type(self, event_id):
        return self.ev_type_repo.get_ev_type(event_id)

    def delete_ev_type(self, event_id):
        return self.ev_type_repo.delete_ev_type(event_id)
        