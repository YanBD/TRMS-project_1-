from abc import ABC, abstractmethod


class EvTypeRepo(ABC):
    @abstractmethod
    def update_ev_type(self, update):
        pass

    @abstractmethod
    def all_ev_type(self):
        pass

    @abstractmethod
    def get_ev_type(self, event_id):
        pass

    @abstractmethod
    def delete_ev_type(self,event_id):
        pass
