from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    fullname = models.CharField(max_length=255, null=False)
    born_date = models.CharField(max_length=150)
    born_location = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f"{self.fullname}"


class Quote(models.Model):
    quote = models.TextField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.quote}"
