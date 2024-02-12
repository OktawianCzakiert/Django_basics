from django.forms import ModelForm, CharField, TextInput, DateInput, DateField, Textarea
from .models import Tag, Author, Quote


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):

    fullname = CharField(min_length=3, max_length=255, required=True, widget=TextInput())
    born_date = DateField(widget=DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
        }
    ))
    born_location = CharField(min_length=3, max_length=500, widget=TextInput())
    description = CharField(min_length=3, max_length=5000, widget=Textarea())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):

    quote = CharField(min_length=3, max_length=5000, required=True, widget=Textarea())

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']
