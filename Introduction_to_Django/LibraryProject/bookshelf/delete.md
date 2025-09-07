In[18]: from bookshelf.models import Book

In[19]: book = Book.objects.get(title = 'Nineten Eighty-Four')

In [20]: book.delete()
Out[20]: (1, {'bookshelf.Book': 1})

In [22]: books = Book.objects.all()

In [23]: for book in books:
    ...:     print(book.title)
    ...:
