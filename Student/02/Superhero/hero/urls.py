from django.urls import path
from .views import BlackWidowView, HulkView, IndexView, IronManView, BatmanView

urlpatterns = [
    path('', IndexView.as_view()),
    path('hulk', HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('blackwidow', BlackWidowView.as_view()),
    path('batman', BatmanView.as_view()),
]
