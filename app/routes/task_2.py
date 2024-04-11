from typing import Annotated

from fastapi import APIRouter, Body

from app.core import convert_arabic_to_roman, convert_roman_to_arabic
from app.models import ConverterResponse


router = APIRouter(tags=["Стажировка"])

"""
Задание_2. Конвертер
    1. Реализовать функции convert_arabic_to_roman() и convert_roman_to_arabic() из пакета app.core
    2. Написать логику и проверки для вводимых данных. Учитывать, что если арабское число выходит за пределы 
    от 1 до 3999, то возвращать "не поддерживается"
    3. Запустить приложение и проверить результат через swagger
"""
@router.post("/converter", description="Задание_2. Конвертер")
async def convert_number(number: Annotated[int | str, Body()]) -> ConverterResponse:
    """
    Принимает арабское или римское число.
    Конвертирует его в римское или арабское соответственно.
    Возвращает первоначальное и полученное числа в виде json:
    {
        "arabic": 10,
        "roman": "X"
    }
    """
    list_rim_nums = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                     'V': 5, 'IV': 4, 'I': 1}
    roman_answer = ''
    number_answer = 0
    if isinstance(number, int):
        number_answer = number
        for letter, value in list_rim_nums.items():
            while number >= value:
                roman_answer += letter
                number -= value
    elif isinstance(number, str):
        roman_answer=number
        for letter, value in list_rim_nums.items():
            while number.find(letter) != -1 :
                print(letter)
                number_answer+=value
                number=number.replace(letter,'',1)
                print('Убрали, получили ' +number)

    converter_response = ConverterResponse(arabic=number_answer,roman=roman_answer)
    return converter_response
