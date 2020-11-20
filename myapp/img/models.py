from django.db import models

# Create your models here.
class Img(models.Model):
    image = models.ImageField(upload_to='user-posts/', blank=False)
    caption = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)