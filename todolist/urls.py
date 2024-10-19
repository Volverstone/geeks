
from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tasks/', views.TaskListAPIView.as_view()),
    path('api/v1/tasks/<int:id>/', views.TaskDetailAPIView.as_view()),
]