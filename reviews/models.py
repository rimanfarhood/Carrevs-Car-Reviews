from django.db import models
from django.contrib.auth.models import User
import datetime
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from django.core.validators import MinValueValidator, MaxValueValidator

# Choice fields for car information

current_year = datetime.datetime.now().year

YEAR_MODEL = [(year, str(year)) for year in range(current_year, current_year - 20, -1)]

FUEL_TYPE = (
    ("petrol", "Petrol"),
    ("diesel", "Diesel"),
    ("ethanol", "Ethanol"),
    ("hybrid", "Hybrid"),
    ("electric", "Electric"),
)

CAR_MAKE = (
    ("audi", "Audi"),
    ("bmv", "BMV"),
    ("chevrolet", "Chevrolet"),
    ("dodge", "Dodge"),
    ("Fiat", "Fiat"),
    ("ford", "Ford"),
    ("honda", "Honda"),
    ("hyundai", "Hyundai"),
    ("kia", "Kia"),
    ("mazda", "Mazda"),
    ("mercedes", "Mercedes"),
    ("mini cooper", "Mini Cooper"),
    ("nissan", "Nissan"),
    ("renault", "Renault"),
    ("suzuki", "Suzuki"),
    ("tesla", "Tesla"),
    ("toyota", "Toyota"),
    ("volkswagen", "Volkswagen"),
    ("volvo", "Volvo"),
)

STATE = (("new", "New"), ("used", "Used"))

GEARBOX = (("manual", "Manual"), ("automatic", "Automatic"))

DRIVETRAIN_TYPES = (
    ("front-wheel", "Front-wheel"),
    ("rear-wheel", "Rear-wheel"),
    ("four-wheel", "Four-wheel"),
)

MILES = [
    ("0 - 500", "0 - 500"),
    ("500 - 1500", "500 - 1500"),
    ("2000 - 4000", "2000 - 4000"),
    ("5000 - 7000", "5000 - 7000"),
    ("7500 - 10.000", "7500 - 10.000"),
    ("11.000 - 13.000", "11.000 - 13.000"),
    ("14.000 - 16.000", "14.000 - 16.000"),
    ("17.000 - 19.000", "17.000 - 19.000"),
    ("20.000+", "20.000+"),
]

CAR_TYPES = (
    ("sedan", "Sedan"),
    ("hatchback", "Hatchback"),
    ("cabriolet", "Cabriolet"),
    ("wagon", "Wagon"),
    ("suv", "SUV"),
    ("coupe", "Coupe"),
    ("crossover", "Crossover"),
    ("compact", "Compact"),
    ("truck", "Truck"),
    ("minivan", "Minivan"),
)


class CarModel(models.Model):
    """
    Model representing the car information for review
    """

    user = models.ForeignKey(
        User, related_name="review_owner", on_delete=models.CASCADE
    )
    make = models.CharField(max_length=20, choices=CAR_MAKE, null=False, blank=False)
    model = models.CharField(max_length=300, null=False, blank=False)
    year = models.IntegerField(
        choices=YEAR_MODEL, default=current_year, null=False, blank=False
    )
    fuel = models.CharField(max_length=20, choices=FUEL_TYPE, null=False, blank=False)
    condition = models.CharField(max_length=5, choices=STATE, null=False, blank=False)
    engine_size = models.CharField(max_length=10, null=False, blank=False)
    transmission = models.CharField(
        max_length=20, choices=GEARBOX, null=False, blank=False
    )
    drivetrain = models.CharField(
        max_length=15, choices=DRIVETRAIN_TYPES, null=False, blank=False
    )
    mileage = models.CharField(max_length=25, choices=MILES, null=False, blank=False)
    price = models.CharField(max_length=15, null=False, blank=False)
    hp = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(66, message="Invalid input, the value is too low"),
            MaxValueValidator(2012, message="Invalid input, value to high"),
        ],
    )
    car_type = models.CharField(
        max_length=10, choices=CAR_TYPES, null=False, blank=False
    )
    image = ResizedImageField(
        size=[1000, None],
        quality=75,
        upload_to="reviews/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.make} - {self.model}"


# Choices for car review

RATING = [
    (1, "1/5"),
    (2, "2/5"),
    (3, "3/5"),
    (4, "4/5"),
    (5, "5/5"),
]


class CarReviewModel(CarModel):
    """
    Model to create car reviews
    """

    drivingexp = models.IntegerField(choices=RATING, null=False, blank=False)
    acceleration = models.IntegerField(choices=RATING, null=False, blank=False)
    comfort = models.IntegerField(choices=RATING, null=False, blank=False)
    safety = models.IntegerField(choices=RATING, null=False, blank=False)
    practicality = models.IntegerField(choices=RATING, null=False, blank=False)
    interior = models.IntegerField(choices=RATING, null=False, blank=False)
    ergonomics = models.IntegerField(choices=RATING, null=False, blank=False)
    pros = RichTextField(max_length=350, null=False, blank=False)
    cons = RichTextField(max_length=350, null=False, blank=False)
    additional = RichTextField(max_length=1500, null=True, blank=True)
    summary = RichTextField(max_length=500, null=False, blank=False)
    overall = models.IntegerField(choices=RATING, null=False, blank=False)
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-posted_date"]

    def __str__(self):
        return f"{self.make} - {self.model} {self.user} "
