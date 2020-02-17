from django.urls import path

from customers import views

app_name='customer_app'

urlpatterns=[
    path('create/',views.create,name='create'),
    path('list/',views.index,name='list'),
    path('edit/<str:pk>/',views.edit,name='edit'),#here i pass primary key
     path('delete/<str:pk>/',views.delete,name='delete'),
]