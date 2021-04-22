from django.core.exceptions import ValidationError

from books.utils import create_new_ref_number

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Isbn(models.Model):
    author_title = models.CharField(max_length=25)
    book_title = models.CharField(max_length=50)
    isbn_number = models.CharField(
           max_length = 10,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number()
      )

    def __str__(self):
        return f"{self.author_title} Author | {self.book_title} BookTitle | IsbnNumber {self.isbn_number} "

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise ValidationError("category must be greater than 2 characters")

        return name


class Metric(models.Model):
    visits = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    ratio = models.DecimalField(null=True, blank=True, max_digits=2, decimal_places=1)

    def __str__(self):
        return f"{self.visits} visits | {self.likes} likes | ratio {self.ratio} "


class Book(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2048)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="books")
    Categories = models.ManyToManyField(Category)
    metrics = models.OneToOneField(Metric, on_delete=models.CASCADE, null=True, blank=True)
    isbn = models.ForeignKey(Isbn, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
