from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from .models import CarReviewModel
from .forms import CarReviewModelForm


class AddCarReview(LoginRequiredMixin, CreateView):
    """Add car review view"""
    template_name = 'reviews/add_review.html'
    model = CarReviewModel
    form_class = CarReviewModelForm
    success_url = '/reviews/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddCarReview, self).form_valid(form)
