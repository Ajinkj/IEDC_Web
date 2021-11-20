from django.db import models

# Create your models here.
class iedcinfo(models.Model):
   

    IEDC_Title= models.CharField(max_length=100)
    IEDC_photo=models.ImageField(upload_to='images/info')
    IEDC_Short_Desc= models.TextField()
    IEDC_long_Desc= models.TextField()
    photos=models.ManyToManyField('all_photos', blank=True)

    
    # Photo_1=models.ImageField(upload_to='images/events', blank=True)
    # Photo_2=models.ImageField(upload_to='images/events',blank=True)
    # Photo_3=models.ImageField(upload_to='images/events',blank=True)
    # Photo_4=models.ImageField(upload_to='images/events',blank=True)
    # Photo_5=models.ImageField(upload_to='images/events',blank=True)
    # Photo_6=models.ImageField(upload_to='images/events',blank=True)
    # Photo_7=models.ImageField(upload_to='images/events',blank=True)
    # Photo_8=models.ImageField(upload_to='images/events',blank=True)
    # Photo_9=models.ImageField(upload_to='images/events',blank=True)
    # Photo_10=models.ImageField(upload_to='images/events',blank=True)
    # Photo_11=models.ImageField(upload_to='images/events',blank=True)
    # Photo_12=models.ImageField(upload_to='images/events',blank=True)
    


    def __str__(self):
        return self.IEDC_Title

class all_photos(models.Model):
    photo_name=models.CharField(max_length=100, )
    photo=models.ImageField(upload_to='images/events')
    photo_Desc= models.TextField(blank=True)

    def __str__(self):
        return self.photo_name





class milestone(models.Model):
    Title= models.CharField(max_length=100)
    Description= models.TextField()


    def __str__(self):
        return self.Title


class events(models.Model):
    Event_name= models.CharField(max_length=100)
    Event_photo= models.ImageField(upload_to='images/events')
    Event_short_Desc= models.TextField()
    Event_Description= models.TextField()
    Event_Register_Link=models.CharField(max_length=300, blank=True)
    Event_Home_visible=models.BooleanField(default=False)
    photos=models.ManyToManyField('all_photos', blank=True)
    # Photo_1=models.ImageField(upload_to='images/events', blank=True)
    # Photo_2=models.ImageField(upload_to='images/events',blank=True)
    # Photo_3=models.ImageField(upload_to='images/events',blank=True)
    # Photo_4=models.ImageField(upload_to='images/events',blank=True)
    # Photo_5=models.ImageField(upload_to='images/events',blank=True)
    # Photo_6=models.ImageField(upload_to='images/events',blank=True)
    # Photo_7=models.ImageField(upload_to='images/events',blank=True)
    # Photo_8=models.ImageField(upload_to='images/events',blank=True)
    # Photo_9=models.ImageField(upload_to='images/events',blank=True)
    # Photo_10=models.ImageField(upload_to='images/events',blank=True)
    # Photo_11=models.ImageField(upload_to='images/events',blank=True)
    # Photo_12=models.ImageField(upload_to='images/events',blank=True)


    def __str__(self):
        return self.Event_name

class form_msg(models.Model):
    name =models.CharField( max_length=200)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name



