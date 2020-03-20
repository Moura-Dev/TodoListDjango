from typing import List, Any

from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('deletecompleted', views.deleteCompleted, name='deletecompleted'),
    path('deleteAll', views.deleteAll, name='deleteall'),
]
