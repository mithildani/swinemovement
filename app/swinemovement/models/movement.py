from django.db import models

from swinemovement.models.company import Company
from swinemovement.models.premise import Premise
from swinemovement.models.species import Species


class Movement(models.Model):
    origin_premise = models.ForeignKey(
        Premise,
        related_name='origin_movement',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    destination_premise = models.ForeignKey(
        Premise,
        related_name='destination_movement',
        on_delete=models.CASCADE
    )

    species = models.ForeignKey(Species, related_name='movement', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='movement', on_delete=models.CASCADE)

    reason = models.TextField(null=True, blank=True)
    items_moved = models.IntegerField(db_index=True)
    shipment_start_date = models.DateField(db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
