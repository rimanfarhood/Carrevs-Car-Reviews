from django.contrib import admin
from .models import CarReviewModel


@admin.register(CarReviewModel)
class CarReviewModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CarReviewModel._meta.fields]
    search_fields = ["make", "model", "year"]
    list_filter = ("user",)
