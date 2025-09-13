from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from relationship_app.models import Book, Library

def BookView(request):
    books = Book.objects.all()
    context = {'books' : books}
    return render(request, 'list_books.html')

class LibraryDetail(DetailView):
    model = Library
    template_name = 'library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()  

