from django.db import models


class Laptop(models.Model):
    company = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    price = models.FloatField(null=True)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.company

    def __repr__(self):
        return f"<Animal #{self.pk} {self.company!r}>"
