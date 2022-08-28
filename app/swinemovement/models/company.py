from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

