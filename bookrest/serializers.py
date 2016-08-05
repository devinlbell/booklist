from django.forms import widgets
from rest_framework import serializers
from bookrest.models import Books, BOOK_CHOICES

class BooksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Books
		fields = ('title', 'pub_date', 'summary', 'price', 'link', 'img', 'author', 'book_type')



