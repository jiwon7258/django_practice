from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)  # varchar
    """ 
    N:N 관계
    하나의 book에 여러개 author가 존재 가능
    하나의 author에 여러개 book이 존재 가능
     """
    authors = models.ManyToManyField("Author")
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class Author(models.Model):
    salutation = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name
