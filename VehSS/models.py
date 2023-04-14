from django.db import models

# Create your models here.
class Owner(models.Model):

    name = models.CharField(max_length=120,null=True)
    email=models.EmailField(max_length=120,null=True)
    # email=models.EmailField(max_length=120,null=True)
    location = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[('Vadodara','Vadodara'),('Anand','Anand'),('Nadiad','Nadiad')]
        )
    carname = models.CharField(max_length=120,null=True)
    seats = models.IntegerField(null=True)
    # trav=models.ForeignKey(Traveller,blank=True,null=False,on_delete=models.CASCADE)
    phone = models.CharField(max_length=120,null=True)
    date_time = models.DateTimeField(null=True)
    # attendees = models.ManyToManyField(Traveller,blank=True,null=False)
    image = models.ImageField(upload_to='Hello/static/image')

    def __str__(self):
        return self.name
    
class Traveller(models.Model):
    name = models.CharField(max_length=120,null=True)
    email=models.EmailField(max_length=120,null=True)
    location = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[('Vadodara','Vadodara'),('Anand','Anand'),('Nadiad','Nadiad')]
        )
    phone = models.CharField(max_length=120,null=True)
    date_time = models.DateTimeField(null=True)

class Summary(models.Model):
    traveller_name = models.CharField(max_length=120,null=True)
    owner_name = models.CharField(max_length=120,null=True)
    email=models.EmailField(max_length=120,null=True)
    location = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[('Vadodara','Vadodara'),('Anand','Anand'),('Nadiad','Nadiad')]
        )
    phone = models.CharField(max_length=120,null=True)
    date_time = models.CharField(max_length=120,null=True)
    image = models.ImageField(upload_to='Hello/static/image')

