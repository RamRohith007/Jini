from django.db import models

# Create your models here.
class PicStock(models.Model):
    owner = models.CharField(max_length=150)
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='picstock/')
    uploaded_datetime = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['uploaded_datetime']

    def __str__(self):
        return f"{self.name} - Uploaded by {self.owner}"
    

    