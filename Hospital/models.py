from django.db import models

# Create your models here.
class Doctor(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    contact = models.IntegerField()
    specilization = models.CharField(max_length=50)

    def __str__(self):
        return self.First_name+" "+self.Last_name

class Patient(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField()
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.First_name+" "+self.Last_name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.doctor.First_name+" "+self.doctor.Last_name+"--"+self.patient.First_name+" "+self.patient.Last_name
    
class contact(models.Model):
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=80)
    message = models.CharField(max_length=1000)
    
