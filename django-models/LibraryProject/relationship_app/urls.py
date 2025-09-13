from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.BookView),
    path('libraries/', views.LibraryDetail.as_view())
]