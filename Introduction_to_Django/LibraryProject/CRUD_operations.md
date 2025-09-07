In [12]: book1 = Book(title = '1984', author = 'George Orwell', publication_yea
       ⋮ r = 1949)

In [13]: book1.save()

In [14]: print(book1.title)
1984

In [15]: books = Book.objects.all()

In [16]: for book in books:
    ...:     print(book.title)
    ...:
1984

In [17]: book1.title = 'Nineteen Eighty-Four'

In [18]: book1.save()

In [19]: print(book1.title)
Nineteen Eighty-Four

In [20]: book1.delete()
Out[20]: (1, {'bookshelf.Book': 1})

In [22]: books = Book.objects.all()

In [23]: for book in books:
    ...:     print(book.title)
    ...:
