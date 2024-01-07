from django.urls import path
from .views import AddCarReview, Reviews

urlpatterns = [
    path("", AddCarReview.as_view(), name="add_review"),
    path("reviews/", Reviews.as_view(), name="reviews"),
]
