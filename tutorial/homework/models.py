from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=32)
    subject = models.CharField(max_length=32, null=True)
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=32)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    