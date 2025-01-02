from django.db import models
from django.core.exceptions import ValidationError

def validate_status(value):
    if value  in ("available","unavailable","borrowed"):
        return value
    
    raise ValidationError("The status should be one of ['available','unavailable','borrowed']")
        
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
    count = models.IntegerField()
    status = models.CharField(max_length=100,validators=validate_status)

    def __str__(self):
        return self.title
    
