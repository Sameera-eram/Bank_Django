from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class AccType(models.Model):
    name = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class Data(models.Model):
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=10)
    aadhar = models.CharField(max_length=12)
    dob = models.DateField()
    address = models.TextField()
    acc_no = models.CharField(max_length=20, default="1200")
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    pin = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=500)
    account_type = models.ForeignKey(AccType, on_delete=models.CASCADE)

