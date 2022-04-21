from django.db import models
from django.db import connections
# Create your models here.
class Newuser(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password1=models.CharField(max_length=150)

class Newhuser(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password1=models.CharField(max_length=150)

class Meet(models.Model):
    meet_name=models.CharField(max_length=150)
    timedate=models.DateTimeField('date')
    meet_code=models.CharField(max_length=150)
    class Meta:
        db_table="loginsys_meet"

class Meetreg(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    contact_number=models.BigIntegerField()
    college_name=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    meet_code=models.CharField(max_length=150)
    class Meta:
        db_table="loginsys_meetreg"

class chkbox(models.Model):
    meet_code=models.CharField(max_length=150)
    class Meta:
        db_table="loginsys_chkbox"
    def __str__(self):
        return self.meet_code

class check(models.Model):
   username=models.CharField(max_length=150)
   class Meta:
        db_table="loginsys_check"

class Query(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    message=models.CharField(max_length=150)



 

