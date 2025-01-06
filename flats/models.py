from django.db import models


# Create your models here.
class ResaleFlat(models.Model):
    month = models.CharField(max_length=20)
    town = models.CharField(max_length=100)
    flat_type = models.CharField(max_length=50)
    block = models.CharField(max_length=10)
    street_name = models.CharField(max_length=255)
    storey_range = models.CharField(max_length=50)
    floor_area_sqm = models.FloatField()
    flat_model = models.CharField(max_length=100)
    lease_commence_date = models.IntegerField()
    remaining_lease = models.IntegerField()
    resale_price = models.FloatField()

    class Meta:
        unique_together = (
            "month",
            "town",
            "flat_type",
            "block",
            "street_name",
            "resale_price",
        )

    def __str__(self):
        return f"{self.flat_type} at {self.street_name} ({self.town})"
