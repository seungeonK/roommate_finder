from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from phone_field import PhoneField
from PIL import Image

# (Seungeon)
# This is used for amenities.
# We have to have each amenity "object"
# So whenever we create a amenity, this will be created
class AbstractItem(models.Model):
    name = models.CharField(max_length = 30)

    # (Seungeon)
    # abstract = True will prevent this class from storing in the DB.
    class Meta:
        abstract = True

    def __str__(self):
        return self.name



class Profile(models.Model):
    ON_GROUNDS = "On-grounds"
    OFF_GROUNDS = "Off-grounds"
    NO_PREFERENCE = "No preference"

    GROUNDS_CHOICES = (
        (ON_GROUNDS, "On-Grounds"),
        (OFF_GROUNDS, "Off-Grounds"),
        (NO_PREFERENCE, "No Preference"),
    )

    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
        (NO_PREFERENCE, "No preference")
    )

    user = models.OneToOneField(
        User,
        null = True,
        on_delete = models.CASCADE, # if the "User" is deleted, profile is also deleted
    )

    image = models.ImageField(
        default = "default.jpg",

        # the directory that the image will be uploaded to (Django will create the directory if it doesn't exist yet)
        upload_to = "profile_pics",
    )

    age = models.IntegerField(
        blank = True,
        validators = [MinValueValidator(16), MaxValueValidator(120)],
        null = True,
    )

    bio = models.TextField(
        blank = True,
        default = "",
    )

    graduation_year = models.IntegerField(
        blank = True,
        default = 2021,
        validators = [MinValueValidator(2021), MaxValueValidator(2025)],
        null = True,
    )

    gender = models.CharField(
        verbose_name = "Gender",
        blank = True,
        max_length = 30,
        choices = GENDER_CHOICES[0:3],
    )

    pronouns = models.CharField(
        blank = True,
        max_length = 50,
    )

    phone_number = PhoneField(
        blank = True,
        max_length = 14,
    )

    on_grounds = models.CharField(
        blank = True,
        choices = GROUNDS_CHOICES,
        max_length = 50,
        verbose_name = "On-Grounds or Off-Grounds?"
    )

    max_price = models.IntegerField(
        verbose_name = "Max Rent or Rent Amount",
        blank = True,
        validators = [MinValueValidator(0), MaxValueValidator(10000)],
        default = 600,
    )

    display_profile = models.BooleanField(
        blank = True,
        default = False,
        verbose_name = "MAKE PROFILE PUBLIC",
    )

    # user wants to match with people who only have
    match_list = models.CharField(
        verbose_name = "Match with people who",
        blank = True,
        choices = (
            ("Property", "Have a property"),
            ("Profile", "Don't have a property"),
            ("Both", "No preference"),
        ),
        max_length = 100
    )

    pref_gender = models.CharField(
        verbose_name='Preferred Gender',
        blank=True,
        max_length=30,
        choices=GENDER_CHOICES,
    )

    # Returns a list of preferences that the user specified
    def preference_list(self):
        return ["max_price", "on_grounds", "pref_gender"]

    # to-string method for profiles
    def __str__(self):
        return f"{self.user.username}'s Profile"

    # Validation functions:
    def is_valid_graduation_year(self):
        if self.graduation_year != None:
            if self.graduation_year < 2021 or self.graduation_year > 2025:
                return False
        return True

    def is_valid_age(self):
        if self.age is not None:
            if self.age < 16 or self.age > 120:
                return False
        return True

    def is_valid_phone_number(self):
        if self.phone_number is not None:
            if sum(c.isdigit() for c in self.phone_number) != 10:
                return False
        return True

    def is_valid_max_price(self):
        if self.max_price is not None:
            if self.max_price < 0 or self.max_price > 10000:
                return False
        return True



# (Seungeon)
# Amenity class which inherited from AbstractItem
# AbstractItem will add each amenity
class Amenity(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "Amenities"
    def __str__(self):
        return self.name



class Property(models.Model):
    class Meta:
        verbose_name_plural = "Properties"

    FURNISHED = "Furnished"
    UNFURNISHED = "Unfurnished"
    FURNISHED_CHOICES = (
        (FURNISHED, "Furnished"),
        (UNFURNISHED, "Unfurnished"),
    )

    SINGLE = "Single"
    DOUBLE = "Double"
    EITHER = "Either"

    SINGLE_DOUBLE_CHOICES = (
        (SINGLE, "Single Room"),
        (DOUBLE, "Double Room"),
        (EITHER, "Either Single or Double"),
    )

    APARTMENT = "Apartment"
    HOUSE = "House"
    TOWNHOUSE = "Townhouse"
    OTHER = "Other"

    BUILDING_TYPE_CHOICES = (
        (APARTMENT, "Apartment"),
        (HOUSE, "House"),
        (TOWNHOUSE, "Townhouse"),
        (OTHER, "Other"),
    )

    ON_GROUNDS = "On-Grounds"
    OFF_GROUNDS = "Off-Grounds"

    GROUNDS_CHOICES = (
        (ON_GROUNDS, "On-Grounds"),
        (OFF_GROUNDS, "Off-Grounds"),
    )

    profile = models.OneToOneField(
        Profile,
        null = True,
        on_delete = models.CASCADE, # if the profile is deleted, the property is also deleted.
    )

    image = models.ImageField(
        default="default_property.jpg",

        # the directory that the image will be uploaded to (Django will create the directory if it doesn't exist yet)
        upload_to="property_pics",
    )

    rent = models.IntegerField(
        blank = True,
        validators = [MinValueValidator(0), MaxValueValidator(10000)],
        null = True,
    )

    amenities = models.TextField(
        blank = True,
        default="",
    )

    address = models.CharField(
        verbose_name = "Address/Location",
        blank = True,
        max_length = 200,
    )

    furnished = models.CharField(
        blank = True,
        choices = FURNISHED_CHOICES,
        max_length = 50,
    )

    current_number_of_roommates = models.IntegerField(
        blank = True,
        validators = [MinValueValidator(0), MaxValueValidator(20)],
        null = True,
    )

    number_of_roommates_seeking = models.IntegerField(
        blank = True,
        validators = [MinValueValidator(1), MaxValueValidator(20)],
        null = True,
    )

    room_type = models.CharField(
        blank = True,
        choices = SINGLE_DOUBLE_CHOICES,
        max_length = 50,
    )

    number_of_bedrooms = models.IntegerField(
        blank = True,
        validators = [MinValueValidator(1), MaxValueValidator(20)],
        null = True,
    )

    number_of_bathrooms = models.IntegerField(
        blank = True,
        validators = [MinValueValidator(1), MaxValueValidator(20)],
        null = True,
    )

    building_policies = models.TextField(
        blank = True,
        default = ""
    )

    lease_duration = models.IntegerField(
        "Lease Duration (Months)",
        blank = True,
        validators = [MinValueValidator(1), MaxValueValidator(72)],
        null = True,
        default = 12,
    )

    building_type = models.CharField(
        blank = True,
        choices = BUILDING_TYPE_CHOICES,
        max_length = 50,
    )

    other_details = models.TextField(
        blank = True,
        default = ""
    )

    display_property = models.BooleanField(
        blank = True,
        default = False,
        verbose_name = "MAKE PROPERTY PUBLIC",
    )

    on_grounds = models.CharField(
        blank = True,
        choices = GROUNDS_CHOICES,
        max_length = 50,
        verbose_name = "On-Grounds or Off-Grounds?"
    )

    # to-string method for properties
    def __str__(self):
       return f"{self.profile.user.first_name} {self.profile.user.last_name}'s Property"

    # Validation functions:
    def is_valid_rent(self):
        if self.rent is not None:
            if self.rent < 0 or self.rent > 10000:
                return False
        return True

    def is_valid_curr_num_roommates(self):
        if self.current_number_of_roommates is not None:
            if self.current_number_of_roommates < 0 or self.current_number_of_roommates > 20:
                return False
        return True

    def is_valid_num_roommates_seeking(self):
        if self.number_of_roommates_seeking is not None:
            if self.number_of_roommates_seeking < 1 or self.number_of_roommates_seeking > 20:
                return False
        return True

    def is_valid_number_of_bedrooms(self):
        if self.number_of_bedrooms is not None:
            if self.number_of_bedrooms < 1 or self.number_of_bedrooms > 20:
                return False
        return True

    def is_valid_number_of_bathrooms(self):
        if self.number_of_bathrooms is not None:
            if self.number_of_bathrooms < 1 or self.number_of_bathrooms > 20:
                return False
        return True

    def is_valid_lease_duration(self):
        if self.lease_duration is not None:
            if self.lease_duration < 1 or self.lease_duration > 72:
                return False
        return True
