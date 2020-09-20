from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('todos/completed/', views.TodoCompletedList.as_view()),
]