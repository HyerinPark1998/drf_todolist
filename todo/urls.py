from django.urls import path
from todo import views

urlpatterns = [
    path('', views.ToDoListView.as_view(),name='todolist_view'),
    path('<int:todo_id>/',views.ToDoDetailView.as_view(),name='todoedtail_view'),
]