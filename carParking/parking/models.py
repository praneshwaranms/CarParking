from django.db import models

# Create your models here.
class slots_availability(models.Model):
    slots = models.CharField(max_length = 50,default = "0")


class slots_booking(models.Model):
    slot = models.CharField(max_length = 50 ,default = '-')
    email = models.CharField(max_length = 50,default = '-')
    name =  models.CharField(max_length = 50,default = '-')
    phone_number = models.CharField(max_length = 50 ,default = '-')
    date =  models.CharField(max_length = 50,default = '-')
    fromTime =  models.CharField(max_length = 50,default = '-')
    toTime =  models.CharField(max_length = 50,default = '-')
    duration =  models.CharField(max_length = 50,default = '-')
    licensePlateNo =  models.CharField(max_length = 50,default = '-')
    vehicleModel = models.CharField(max_length = 50 ,default = '-')
    staus = models.IntegerField(default = 0)
    otp = models.CharField(max_length = 50,default = '-')


class LandInformation(models.Model):
    name = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=12, null=True, blank=True)
    document_input = models.FileField(upload_to='documents/')
    latitude = models.FloatField()
    longitude = models.FloatField()
    landmark_name = models.CharField(max_length=100)
    exact_location = models.TextField()


class login_details(models.Model):
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length =50)