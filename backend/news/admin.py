from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Publisher, Author, Book,Profile
from django.contrib.auth.models import User

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Profile)