import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_management.settings')
django.setup()

from library.models import Author, Library, Group, Column, Shelf, Book

fake = Faker()

def create_authors(n):
    for _ in range(n):
        Author.objects.create(
            name=fake.name(),
            bio=fake.text(),
            contact=fake.email()
        )

def create_libraries(n):
    for _ in range(n):
        Library.objects.create(
            name=fake.company(),
            address=fake.address(),
            contact=fake.phone_number(),
            description=fake.text()
        )

def create_groups(n):
    libraries = list(Library.objects.all())
    for _ in range(n):
        if libraries:
            Group.objects.create(
                name=fake.word(),
                library=fake.random_element(libraries),
                description=fake.text()
            )

def create_columns(n):
    groups = list(Group.objects.all())
    for _ in range(n):
        if groups:
            Column.objects.create(
                name=fake.word(),
                group=fake.random_element(groups),
                description=fake.text()
            )

def create_shelves(n):
    columns = list(Column.objects.all())
    for _ in range(n):
        if columns:
            Shelf.objects.create(
                name=fake.word(),
                column=fake.random_element(columns),
                description=fake.text()
            )

def create_books(n):
    authors = list(Author.objects.all())
    shelves = list(Shelf.objects.all())
    for _ in range(n):
        if authors and shelves:
            Book.objects.create(
                title=fake.sentence(),
                author=fake.random_element(authors),
                shelf=fake.random_element(shelves),
                description=fake.text(),
                genre=fake.word()
            )

# Number of records to create
n_records = 10

create_authors(n_records)
create_libraries(n_records)
create_groups(n_records)
create_columns(n_records)
create_shelves(n_records)
create_books(n_records)
