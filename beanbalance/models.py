from django.db import models

# Create your models here.
class Balance(models.Model):
    bob = models.DecimalField(max_digits=6, decimal_places=2, default = 0.00)
    jeremy = models.DecimalField(max_digits=6, decimal_places=2, default = 0.00)
    coworker1 = models.DecimalField(max_digits=6, decimal_places=2, default = 0.00)
    coworker2 = models.DecimalField(max_digits=6, decimal_places=2, default = 0.00)
    coworker3 = models.DecimalField(max_digits=6, decimal_places=2, default = 0.00)
    coworker4 = models.DecimalField(max_digits=6, decimal_places=2, default = 0.00)
    coworker5 = models.DecimalField(max_digits=6, decimal_places=2, default = 0.00)
    def __str__(self):
        return f"Entry(id={self.id})"