from django.urls import path
from .views import (ListStatusesView,
                    CreateStatusView,
                    UpdateStatusView,
                    DeleteStatusView)

urlpatterns = [
    path('', ListStatusesView.as_view(), name='statuses'),
    path('create/', CreateStatusView.as_view(), name='create_status'),
    path('<int:pk>/update/', UpdateStatusView.as_view(), name='update_status'),
    path('<int:pk>/delete/', DeleteStatusView.as_view(), name='delete_status')
]