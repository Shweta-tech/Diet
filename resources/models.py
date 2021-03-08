from django.db import models

# Create your models here.


class image_up(models.Model):
    # diet=models.OneToOneField(dietrecallmodel, on_delete=models.CASCADE)
    title=models.CharField( max_length=150,null=True)
    image = models.ImageField( upload_to='images/%Y/%m/%d')

class Document(models.Model):
    title=models.CharField( max_length=150,null=True)
    Document = models.FileField(upload_to='documents/%Y/%m/%d')

    
    #  School Resources
class document_sch(models.Model):
    title=models.CharField( max_length=150,null=True)
    document = models.FileField(upload_to='document_school/%Y/%m/%d',default=False)

class image_up_sch(models.Model):
    # diet=models.OneToOneField(dietrecallmodel, on_delete=models.CASCADE)
    title=models.CharField( max_length=150,null=True)
    image = models.ImageField( upload_to='image_school/%Y/%m/%d',default=False)

class video_sch(models.Model):
    title=models.CharField( max_length=150,null=True)
    video = models.FileField(upload_to='video_school/%Y/%m/%d',default=False)



#  Nutri-Garden Resource
class document_nutri(models.Model):
    title=models.CharField( max_length=150,null=True)
    document = models.FileField(upload_to='document_nutri/%Y/%m/%d',default=False)
class image_up_nutri(models.Model):
    # diet=models.OneToOneField(dietrecallmodel, on_delete=models.CASCADE)
    title=models.CharField( max_length=150,null=True)
    image = models.ImageField( upload_to='image_nutri/%Y/%m/%d',default=False)

class video_nutri(models.Model):
    title=models.CharField( max_length=150,null=True)
    video = models.FileField(upload_to='video_nutri/%Y/%m/%d',default=False)




#  ICDS Reources
class document_icds(models.Model):
    title=models.CharField( max_length=150,null=True)
    document = models.FileField(upload_to='document_icds/%Y/%m/%d',default=False)

class image_up_icds(models.Model):
    # diet=models.OneToOneField(dietrecallmodel, on_delete=models.CASCADE)
    title=models.CharField( max_length=150,null=True)
    image = models.ImageField( upload_to='image_icds/%Y/%m/%d',default=False)

class video_icds(models.Model):
    title=models.CharField( max_length=150,null=True)
    video = models.FileField(upload_to='video_icds/%Y/%m/%d',default=False)