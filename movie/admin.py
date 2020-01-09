from django.contrib import admin

# Register your models here.
from movie.models import Movie, Actor, Director, Genre, Payment, Order


class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Movie, MovieAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Genre, GenreAdmin)


class ActorAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Actor, ActorAdmin)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Director, DirectorAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Payment, PaymentAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['movie']


admin.site.register(Order, OrderAdmin)
