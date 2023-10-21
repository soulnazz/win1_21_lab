from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_view),
    path('book_detail/<int:id>/', views.book_detail_view),
    path('add-comment/',views.createBookView),
    path('delete_book/', views.book_delete_view),
    path('delete_book/<int:id>/delete/', views.book_drop_view),
    path('create_book/', views.createBookPostView),

]