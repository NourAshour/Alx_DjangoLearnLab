from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('list_books/', list_books),
    path('libraries/', LibraryDetailView.as_view())
]