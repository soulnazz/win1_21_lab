from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookView.as_view()),
    path('book_detail/<int:id>/', views.BookDetailView.as_view()),
    path('book_list/<int:id>/delete/', views.BookDropView.as_view()),
    path('book_list/<int:id>/update/', views.UpdateBookPostView.as_view()),
    path('create_post_book/', views.CreateBookPostView.as_view()),
    path('add-comment/', views.createBookView),
    path('seacrh/', views.SearchView.as_view(), name='search')

]