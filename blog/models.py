from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
#Database---> Excel work
#table ---> sheet
# Model In django--->Table ---> sheet
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField("title", max_length=255)
    content = models.TextField("Content")
    auther = models.CharField("Author", max_length=30)
    slug = models.CharField( max_length=120)
    image = models.ImageField(default="")
    datetime =models.DateTimeField(blank=True)

    def __str__(self):
        return  self.title + " by author " + self.auther


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return  self.comment[0:13] + "..." +" by "+ self.user.username

