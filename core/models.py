from django.db import models


class Movie(models.Model):
	title = models.CharField(max_length=255)  # Title of the movie
	role = models.CharField(max_length=255)  # Role (character name or specific role in production)
	director = models.CharField(max_length=255)  # Name of the director
	production = models.CharField(max_length=255)  # Production company/studio
	image = models.CharField(max_length=255)

	def __str__(self):
		return self.title  # Display the title when Model objects are printed
