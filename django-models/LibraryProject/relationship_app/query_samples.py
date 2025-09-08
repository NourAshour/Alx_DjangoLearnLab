from models import Book, Library, Librarian
books = Book.objects.filter(author = 'author1')

books = Library.objects.get(name=library_name)
books.all()

lib1_librarian = Librarian.objects.filter(library = 'lib1')