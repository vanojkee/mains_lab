from django.urls import path
from .views import *

urlpatterns = [
    path('clients-upload/', ClientsUploadAPIView.as_view(), name='client-upload'),
    path('bills-upload/', BillsUploadAPIView.as_view(), name='bills-upload'),
    path('clientslist/', ClientsListAPIView.as_view(), name='clientslist'),
    path('billslist/', BillsListAPIView.as_view(), name='billslist')
]
