from django.urls import path
from . import views
app_name = 'students'

urlpatterns=[
        path('register/', views.register, name='register'),
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),
        path('profile/', views.profile, name='profile'),
        path('issuebook/<pk1>/<pk2>/', views.IssueBook, name='issuebook'),
        path('view_book/', views.BookListView.as_view(), name='list'),
        path('view_issued_book/', views.IssuedBookListView.as_view(), name='booklist'),
        path('request_books/', views.book_request, name='request')
]
