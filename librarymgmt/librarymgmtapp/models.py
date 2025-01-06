from django.db import models

class Book(models.Model):
    CHOICES = [
        ("available", "Available"),
        ("unavailable", "Unavailable"),
        ("borrowed", "Borrowed"),
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
    count = models.IntegerField()
    status = models.CharField(max_length=100,choices=CHOICES)

    def __str__(self):
        return self.title
    
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True) 
    member_id = models.IntegerField(primary_key=True)
    borrowed_books = models.ManyToManyField(Book,blank=True,related_name="borrowers")#related_name makes it possible to usie query from either model, the User model or the Book model.

class Transcation(models.Model):
    STATUS = [
        ("returned","Returned"),
        ("not returned","Not Returned")
    ]
    book = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    borrowed_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=100)
    transcation_id = models.CharField(max_length=6,primary_key=True)

    def __str__(self):
        return self.transaction_id