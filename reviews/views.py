from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import CarReviewModel
from .forms import CarReviewModelForm


class Reviews(ListView):
    """View all Reviews"""

    template_name = "reviews/reviews.html"
    model = CarReviewModel
    context_object_name = "reviews"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            reviews = self.model.objects.filter(
                Q(manufacturer__icontains=query)
                | Q(model__icontains=query)
                | Q(condition__icontains=query)
                | Q(year__icontains=query)
            )
        else:
            reviews = self.model.objects.all()
        return reviews


class CarReviewDetail(DetailView):
    template_name = "reviews/review_detail.html"
    model = CarReviewModel
    context_object_name = "review"


class AddCarReview(LoginRequiredMixin, CreateView):
    """Add car review view"""

    template_name = "reviews/add_review.html"
    model = CarReviewModel
    form_class = CarReviewModelForm
    success_url = "/reviews/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddCarReview, self).form_valid(form)
