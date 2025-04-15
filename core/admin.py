from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ('title', 'role', 'director', 'production')  # Display these fields in the admin list view
	search_fields = ('title', 'director')  # Add search functionality for these fields
