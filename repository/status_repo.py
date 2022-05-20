from abc import ABC, abstractmethod


class StatusRepo(ABC):
    @abstractmethod
    def update_status(self, update):
        pass

    @abstractmethod
    def all_status(self):
        pass

    @abstractmethod
    def get_status(self, status_id):
        pass

    @abstractmethod
    def delete_status(self, status_id):
        pass

