#from email import message
from django.db import models
from django.utils.html import mark_safe

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    photo = models.ImageField(null=True, blank=True, upload_to="images/")
    message = models.TextField()
    availability = models.TextField(default="", null=True, blank=True,)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)

    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.photo.url}" width = "300"/>')

    def __str__(self):
        return self.email
