from django.urls import path
from .views import (
    AddCarReview, Reviews,
    CarReviewDetail, DeleteReview
)

urlpatterns = [
    path("", AddCarReview.as_view(), name="add_review"),
    path("reviews/", Reviews.as_view(), name="reviews"),
    path("<slug:pk>/", CarReviewDetail.as_view(), name="review_detail"),
    path("delete/<slug:pk>/", DeleteReview.as_view(), name="delete_review"),
]
