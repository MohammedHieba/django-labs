from django import forms
from django.core.exceptions import ValidationError

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ("metrics",)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 10 or len(title) > 50:
            raise ValidationError("title shouldn't be between 10 & 50 characters")

        return title




