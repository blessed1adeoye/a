from django.db import models

class HomE(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    me = models.TextField()

    def __str__(self):
         return self.first_name
    

class About(models.Model):
    cv = models.FileField( upload_to='media/pdf')
    fb_URL = models.URLField('FACEBOOK URL', blank=True, null=True)
    tw_URL = models.URLField('TWITTER URL', blank=True, null=True)
    lk_URL = models.URLField('LINKEDIN URL', blank=True, null=True)
    insta_URL = models.URLField('INSTAGRAM URL', blank=True, null=True)
    whatapp_url  = models.URLField('WHATSAPP URL', blank=True, null=True)
    
    

class Education(models.Model):
     span = models.CharField('Year', max_length=10)
     h3 = models.CharField( 'Certificate', max_length=100)
     para = models.TextField()
     school = models.TextField(blank=True, null=True )

     def __str__(self):
          return self.h3
     
class Portfolio(models.Model):
     name = models.CharField(max_length=50)
     pic = models.ImageField(upload_to='Galary')

     def __str__(self):
          return self.name
     
class Carousel(models.Model):
     name = models.CharField(max_length=10, blank=True, null=True)
     pic = models.ImageField(upload_to='Carousel')
     date = models.DateTimeField(auto_now_add=True)

     def __str__(self) -> str:
          return self.name
     

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




     