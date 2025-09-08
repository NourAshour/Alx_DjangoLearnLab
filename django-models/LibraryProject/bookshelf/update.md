In [16]: book = Book.objects.get(title = '1984')

In [17]: book.title = 'Nineteen Eighty-Four'

In [18]: book.save()

In [19]: print(book.title)
Nineteen Eighty-Four