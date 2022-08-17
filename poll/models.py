from turtle import position
from django.db import models

# Create your models here.
class Poll(models.Model):
    poll_id = models.IntegerField(primary_key=True)
    post = (
        ('President','President'),
        ('Vice President','Vice President'),
        ('Ladies Wing President','Ladies Wing President'),
        ('General Secretary','General Secretary'),
        ('Financial Secretary','Financial Secretary'),
        ('Organizing Secretary','Organizing Secretary')
    )
    Quest = models.CharField(max_length=250)
    position = models.CharField(choices=post,max_length=200)
    Name_1=models.CharField(max_length=100,blank=True,null=True)
    Name_2=models.CharField(max_length=100,blank=True,null=True)
    image_1=models.ImageField(upload_to='media',null=True, blank=True)
    image_2=models.ImageField(upload_to='media',null=True, blank=True)
    count_1=models.IntegerField(default=0)
    count_2=models.IntegerField(default=0)
    date_created=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']
        
    def total(self):
        return self.count_2  + self.count_1

    def winner(self):
        if self.count_1 < self.count_2:
            return self.Name_2
        elif self.count_1 > self.count_2:
            return self.Name_1 