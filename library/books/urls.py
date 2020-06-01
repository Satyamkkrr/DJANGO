from django.urls import path, re_path
from . import views
app_name = 'books'

urlpatterns=[
        path('add_book/', views.BookCreteView.as_view(), name='create'),
        path('view_book/', views.BookListView.as_view(), name='list'),
        re_path('modify_book/(?P<pk>\d+)/', views.BookUpdateView.as_view(), name='update'),
        re_path('remove_book/(?P<pk>\d+)/', views.BookDeleteView.as_view(), name='delete')
]
