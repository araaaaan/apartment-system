from django.db import models

class User_APT(models.Model):
    floor    = models.CharField(max_length=4, null=True)
    password = models.CharField(max_length=4, null=True)
    cost     = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    
    class Meta:
        db_table = 'users'