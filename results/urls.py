from django.urls import path
from results.views import results_view, single_result_view

urlpatterns = [
    path('results/', results_view, name='results'),
    path('results/<int:Id>/', single_result_view, name='results')
]
