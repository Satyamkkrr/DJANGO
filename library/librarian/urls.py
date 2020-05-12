from django.urls import path
from . import views
app_name = 'librarian'

urlpatterns=[
        path('login/', views.login, name='login'),
        path('profile/', views.profile, name='profile'),
        path('logout/', views.logout, name='logout'),
        #path('add_books/', views.add_books, name='add_books'),
]
