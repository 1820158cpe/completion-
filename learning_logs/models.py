from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True, auto_now = False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, )

    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_added =  models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text
        

    
    