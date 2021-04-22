from django.contrib import admin
from .models import Book, Metric, Category, Isbn
from .forms import BookForm
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
     category = Category
     list_display = ("name", "created_at")

class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ("title", "user", "content")
    list_filter = ("Categories",)
    search_fields = ("title",)


class BookInline(admin.StackedInline):
    model = Book
    max_num = 4
    extra = 1

class IsbnAdmin (admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Metric)
admin.site.register(Isbn, IsbnAdmin)