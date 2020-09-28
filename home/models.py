from django.db import models

# Create your models here.
#Database---> Excel work
#table ---> sheet
# Model In django--->Table ---> sheet
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=255)
    email = models.CharField("Name", max_length=100)
    phone = models.CharField("Phone", max_length=13)
    content = models.TextField("Content")
    times = models.DateTimeField(auto_now_add=True ,blank=True)


    def __str__(self):
        return 'Message From   ' + self.name + ' -->  ' + self.email


