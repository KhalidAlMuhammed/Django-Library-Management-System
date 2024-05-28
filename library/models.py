from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, default="")
    bio = models.TextField(default="")
    contact = models.CharField(max_length=100, default="")

class Library(models.Model):
    name = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=200, default="")
    contact = models.CharField(max_length=100, default="")
    description = models.TextField(default="")

class Group(models.Model):
    name = models.CharField(max_length=100, default="")
    library = models.ForeignKey(Library, on_delete=models.CASCADE, default="")
    description = models.TextField(default="")

class Column(models.Model):
    name = models.CharField(max_length=100, default="")
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    description = models.TextField(default="")

class Shelf(models.Model):
    name = models.CharField(max_length=100, default="")
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    description = models.TextField(default="")

class Book(models.Model):
    title = models.CharField(max_length=100, default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    description = models.TextField(default="")
    genre = models.CharField(max_length=50, default="")
