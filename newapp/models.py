from django.contrib.auth.models import AbstractUser
from django.contrib.gis import forms
from django.db import models

# Create your models here.
class work(models.Model):
    works=models.CharField(max_length=100)

    def __str__(self):
        return self.works
class Login(AbstractUser):

    is_worker = models.BooleanField(default=False)
    is_customer =models.BooleanField(default=False)


class regist(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    phone=models.CharField(max_length=100, required=True)
    email=models.CharField(max_length=100)





    def __str__(self):
        return self.Name


class workerregist(models.Model):
    user = models.OneToOneField(Login,on_delete=models.CASCADE,)
    WorkerName = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    work = models.ForeignKey(work, on_delete=models.DO_NOTHING)
    profile = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.WorkerName

class Schedule(models.Model):


    workers = models.ForeignKey(workerregist,on_delete=models.DO_NOTHING)
    Work = models.ForeignKey(work,on_delete=models.DO_NOTHING,null=True,blank=True)
    date = models.DateField(max_length=100)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)

class Feedback(models.Model):
    customer = models.ForeignKey(regist,on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=100)
    replay = models.CharField(max_length=100,null=True,blank=True)

class Notification(models.Model):
    date = models.DateField(max_length=100,auto_now=True)
    notification = models.TextField(max_length=100)

class Appointment(models.Model):

    user = models.ForeignKey(regist,on_delete=models.DO_NOTHING)
    schedule = models.ForeignKey(Schedule,on_delete=models.DO_NOTHING)
    status = models.IntegerField(default=0)

class Bill(models.Model):
    name = models.ForeignKey(regist,on_delete=models.DO_NOTHING)
    bill_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(max_length=30)
    paid_on = models.DateField(max_length=100,auto_now=True)
    status = models.IntegerField(default=0)

class Creditcard(models.Model):
    card_no = models.IntegerField(max_length=30)
    card_cvv = models.IntegerField(max_length=30)
    expiry_date = models.CharField(max_length=200)
