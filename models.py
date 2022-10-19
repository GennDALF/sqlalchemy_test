from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


# класс, от которого будут наследоваться модели
Base = declarative_base()


# модель таблицы связей таблиц author и publisher
author_publisher = Table(
    'author_publisher',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('author.author_id')),
    Column('publisher_id', Integer, ForeignKey('publisher.publisher_id'))
)
# модель таблицы связей таблиц book и publisher
book_publisher = Table(
    'book_publisher',
    Base.metadata,
    Column('book_id', Integer, ForeignKey('book.book_id')),
    Column('publisher_id', Integer, ForeignKey('publisher.publisher_id'))
)


# модель класса для автора
class Author(Base):
    __tablename__ = 'author'
    author_id = Column('author_id', Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    # books = relationship('Book', backref=backref('author'))
    # publishers = relationship('Publisher', secondary=author_publisher, back_populates='authors')

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'


# модель класса для книги
class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('author.author_id'))
    title = Column(String)
    # publishers = relationship('Publisher', secondary=book_publisher, back_populates='books')

    def __repr__(self):
        return f'{self.title}'


# модель класса для издательства
class Publisher(Base):
    __tablename__ = 'publisher'
    publisher_id = Column(Integer, primary_key=True)
    name = Column(String)
    # authors = relationship('Author', secondary=author_publisher, back_populates='publishers')
    # books = relationship('Book', secondary=book_publisher, back_populates='publishers')

    def __repr__(self):
        return f'{self.name}'


if __name__ == '__main__':
    print(author_publisher.columns, sep='\n', end='\n'*2)
    print(book_publisher.columns, sep='\n', end='\n'*2)