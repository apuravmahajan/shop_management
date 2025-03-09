from django.urls import path

from .views import update, display, delete

urlpatterns = [
    path('update/', update, name='update'),
    path('display/', display, name='display'),
    path('delete/', delete, name='delete'),
]
