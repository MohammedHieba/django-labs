from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    books_list = Book.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(books_list, 5)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    return render(request, 'books/index.html', {"books": books})


def show(request, id):
    book = Book.objects.get(pk=id)
    return render(request, 'books/show.html', {
        'book': book})


def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'books/create.html', {'form': form})


def edit(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST or None, instance=book )
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'books/edit.html', {
        'form': form,
        'book': book})


def delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('index')