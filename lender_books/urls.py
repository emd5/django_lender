from django.urls import path
from .views import books_detail_view, books_list_view

urlpatterns = [
    path('', books_list_view, name='books_list'),
    path('<int:pk>', books_detail_view, name='books_detail')
]
