"""
Файл содержит pydantic модели, для сериализации и валидации данных
"""
from typing import List

from pydantic import BaseModel
from datetime import date


class Genre(BaseModel):
    name: str


class Author(BaseModel):
    first_name: str
    last_name: str
    age: int


class Book(BaseModel):
    """
    Основываясь на этой модели, pydantic будет валидировать данные, которые проходят через него.
    """
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genre]
    pages: int
