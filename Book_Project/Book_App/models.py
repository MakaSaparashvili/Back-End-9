#ForeignKey Relationship

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


    def book_count(self):
        return self.book_set.count()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    def __str__(self):
        return self.title


#ManyToMany Relationship

class Course(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course, related_name='students')

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def list_courses(self):
        return ", ".join(course.title for course in self.courses.all())
    def __str__(self):
        return self.name

