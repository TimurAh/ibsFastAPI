import logging
import time
import logging.config
from contextvars import ContextVar
from app.models.config_logger import logger_output
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

logging.config.dictConfig(logger_output)
output_log = logging.getLogger("output")
client_host: ContextVar[str | None] = ContextVar("client_host", default=None)

"""
Задание_7. Логирование в FastAPI с использованием middleware.

Написать конфигурационный файл для логгера "output"
Формат выводимых логов:
[CURRENT_DATETIME] {file: line} LOG_LEVEL - | EXECUTION_TIME_SEC | HTTP_METHOD | URL | STATUS_CODE |
[2023-12-15 00:00:00] {example:62} INFO | 12 | GET | http://localhost/example | 200 |


Дописать класс CustomMiddleware.
Добавить middleware в приложение (app).
"""


class CustomMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        """Load request ID from headers if present. Generate one otherwise."""
        client_host.set(request.client.host)

        """Ваша реализация."""

        # В случае ошибки при запросе, возвращать код 500
        # response = Response("Internal Server Error", status_code=500)
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        output_log.info("Accepted request", extra={'method': request.method, 'url': request.url,
                                                   'status_code': 200, 'process_time': process_time})
        # 'method', request.method, 'url', request.url,
        # 'status_code', '200', 'process_time', str(process_time
        return response
