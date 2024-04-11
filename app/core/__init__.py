import io
import traceback
from abc import ABC, abstractmethod
from io import StringIO
import pandas
from fastapi import UploadFile, File


def convert_arabic_to_roman(number: int) -> str:
    pass


def convert_roman_to_arabic(number: str) -> int:
    pass


def average_age_by_position(file : UploadFile):

    df = pandas.read_csv(file.file, encoding='utf-8')
    answer = df.groupby('Должность').agg({'Возраст':['mean']}).to_json (orient='columns')
    return answer
"""
Задание_6.
Дан класс DataGenerator, который имеет два метода: generate(), to_file()
Метод generate генерирует данные формата list[list[int, str, float]] и записывает результат в
переменную класса data
Метод to_file сохраняет значение переменной generated_data по пути path c помощью метода
write, классов JSONWritter, CSVWritter, YAMLWritter.

Допишите реализацию методов и классов.
"""
class BaseWriter(ABC):
    """Абстрактный класс с методом write для генерации файла"""

    @abstractmethod
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        """
        Записывает данные в строковый объект файла StringIO
        :param data: полученные данные
        :return: Объект StringIO с данными из data
        """

        pass


class JSONWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в json формате"""

    """Ваша реализация"""
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        str_io = ''
        str_io += '{ \n'
        for i,wordLine in enumerate(data):
            str_io += f'"line{i+1}"' + ': { '
            for j,word in enumerate(wordLine):
                str_io += f'"{str(word)}"' + ": " + str(word) + (", " if j != len(wordLine) - 1 else '')
            str_io += '},\n' if i != len(data) - 1 else "}"
        str_io += ' \n}'
        return StringIO(str_io)


class CSVWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в csv формате"""

    """Ваша реализация"""

    def write(self, data: list[list[int, str, float]]) -> StringIO:
        str_io = ''
        for i, wordLine in enumerate(data):
            str_io += f"stolbes_{i}" + (", " if i != len(wordLine) - 1 else '')
        str_io +='\n'
        for wordLine in data:
            for j, word in enumerate(wordLine):
                str_io += str(word) + (", " if j != len(wordLine) - 1 else '')
            str_io += "\n"
        return StringIO(str_io)



class YAMLWriter(BaseWriter):
    """Потомок BaseWriter с переопределением метода write для генерации файла в yaml формате"""

    """Ваша реализация"""
    def write(self, data: list[list[int, str, float]]) -> StringIO:
        str_io = ''
        str_io += '<?xml version="1.0" encoding="UTF-8"?>\n<yml_catalog>\n'
        for i, wordLine in enumerate(data):
            str_io += f'\t<line id="{i + 1}">\n'
            for j, word in enumerate(wordLine):
                str_io += f'\t\t<{str(word)}>' + str(word) + f'</{str(word)}>\n'
            str_io += '\t</line>\n'
        str_io += ' \n</yml_catalog>'
        return StringIO(str_io)

fake_db_files={'id':'namefile'}
class DataGenerator:
    def __init__(self, data: list[list[int, str, float]] = None):
        self.data: list[list[int, str, float]] = data
        self.file_id = None

    def generate(self, matrix_size) -> None:
        """Генерирует матрицу данных заданного размера."""

        data: list[list[int, str, float]] = []
        """Ваша реализация"""
        i = 0
        j = 0
        while i < matrix_size:
            data.append([])
            while j < matrix_size:
                data[i].append(str(i+1) + str(j+1))
                j += 1
            j = 0
            i += 1
        self.data = data

    def to_file(self, path: str , writer) -> None:
        """
        Метод для записи в файл данных полученных после генерации.
        Если данных нет, то вызывается кастомный Exception.
        :param path: Путь куда требуется сохранить файл
        :param writer: Одна из реализаций классов потомков от BaseWriter
        """

        """Ваша реализация"""
        self.file_id = len(fake_db_files)
        self.path = "app/files/" + str(self.file_id) + "." + writer
        wr = None
        if writer == 'json':
            wr = JSONWriter()
            file_text = wr.write(self.data)
        elif writer == 'yml':
            wr = YAMLWriter()
            file_text = wr.write(self.data)
        elif writer == 'csv':
            wr = CSVWriter()
            file_text = wr.write(self.data)
        try:
            print('Запись файла началась')
            with open(self.path, 'w') as f:
                f.write(file_text.getvalue())
        except IOError:
            print(traceback.format_exc())
        pass
