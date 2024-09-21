from django.urls import path
from .views import (ListTasksView,
                    CreateTaskView,
                    UpdateTaskView,
                    DeleteTaskView,
                    TaskView)


urlpatterns = [
    path('', ListTasksView.as_view(), name='tasks'),
    path('<int:pk>/', TaskView.as_view(), name='view_task'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
]
