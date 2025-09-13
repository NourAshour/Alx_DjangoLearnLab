from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookView),
    path('libraries/', views.LibraryDetail.as_view())
]