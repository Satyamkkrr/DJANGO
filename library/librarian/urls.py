from django.urls import path
from . import views
app_name = 'librarian'

urlpatterns=[
        path('login/', views.login, name='login'),
        path('profile/', views.profile, name='profile'),
        path('logout/', views.logout, name='logout'),
        path('notifications/', views.notifications, name='notifications'),
        path('remove_request/<pk>/', views.RequestBookDeleteView.as_view(), name='requestdelete'),
        path('student_list/', views.StudentList.as_view(), name='student_list'),
        path('student_detail/<pk>', views.StudentDetail.as_view(), name='student_detail'),
        path('student_transaction/<pk>', views.StudentCurrentTransaction, name='student_transaction'),
        path('student_previous_transaction/<pk>', views.StudentPreviousTransaction, name='student_previous_transaction'),
        path('return_book/<pk1>/<pk2>', views.ReturnBook, name='return_book'),
        path('export/', views.export_xls, name='export'),
        #path('add_books/', views.add_books, name='add_books'),
]
