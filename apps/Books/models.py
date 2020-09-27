from django.db import models
# from datetime import datetime

# Author
class Author(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)

    def FullName(self):
        return self.FirstName + ' ' + self.LastName

    def __str__(self):
        return self.FullName()

# Book
class Book(models.Model):
    Title = models.CharField(max_length=500)
    Date = models.DateField()
    # relation
    Author = models.ForeignKey(
        Author, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        # self.Alumno = self.Alumno.NombreCompleto, due to __str__
        return '{0} => {1}'.format(self.Title, self.Author)

