from repository.reimburse_status_repo import ReimburseStatusRepo


class ReimburseStatusServ:
    def __init__(self, reimburse_status_repo: ReimburseStatusRepo):
        self.reimburse_status_repo = reimburse_status_repo

    def create_reimburse_status(self, status):
        return self.reimburse_status_repo.create_reimburse_status(status)

    def update_reimburse_status(self, update):
        return self.reimburse_status_repo.update_reimburse_status(update)

    def all_reimburse_status(self):
        return self.reimburse_status_repo.all_reimburse_status()

    def get_reimburse_status(self, request_id):
        return self.reimburse_status_repo.get_reimburse_status(request_id)

    def delete_reimburse_status(self, request_id):
        return self.reimburse_status_repo.delete_reimburse_status()
