from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=8,decimal_places=5,help_text="Price of book in this format:123.45")#max_digits le overall kati ota digits hunchha tyo control garchha, decimal_places le chai decimal point pachi kati ota digit rakhne bhanne kura handle garcha 
    genre = models.CharField(null=False,blank=True,max_length=100)


    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    available_books = models.ManyToManyField(Book,related_name="libraries")

    def __str__(self):
        return self.name