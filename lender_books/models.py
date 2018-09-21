from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth.models import User


class Book(models.Model):
    """A Book class that generates db with its attributes """

    STATUS = [
        ('available', 'Available'),
        ('checked-out', 'Checked out'),
    ]

    YEAR = [(str(i), str(i)) for i in range(1900, 2018)]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    year = models.CharField(choices=YEAR, max_length=4)
    status = models.CharField(choices=STATUS, default='Available', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(auto_now=True)

    def __str__(self):
        """A string representation of the book """
        return f'Book: {self.title}'

    def __repr__(self):
        """The official representation of the books title, author and status of book"""
        return f'Book: {self.title} ({self.author},{self.status})'


@receiver(models.signals.post_save, sender=Book)
def set_book_checked_out_date(sender, instance, **kwargs):
    """This method immediately checks the status of when the user changes the status of a book"""
    if instance.status == 'available' and not instance.last_borrowed:
        instance.last_borrowed = timezone.now()
        instance.save()
