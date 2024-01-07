from django import forms
from .models import CarReviewModel
from djrichtextfield.widgets import RichTextWidget


class CarReviewModelForm(forms.ModelForm):
    class Meta:
        model = CarReviewModel
        exclude = ['user']
        fields = '__all__'

        pros = forms.CharField(widget=RichTextWidget())
        cons = forms.CharField(widget=RichTextWidget())
        additional = forms.CharField(widget=RichTextWidget())

        widget = {
            "summary": forms.Textarea(attrs={"rows": 10}),
        }

        labels = {
            "make": "Car Make",
            "model": "Car Model",
            "year": "Model Year",
            "fuel": "Fuel Type",
            "condition": "Condition",
            "engine_size": "Engine Size",
            "transmission": "Transmission",
            "drivetrain": "Drivetrain",
            "mileage": "Mileage",
            "price": "Retail Price",
            "hp": "Horsepower",
            "car_type": "Body Type",
            "image": "Car Image",
            "image_alt": "Describe Image",
            "drivingexp": "Driving Experience"
        }
