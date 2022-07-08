from rest_framework import serializers

from .models import *


class ClientsUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsUpload
        fields = '__all__'


class BillsUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillsUpload
        fields = '__all__'


class ClientsSerializer(serializers.Serializer):
    name = serializers.CharField()
    orgs_count = serializers.IntegerField()
    income = serializers.DecimalField(
        max_digits=9,
        decimal_places=2,
    )


class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'
