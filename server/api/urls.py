from django.urls import include, path
from server.api import views

urlpatterns = [
    path('transactions/', views.get_transactions, name='transactions'),
]
