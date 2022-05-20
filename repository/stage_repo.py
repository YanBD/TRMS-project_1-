from abc import ABC, abstractmethod


class StageRepo(ABC):

    @abstractmethod
    def update_stage(self, update):
        pass

    @abstractmethod
    def all_stage(self):
        pass

    @abstractmethod
    def get_stage(self,stage_id):
        pass

    @abstractmethod
    def delete_stage(self, stage_id):
        pass
