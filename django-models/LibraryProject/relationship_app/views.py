from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from relationship_app.models import Book, Library
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

def list_books(request):
    books = Book.objects.all()
    context = {'books' : books}
    return render(request, 'relationship_app/list_books.html')

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()  

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

