from django.contrib import admin

from .models import Author, Book, Shelf, Column, Group, Library

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Shelf)
admin.site.register(Column)
admin.site.register(Group)
admin.site.register(Library)


