In [20]: book1.delete()
Out[20]: (1, {'bookshelf.Book': 1})

In [22]: books = Book.objects.all()

In [23]: for book in books:
    ...:     print(book.title)
    ...:
