from django.db import models


class Premise(models.Model):
    id = models.CharField(max_length=10, primary_key=True)

    name = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=30, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
