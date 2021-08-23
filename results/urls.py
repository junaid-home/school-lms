from django.urls import path
from results.views import renderResults, renderSingleResult

urlpatterns = [
    path('results/', renderResults, name='results'),
    path('results/<int:Id>/', renderSingleResult, name='results')
]
