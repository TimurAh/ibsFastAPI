from fastapi import APIRouter, Response
from functools import wraps
router = APIRouter(tags=["Стажировка"])

"""
Задание_8. Декоратор - счётчик запросов.

Напишите декоратор который будет считать кол-во запросов сделанных к приложению.
Оберните роут new_request() этим декоратором.
Подумать, как хранить переменную с кол-вом сделаных запросов.
"""
fake_db_count={'count':0}#можно сделать через глобальную переменную, но не красиво
def count_requests(count_requests_this):

    @wraps(count_requests_this)
    async def wrapper(*args, **kwargs):
        fake_db_count['count'] = fake_db_count['count'] + 1
        return await count_requests_this(*args, **kwargs)
    return wrapper


@router.get("/new_request", description="Задание_8. Декоратор - счётчик запросов.")
@count_requests
async def new_request():
    """Возвращает кол-во сделанных запросов."""

    return str(fake_db_count['count'])
