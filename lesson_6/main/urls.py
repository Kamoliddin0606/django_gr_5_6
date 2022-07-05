from django.urls import path
from .views import index
urlpatterns = [
    path('', index, name='index'),
    path('category/<int:id>', index, name='category'),
    
]
