from repository.stage_repo import StageRepo


class StageServ:
    def __init__(self, stage_repo: StageRepo):
        self.stage_repo = stage_repo

    def update_stage(self, update):
        return self.stage_repo.update_stage(update)

    def all_stage(self):
        return self.stage_repo.all_stage()

    def get_stage(self, stage_id):
        return self.stage_repo.get_stage(stage_id)

    def delete_stage(self, stage_id):
        return self.stage_repo.delete_stage(stage_id)
