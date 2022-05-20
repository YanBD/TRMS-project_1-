from abc import ABC, abstractmethod


class ReimburseStatusRepo(ABC):
    @abstractmethod
    def create_reimburse_status(self, status):
        pass

    @abstractmethod
    def update_reimburse_status(self, update):
        pass

    @abstractmethod
    def all_reimburse_status(self):
        pass

    @abstractmethod
    def get_reimburse_status(self, request_id):
        pass

    @abstractmethod
    def delete_reimburse_status(self, request_id):
        pass
    