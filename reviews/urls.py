from django.urls import path
from .views import (
    AddCarReview, Reviews,
    CarReviewDetail, DeleteReview,
    EditReview
)

urlpatterns = [
    path("", AddCarReview.as_view(), name="add_review"),
    path("reviews/", Reviews.as_view(), name="reviews"),
    path("<slug:pk>/", CarReviewDetail.as_view(), name="review_detail"),
    path("delete/<slug:pk>/", DeleteReview.as_view(), name="delete_review"),
    path("edit/<slug:pk>/", EditReview.as_view(), name="edit_review"),
]
