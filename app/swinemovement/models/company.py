from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30, db_index=True, unique=True)
