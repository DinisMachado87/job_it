from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Location(models.Model):
    choices = models.CharField(max_length=40)


class TransportType(models.Model):
    choices = models.CharField(max_length=40)


class HierarchyLevel(models.Model):
    choices = models.CharField(max_length=40)


class ScheduleType(models.Model):
    choices = models.CharField(max_length=40)


class YesNo(models.Model):
    choices = models.CharField(max_length=40)


class OfficeType(models.Model):
    choices = models.CharField(max_length=40)


class HireType(models.Model):
    choices = models.CharField(max_length=40)


class AppStatus(models.Model):
    choices = models.CharField(max_length=40)


class OtherCosts(models.Model):
    choices = models.CharField(max_length=40)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class RelocationChoice(models.Model):
    choices = models.CharField(max_length=40)


class Extras(models.Model):
    choices = models.CharField(max_length=40)


class AreaFocus(models.Model):
    choices = models.CharField(max_length=40)


class Role(models.Model):
    choices = models.CharField(max_length=40)


class CompanySize(models.Model):
    choices = models.CharField(max_length=40)


class OfficeFeatures(models.Model):
    choices = models.CharField(max_length=40)


class SocialActivities(models.Model):
    choices = models.CharField(max_length=40)


class Job(models.Model):
    # User Info
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_jobs"
    )
    # Relocation
    relocate = models.IntegerField(null=True, blank=False)
    location = models.IntegerField(null=True, blank=False)
    housing_cost = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=False)
    # Commute
    commute = models.IntegerField(null=True, blank=False)
    commute_time = models.IntegerField(default=0)
    transport = models.IntegerField(null=True, blank=False)
    commute_costs = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=False)
    # Other Costs
    other_costs = models.IntegerField(null=True, blank=False)
    # Work Details
    work_from_home = models.IntegerField(null=True, blank=False)
    office_days = models.IntegerField(default=5)
    full_time_percentage = models.IntegerField(
        default=0, blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    extras = models.IntegerField(null=True, blank=False)
    area_focus = models.IntegerField(null=True, blank=False)
    job_role = models.IntegerField(null=True, blank=False)
    responsibility = models.IntegerField(null=True, blank=False)
    min_pay = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=False)
    holiday_days = models.IntegerField(default=0, blank=False)
    schedule_type = models.IntegerField(null=True, blank=False)
    company_size = models.IntegerField(null=True, blank=False)
    # Office Details
    bring_pet = models.IntegerField(null=True, blank=False)
    own_computer = models.IntegerField(null=True, blank=False)
    office_type = models.IntegerField(null=True, blank=False)
    desk_features = models.IntegerField(null=True, blank=False)
    social_activities = models.IntegerField(null=True, blank=False)
    pet_sitter = models.IntegerField(null=True, blank=False)
    child_care = models.IntegerField(null=True, blank=False)
    # Hiring Details
    freelance_hire = models.IntegerField(null=True, blank=False)
    deadline = models.DateField(blank=False)
    status = models.IntegerField(null=True, blank=False)
