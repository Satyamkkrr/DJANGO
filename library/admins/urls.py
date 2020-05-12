from django.urls import path
from . import views
app_name = 'admins'
urlpatterns=[
        path('', views.index, name='index'),
        path('login/', views.login, name='login'),
        path('profile/', views.profile, name='profile'),
        path('logout/', views.logout, name='logout'),
        path('add_librarian/', views.add_librarian, name='add_librarian'),
]
