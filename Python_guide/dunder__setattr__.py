class Book:

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year  = year

    def __setattr__(self, key, value):
        if key == 'title' and type(value) == str:
            object.__setattr__(self, key, value)
        elif key == 'title' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")

        if key == 'author' and type(value) == str:
            object.__setattr__(self, key, value)
        elif key == 'author' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")

        if key == 'pages' and type(value) == int:
            object.__setattr__(self, key, value)
        elif key == 'pages' and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")

        if key == 'year' and type(value) == int:
            object.__setattr__(self, key, value)
        elif key == 'year' and type(value) != int:
            raise TypeError("Неверный тип присваиваемых данных.")

book = Book(title='Python ООП', author='Сергей Балакирев', pages=123, year=2022)
print(book.__dict__)
