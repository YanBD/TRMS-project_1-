from abc import ABC, abstractmethod


class UserbaseRepo(ABC):

    @abstractmethod
    def create_userbase(self, userbase):
        pass

    @abstractmethod
    def authenticate_user(self, userbase):
        pass

    @abstractmethod
    def update_user(self, update):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass
