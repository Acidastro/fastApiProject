"""
Файл содержит pydantic модели, для сериализации и валидации данных
"""
from typing import List

from pydantic import BaseModel, validator, Field
from datetime import date


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    # first_name: str = Field(..., max_length=15)  # ограничение введенных символов в 25
    last_name: str
    age: int = Field(20, gt=15, lt=90,
                     description='Автор должен быть старше 15 и младше 90 лет')  # доп поля для валидирования. 15 < age < 90

    # @validator('age')
    # def check_age(cls, v):
    #     """
    #     Собственный валидатор, проверка значения больше 15
    #     """
    #     if v < 15:
    #         raise ValueError('Автор должен быть старше 15 и младше 90 лет')
    #     return v


class Book(BaseModel):
    """
    Основываясь на этой модели, pydantic будет валидировать данные, которые проходят через него.
    """
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre] = []  # По умолчанию пуст. К заполнению не обязателен.
    pages: int = 100


class BookOut(Book):
    id: int
