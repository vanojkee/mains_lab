from django.db.models import Count, Sum
from rest_framework import generics

from .serializers import *
from .utils import save_clients, save_bills


class ClientsUploadAPIView(generics.CreateAPIView):
    """Upload Clients excel file"""
    queryset = ClientsUpload.objects.all()
    serializer_class = ClientsUploadSerializer

    def post(self, request, *args, **kwargs):
        create = self.create(request, *args, **kwargs)
        save_clients(create.data['file'][22:])
        return create


class BillsUploadAPIView(generics.CreateAPIView):
    """Upload Bills excel file"""
    queryset = BillsUpload.objects.all()
    serializer_class = BillsUploadSerializer

    def post(self, request, *args, **kwargs):
        create = self.create(request, *args, **kwargs)
        save_bills(create.data['file'][22:])
        return create


class ClientsListAPIView(generics.ListAPIView):
    serializer_class = ClientsSerializer

    def get_queryset(self):
        queryset = Clients.objects.annotate(
            orgs_count=Count('organization', distinct=True)
        ).annotate(
            income=Sum('organization__bills__bills_sum')
        )

        return queryset.values('name', 'orgs_count', 'income')


class BillsListAPIView(generics.ListAPIView):
    serializer_class = BillsSerializer

    def get_queryset(self):
        queryset = Bills.objects.all()

        client_id = self.request.query_params.get('client_name_id')
        if client_id is not None:
            queryset = queryset.filter(client_name=client_id)

        organization_id = self.request.query_params.get('client_org_id')
        if organization_id is not None:
            queryset = queryset.filter(client_org=organization_id)

        return queryset
