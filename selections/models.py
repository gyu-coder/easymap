from django.db import models

# Create your models here.

class Theme(models.Model):
    
    bft = models.CharField(max_length=264)
    act1 = models.CharField(max_length=264)
    act2 = models.CharField(max_length=264)
    lun = models.CharField(max_length=264)
    act3 = models.CharField(max_length=264)
    act4 = models.CharField(max_length=264)
    din = models.CharField(max_length=264)
    
    def __str__(self):
        return f'{self.bft}: {self.din}'