from django.shortcuts import render
from django.views import View

from .models import Author, Book

class AuthorView(View):
    def get(self, request):
        authors = Author.objects.values('pk', 'name')
        return render(request, 'book/author.html', {'authors': authors})
