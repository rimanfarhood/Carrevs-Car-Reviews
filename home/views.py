from django.views.generic import ListView
from reviews.models import CarReviewModel


class Index(ListView):
    template_name = 'home/index.html'
    model = CarReviewModel
    context_object_name = 'reviews'

    def get_queryset(self):
        return self.model.objects.all()[:3]
