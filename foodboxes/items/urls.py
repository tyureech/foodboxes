from django.urls import path
from items.views import function_based

urlpatterns = [
    path('items/<int:id>/', function_based, name='function-based'),
]
