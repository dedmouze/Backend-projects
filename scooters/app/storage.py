import typing as tp

from app.context import AppContext
from app import models


async def get_scooters(context: AppContext) -> tp.List[models.Scooter]:
    sql = '''
    SELECT id, location, "user" FROM scooters
    '''

    rows = await context.db.fetch(sql)

    return [models.Scooter.from_db(row) for row in rows]
