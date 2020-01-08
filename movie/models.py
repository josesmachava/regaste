from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from account.models import User


class Genre(models.Model):
    name = models.CharField(max_length=255, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Actor(models.Model):
    name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=False)

    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Director(models.Model):
    name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=False)

    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=255, null=False)
    year = models.DateField()
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='static/images/movie/')
    url = models.URLField(max_length=225)
    price = models.CharField(max_length=255, null=False)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}  -  {}".format(self.title, self.release_date, self.category)


class OrderMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Trailer(models.Model):
    title = models.CharField(max_length=255, null=False)
    url = models.URLField(max_length=225)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    order = models.ForeignKey(OrderMovie, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?84?\d{9,9}$',
                                 message="O número de telefone deve ser digitado no formato: '849394995'. São permitidos até 13 dígitos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True,
                                          unique=True)  # validators should be a list

    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
