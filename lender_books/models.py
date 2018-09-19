from django.db import models
import datetime


class Book(models.Model):

    STATUS = [
        ('available', 'Available'),
        ('checked-out', 'Checked out'),
    ]

    YEAR = [(str(i), str(i)) for i in range(1900, 2018)]

    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    year = models.CharField(choices=YEAR, max_length=4)
    status = models.CharField(choices=STATUS, default='Available', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Book: {self.title}'

    def __repr__(self):
        return f'Book: {self.title} ({self.author},{self.status})'
