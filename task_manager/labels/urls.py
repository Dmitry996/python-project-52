from django.urls import path
from .views import (ListLabelsView,
                    CreateLabelView,
                    UpdateLabelView,
                    DeleteLabelView)


urlpatterns = [
    path('', ListLabelsView.as_view(), name='labels'),
    path('create/', CreateLabelView.as_view(), name='create_label'),
    path('<int:pk>/update/', UpdateLabelView.as_view(), name='update_label'),
    path('<int:pk>/delete/', DeleteLabelView.as_view(), name='delete_label'),
]
