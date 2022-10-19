from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author  # Модель валидации

app = FastAPI()


@app.get('/')
def home():
    return {'key': 'hello'}


@app.get('/{pk}')
def get_item(pk: int, q: int = None):
    return {'key': pk, 'q': q}


@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {'user': pk, 'item': item}


@app.post('/author')
def create_author(author: Author = Body(..., embed=True)):
    """
    Создает автора по модели pydantic
    Body(..., embed=True) формирует ключ "author": {} внутри тела
    """
    return {
        'author': author
    }


@app.post('/book',
          response_model=Book,
          # response_model_exclude_unset=True,
          # response_model_exclude={"pages", "date"},
          response_model_include={"pages", "date"},
          )
def create_book(book: Book,
                # author: Author,
                # amount: int = Body(1)
                ):
    """
    Данные item должны соответствовать модели, описанной в классе Book (pydantic)
    Body позволяет добавить параметр в body запроса, а не в url адрес.
    response_model_exclude_unset=True Все параметры в схеме, которые определены по умолчанию, исключаются из ответа.
    response_model_exclude={"pages", "date"} исключает из ответа данные аргументы
    response_model_include={"title", "writer"} в ответ будут включены ТОЛЬКО эти аргументы
    """
    return book
    #     {
    #     'book': book,  # заполняем инфу по Book
    #     'author': author,  # заполняем инфу по Author
    #     'amount': amount,  # аргумент входит в тело запроса, и не учитывается в url
    # }


@app.get('/book/')
def get_book(q: str = Query(None, min_length=2, max_length=5, description='Search book', deprecated=True)):
    """
    Query позволяет поставить ограничения ввода. Установлено ограничение от 2 до 5 символов.
    description позволяет задать описание этой q.
    Query(...): три точки указывают на то, что параметр обязательный.
    Query('test') указывает значение по умолчанию.
    List[str] = Query можно использовать для передачи списка параметров
    Query(['asd'],['qwe']) установить список по умолчанию
    depricated = True устанавливает в документации параметр "устаревший"
    """
    return q


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=1, le=500)):
    """
    gt=1 минмальное значение
    le=20 максимальное значение
    Разница:
    Query = ?pages=20
    Path = /book/5
    """
    return {'pk': pk, "pages": pages}
