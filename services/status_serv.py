from repository.status_repo import StatusRepo


class StatusServ:
    def __init__(self, status_repo: StatusRepo):
        self.status_repo = status_repo

    def update_status(self, update):
        return self.status_repo.update_status(update)

    def all_status(self):
        return self.status_repo.all_status()

    def get_status(self, status_id):
        return self.status_repo.get_status(status_id)

    def delete_status(self, status_id):
        return self.status_repo.delete_status(status_id)
