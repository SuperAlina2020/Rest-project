from django.db import models

class Purchase(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
