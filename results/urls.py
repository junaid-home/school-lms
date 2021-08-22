from results.views import renderResults
from django.urls import path

urlpatterns = [
    path('results/', renderResults, name='results')
]
