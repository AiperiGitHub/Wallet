from django.db import models
from django.utils.translation import gettext_lazy as _



class Author(models.Model):
    name = models.CharField(_('Имя автора'), max_length=100)
    email = models.EmailField(_('Email'), blank=True)

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField(null=True, blank=True)
    pages = models.IntegerField()

    def str(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


