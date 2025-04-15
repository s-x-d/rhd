app_name = 'core'

from django.urls import path
from .views import MovieListView


from . import views

urlpatterns = [
	path('', MovieListView.as_view(), name='home'),
]
