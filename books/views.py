from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


from .models import Book
from .forms import BookForm


@login_required
def my_books(request):
    books = Book.objects.filter(user=request.user)
    return render(request, './templates/books/my_books.html', {'books': books})




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, '../templates/register.html', {'form': form})


@login_required
def profile_view(request):
    # Handle form submission
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('profile')

    # Display list of books
    books = Book.objects.filter(user=request.user)
    form = BookForm()
    context = {
        'books': books,
        'form': form
    }
    return render(request, '../templates/profile.html', context)