from django import forms
from .models import Book, Column, Shelf, Group, Library

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'shelf', 'genre', 'description']

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ['name', 'group', 'description']

class ShelfForm(forms.ModelForm):
    class Meta:
        model = Shelf
        fields = ['name', 'column', 'description']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'library', 'description']

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name', 'address', 'contact', 'description']