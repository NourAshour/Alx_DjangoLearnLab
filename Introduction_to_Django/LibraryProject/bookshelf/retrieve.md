In [15]: books = Book.objects.all()

In [16]: for book in books:
    ...:     print(book.title)
    ...:
1984
