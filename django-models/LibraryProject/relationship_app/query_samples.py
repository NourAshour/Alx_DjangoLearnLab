from models import Book, Author, Library, Librarian
author = Author.objects.get(name='author_name')
books = Book.objects.filter(author=author)

library = Library.objects.get(name='library_name')
books.all()

lib1_librarian = Librarian.objects.get(library='lib1')