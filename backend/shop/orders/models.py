from django.db import models
from authorisation.models import CustomUser

from books.models import Book


class Order(models.Model):
    STATUS_CHOICES = (
        (1, "cart"),
        (2, "in processs"),
        (3, "done")
    )

    user = models.ForeignKey(CustomUser)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)
    timestamp = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    book = models.ForeignKey(Book)
    quantity = models.PositiveSmallIntegerField()
