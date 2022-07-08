from django.db import models
from mains_lab.settings import MEDIA_ROOT


class ClientsUpload(models.Model):
    file = models.FileField(upload_to=MEDIA_ROOT, blank=False, null=False)

    def __str__(self):
        return self.file


class BillsUpload(models.Model):
    file = models.FileField(upload_to=MEDIA_ROOT, blank=True, null=False)

    def __str__(self):
        return self.file


class Clients(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    client_name = models.CharField(max_length=100, unique=False, db_index=False)
    name = models.CharField(max_length=100, unique=False, db_index=False)
    address = models.CharField(max_length=255)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['client_name', 'name']]

    def __str__(self):
        return self.name


class Bills(models.Model):
    client_name = models.ForeignKey(Clients, on_delete=models.CASCADE)
    client_org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    number = models.IntegerField()
    date = models.DateTimeField()
    service = models.CharField(max_length=255, unique=False)
    bills_sum = models.DecimalField(
        max_digits=9,
        decimal_places=2,
    )

    class Meta:
        unique_together = [['client_org', 'number']]

    def __str__(self) -> str:
        return f'{self.client_name} - {self.client_org} № {self.number} - {self.bills_sum}'
