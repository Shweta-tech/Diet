from django.db import models

# Create your models here.
class image_up(models.Model):
    # diet=models.OneToOneField(dietrecallmodel, on_delete=models.CASCADE)
    title=models.CharField( max_length=150,null=True)
    image = models.ImageField( upload_to='images/%Y/%m/%d')

class Document(models.Model):
    title=models.CharField( max_length=150,null=True)
    Document = models.FileField(upload_to='documents/%Y/%m/%d')