from repository.reimbursement_repo import ReimbursementRepo


class ReimbursementServ:
    def __init__(self, reimbursement_repo: ReimbursementRepo):
        self.reimbursement_repo = reimbursement_repo

    def create_reimbursement(self, request):
        return self.reimbursement_repo.create_reimbursement(request)

    def update_reimbursement(self, update):
        return self.reimbursement_repo.update_reimbursement(update)

    def get_reimbursement(self, request_id):
        return self.reimbursement_repo.get_reimbursement(request_id)

    def all_reimbursement(self):
        return self.reimbursement_repo.all_reimbursement()

    def delete_reimbursement(self, request_id):
        return self.reimbursement_repo.delete_reimbursement(request_id)
