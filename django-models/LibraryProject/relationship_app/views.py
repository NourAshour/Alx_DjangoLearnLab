from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from relationship_app.models import Book, Library
from .models import Library

def list_books(request):
    books = Book.objects.all()
    context = {'books' : books}
    return render(request, 'relationship_app/list_books.html')

class LibraryDetail(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()  

