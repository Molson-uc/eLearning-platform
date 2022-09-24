from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title",)

    def get_absolute_url(self):
        return self.slug


class Course(models.Model):
    owner = (
        models.ForeignKey(
            User, on_delete=models.CASCADE, related_name="courses_created"
        ),
    )
    subject = (
        models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="courses"),
    )
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
