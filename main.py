from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Author, Book, Publisher

from pathlib import Path
from sys import path

from pprint import pprint

db_path = Path(path[0]) / 'author_book_publisher.db'


def main():
    """Основная точка входа программы."""


if __name__ == '__main__':
    # подключение к sqlite базе данных через SQLAlchemy
    engine = create_engine(f"sqlite:///{db_path}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # формирование запроса и транзакции
    authors = session.query(Author)
    print(authors)
    # отправка транзакции и получение ответа
    print(authors.all(), end='\n'*2)

    books = session.query(Book)
    print(books)
    pprint(books.order_by(Book.title).all())
    print()

    publishers = session.query(Publisher)
    print(publishers)
    pprint(publishers.all())
