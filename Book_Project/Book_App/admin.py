from django.contrib import admin

from .models import Book
from .models import Author
from .models import Course
from .models import Student


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Student)
