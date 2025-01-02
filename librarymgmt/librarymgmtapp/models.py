from django.db import models


        
    
class Book(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("unavailable", "Unavailable"),
        ("borrowed", "Borrowed"),
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
    count = models.IntegerField()
    status = models.CharField(max_length=100,choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
    
