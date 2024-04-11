import shutil

from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse

router = APIRouter(tags=["API для хранения файлов"])

"""
Задание_5. API для хранения файлов

a.	Написать API для добавления(POST) "/upload_file" и скачивания (GET) "/download_file/{id}" файлов. 
В ответ на удачную загрузку файла должен приходить id для скачивания. 
b.	Добавить архивирование к post запросу, то есть файл должен сжиматься и сохраняться в ZIP формате.
с*.Добавить аннотации типов.
"""
fake_db_files={'id':'namefile'}
@router.post("/upload_file", description="Задание_5. API для хранения файлов")
async def upload_file(file: UploadFile ):
    """Описание."""
    file_id:int = 0 #нужна БД, где будут id и имя нашего файла

    with open('app/files/' + file.filename, "wb") as wf:
        file_id+=1
        fake_db_files[1] = file.filename
        print(file.content_type)
        shutil.copyfileobj(file.file, wf)
        file.file.close()
    return file_id


@router.get("/download_file/{file_id}", description="Задание_5. API для хранения файлов")
async def download_file(file_id: int):
    """Описание."""

    file = FileResponse("app/files/"+fake_db_files[file_id])

    return file
