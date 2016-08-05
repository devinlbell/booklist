from django.db import models

# Create your models here.
BOOK_CHOICES = [('Novel', 'nov'), ('Hardcover', 'hc'), ('Paperback', 'pb'), ('Kindle', 'knd'), ('Audible', 'aud'), ('Magazine', 'mag')]

class Books(models.Model):
	title = models.CharField(max_length=200)
	pub_date = models.DateField()
	summary = models.CharField(max_length=1000)
	price = models.DecimalField(max_digits=7,decimal_places = 2)
	link = models.URLField(max_length=500)
	img = models.URLField(max_length=500)
	author = models.CharField(max_length=200, null = True)
	book_type = models.CharField(choices=BOOK_CHOICES, max_length=100)



def __str__(self):
	return self.title
