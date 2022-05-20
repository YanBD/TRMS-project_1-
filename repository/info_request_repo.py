from abc import ABC, abstractmethod


class InfoRequestRepo(ABC):
    @abstractmethod
    def create_info_request(self, info_request):
        pass

    @abstractmethod
    def update_info_request(self, update):
        pass

    @abstractmethod
    def get_info_request(self, info_id):
        pass

    @abstractmethod
    def delete_info_request(self, info_id):
        pass
