from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(
        self,
        floor,
        password, 
        **extra_fields
    ):
        if not floor:
            raise ValueError("CHECK FLOOR")
        
        user = self.model(floor=floor, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
     
        return user
    
    def create_superuser(
        self,
        floor,
        password
    ):
        if not floor or not floor == '0000':
            raise ValueError('IVALID_FLOOR')
    
        user = self.create_user(floor=floor, password=password)
        user.is_superuser = True
        user.save(using=self.db)

class User(AbstractBaseUser, PermissionsMixin):
    floor    = models.CharField(max_length=4, null=True, unique=True)
    password = models.CharField(max_length=4, null=True)
    cost     = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    objects  = UserManager()
    
    USERNAME_FIELD = 'floor'
    
    class Meta:
        db_table = 'users'
        
class DoorLog(models.Model):
    open_date = models.DateTimeField()
    user      = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'door_logs'