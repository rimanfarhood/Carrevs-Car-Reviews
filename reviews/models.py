from django.db import models
from django.contrib.auth.models import User
import datetime
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from django.core.validators import MinValueValidator, MaxValueValidator

# Choice fields for car information

current_year = datetime.datetime.now().year

YEAR_MODEL = [
    (year, str(year)) for year in range(current_year, current_year - 20, -1)
]

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
