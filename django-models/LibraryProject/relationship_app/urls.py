from django.urls import path
from .views import list_books, LibraryDetailView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('list_books/', list_books),
    path('libraries/', LibraryDetailView.as_view(), name = 'libraries'),
    path('register/', SignUpView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(template_name = 'relationship_app/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout')
]