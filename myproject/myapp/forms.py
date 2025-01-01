from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta: #Configuration settings of the model(configuration settings bannale db ma kun kun field baschha kun model sanga tied hunchha bhanne kura ho !)
        model = Book
        fields = ['title', 'author', 'published_date','price','id','genre']

    def clean_genre(self):
        genres = self.cleaned_data['genre']

        if isinstance(genres,str):
            return [genre.strip() for genre in genres.split(",") if genre.strip()]