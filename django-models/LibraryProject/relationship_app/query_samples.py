from models import Book, Library, Librarian
books = Book.objects.filter(author = 'author1')
lib1_books = Library.objects.filter(name = 'lib1')
lib1_librarian = Librarian.objects.filter(library = 'lib1')