from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
