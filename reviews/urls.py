from django.urls import path
from .views import AddCarReview

urlpatterns = [
    path("", AddCarReview.as_view(), name="add_review"),
]
