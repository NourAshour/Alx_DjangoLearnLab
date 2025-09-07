In [15]: book1 = Book.objects.get(title = '1984')

In [16]: print(book1.title)
1984

In [17]: print(book1.author)
George Orwell

In [18]: print(book1.publication_year)
1949
