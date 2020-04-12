from django.db import models

# Create your models here.
from django.db import models
import jwt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import (AbstractUser,AbstractBaseUser, BaseUserManager, PermissionsMixin)
fs = FileSystemStorage(location='/files')

class UserManager(BaseUserManager):
    def create_user(self, email, password="password"):
            #raise ValueError("ENTER AN EMAIL BUDDY")
        #if not username:
        #    raise ValueError("I KNOW YOU HAVE A NAME")
            #raise ValueError("PASSWORD?!?!?!? HELLO??")
        print(self.model)
        user = self.model(
             email = self.normalize_email(email)
             )
        user.save()
        if password:
            user.set_password(password)
        else:
            encoded = jwt.encode({'email':user.email}, 'secret', algorithm='HS256')
            user.set_password(encoded)

        return user
    def create_superuser(self, password, email):
        user=self.create_user(email, password)
        user.is_staff=True
        user.is_superuser = True
        user.save()
        return user



class User(AbstractUser):
    email=models.CharField(unique=True, max_length=256)
    username=models.CharField(max_length=256, blank=True)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email

class Package(models.Model):
    id=models.CharField(primary_key=True, max_length=256)
    name=models.CharField(max_length=256)
    price=models.IntegerField()
    icon=models.ImageField(blank=True)
    description=models.CharField(max_length=256)

class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    package=models.ForeignKey(Package, on_delete=models.CASCADE,blank=True)
    date=models.DateField(auto_now=True)
    is_recieved=models.BooleanField(default=False)
    is_downloaded=models.BooleanField(default=False)
    is_proccessed=models.BooleanField(default=False)
    is_being_printed=models.BooleanField(default=False)
    is_printed=models.BooleanField(default=False)
    is_sent=models.BooleanField(default=False)
    file_3d_printing=models.FileField(upload_to='files/raw_data/')


class Address(models.Model):
    user=models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    ZIPcode=models.IntegerField()
    city=models.CharField(max_length=256, default="")
    address_line1=models.CharField(max_length=256)
    address_line2=models.CharField(max_length=256)
    country=models.CharField(max_length=256)
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)

class Receipt(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    recepit_file=models.FileField(upload_to='files/recepits/')
