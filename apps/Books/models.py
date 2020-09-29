from django.db import models
# from datetime import datetime

# Author
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name()

# Book
class Book(models.Model):
    title = models.CharField(max_length=500)
    published_date = models.DateField()
    # relation
    author = models.ForeignKey(
        Author, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        # self.Alumno = self.Alumno.NombreCompleto, due to __str__
        return '{0} => {1}'.format(self.title, self.author)

