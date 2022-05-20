from exceptions.resource_not_found import ResourceNotFound
from models.stage import Stage
from repository.stage_repo import StageRepo
from utility.db_conn import connection


def _build_stage(query):
    return Stage(stage_id=query[0], stage_desc=query[1])


class StageImpl(StageRepo):
    def update_stage(self, update):
        sql = 'update stage set stage_desc=%s where stage_id=%s returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [update.stage_desc, update.stage_id])
        connection.commit()
        query = cursor.fetchone()
        if query:
            return _build_stage(query)
        else:
            return ResourceNotFound(f'Stage ID({update.stage_id}) does not match list of known Stages')

    def all_stage(self):
        sql = 'select * from stage'
        cursor = connection.cursor()
        cursor.execute(sql)
        querys = cursor.fetchall()
        stage_list = [_build_stage(query) for query in querys]
        return stage_list

    def get_stage(self, stage_id):
        sql = 'select * from stage where stage_id=%s'
        cursor = connection.cursor()
        cursor.execute(sql[stage_id])
        query = cursor.fetchone()
        if query:
            return _build_stage(query)
        else:
            return ResourceNotFound(f'Stage ID({stage_id}) does not match list of known Stages')

    def delete_stage(self, stage_id):
        sql = 'delete from stage where stage_id =%s'
        cursor = connection.cursor()
        check = self.get_stage(stage_id)
        if check:
            cursor.execute(sql, [stage_id])
            connection.commit()
        else:
            return ResourceNotFound(f'Stage ID({stage_id}) does not match list of known Stages')
