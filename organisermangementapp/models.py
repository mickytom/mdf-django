from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Blogposter(models.Model):
    heading = models.CharField(max_length=500)
    category = models.ForeignKey(Activity, on_delete=models.CASCADE, max_length=50,null=True, blank=True)
    back_ground_img = models.ImageField(upload_to="images", null=True,blank=True)
    back_ground_img_title = models.CharField(max_length=1000, null=True, blank=True)
    writer_name = models.CharField(max_length=1000,null=True, blank=True)
    cause_sub_heading = models.CharField(max_length=1000, null=True, blank=True)
    cause_sub_heading_img = models.ImageField(upload_to="images", null=True, blank=True)
    cause_sub_heading_img_title = models.CharField(max_length=1000, null=True, blank=True)
    article = models.TextField(max_length=5000, null=True, blank=True)
    youtube_link = models.CharField(max_length=1000, null=True, blank=True)
    images1 = models.ImageField(upload_to="images", null=True, blank=True)
    images2 = models.ImageField(upload_to="images", null=True, blank=True)
    images3 = models.ImageField(upload_to="images", null=True, blank=True)
    images4 = models.ImageField(upload_to="images", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.writer_name
    @property
    def imageURL(self):
        try:
            url =self.back_ground_img.url
        except:
            url =""
        return url

    @property
    def image1(self):
        try:
            url = self.images1.url
        except:
            url = ""
        return url

    @property
    def image2(self):
        try:
            url = self.images2.url
        except:
            url = ""
        return url
    @property
    def image3(self):
        try:
            url = self.images3.url
        except:
            url = ""
        return url
    @property
    def image4(self):
        try:
            url = self.images4.url
        except:
            url = ""
        return url


