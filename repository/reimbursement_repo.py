from abc import ABC, abstractmethod


class ReimbursementRepo(ABC):
    @abstractmethod
    def create_reimbursement(self,request):
        pass

    @abstractmethod
    def update_reimbursement(self,update):
        pass

    @abstractmethod
    def get_reimbursement(self,request_id):
        pass

    @abstractmethod
    def all_reimbursement(self):
        pass

    @abstractmethod
    def delete_reimbursement(self, request_id):
        pass

