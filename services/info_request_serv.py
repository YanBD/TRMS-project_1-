from repository.info_request_repo import InfoRequestRepo


class InfoRequestServ:
    def __init__(self, info_request_repo: InfoRequestRepo):
        self.info_request_repo = info_request_repo

    def create_info_request(self, info_request):
        return self.info_request_repo.create_info_request(info_request)

    def update_info_request(self, update):
        return self.info_request_repo.update_info_request(update)

    def get_info_request(self, info_id):
        return self.info_request_repo.get_info_request(info_id)

    def delete_info_request(self, info_id):
        return self.info_request_repo.delete_info_request(info_id)
