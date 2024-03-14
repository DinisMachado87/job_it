from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Job criteria choices variables
CHOICES_office_days = (
    (0, 'n/a'),
    (1, 'Work f/ home'),
    (2, '1'),
    (3, '2'),
    (4, '3'),
    (5, '4'),
    (6, '5'),
    (7, '6'),
    (8, '7')
)
CHOICES_responsibility = (
    (0, 'n/a'),
    (1, 'Manager'),
    (2, 'Supervisor'),
    (3, 'Team Leader'),
    (4, 'Employee')
)
CHOICES_schedule_type = (
    (0, 'n/a'),
    (1, 'Fixed'),
    (2, 'Flexible'),
    (3, 'Remote')
)
CHOICES_starting_time = (
    (0, 'n/a'),
    (1, '6:00'),
    (2, '6:30'),
    (3, '7:00'),
    (4, '7:30'),
    (5, '8:00'),
    (6, '8:30'),
    (7, '9:00'),
    (8, '9:30'),
    (9, '10:00'),
    (10, '10:30'),
    (11, '11:00'),
    (12, '11:30'),
    (13, '12:00'),
    (14, '12:30'),
    (15, '1:00'),
    (16, '1:30'),
    (17, '2:00'),
    (18, '2:30'),
    (19, '3:00'),
    (20, '3:30'),
    (21, '4:00'),
    (22, '4:30'),
    (23, '5:00'),
    (24, '5:30'),
    (25, '6:00'),
    (26, '6:30'),
    (27, '7:00'),
    (28, '7:30'),
    (29, '8:00'),
    (30, '8:30'),
    (31, '9:00'),
    (32, '9:30'),
    (33, '10:00'),
    (34, '10:30'),
    (35, '11:00'),
    (36, '11:30'),
    (37, '12:00'),
    (38, '12:30'),
    (39, '1:00'),
    (40, '1:30'),
    (41, '2:00'),
    (42, '2:30'),
    (43, '3:00'),
    (44, '3:30'),
    (45, '4:00'),
    (46, '4:30'),
    (47, '5:00'),
    (48, '5:30'),
)
CHOICES_company_size = (
    (0, 'n/a'),
    (1, 'Small'),
    (2, 'Medium'),
    (3, 'Large')
)
CHOICES_yes_no = (
    (0, 'n/a'),
    (1, 'Yes'),
    (2, 'No')
)
CHOICES_freelance_hired = (
    (0, 'n/a'),
    (1, 'Freelance'),
    (2, 'Employed')
)
CHOICES_office_type = (
    (0, 'n/a'),
    (1, 'Open'),
    (2, 'Cubicle'),
    (3, 'Private')
)
CHOICES_status = (
    (0, 'n/a'),
    (1, 'Considering'),
    (2, 'Applied'),
    (3, 'Interviewing'),
    (4, 'Rejected'),
    (5, 'Accepted')
)


class Job(models.Model):
    '''
    The Job model is used to store the user's job applications.
    The model includes fields for the user's job criteria
    and a method to calculate the match percentage between the current job
    and the user's dream job.
    '''
    # User Info
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_jobs"
    )
    # Dream job reference
    is_dream_job = models.BooleanField(default=False)
    # Job description
    job_to_apply = models.CharField(max_length=15)
    employer = models.CharField(max_length=15, default="")
    slug = models.SlugField(max_length=30, unique=True)
    # job criteria
    commute_time = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(120)],
        help_text="in minutes"
    )
    office_days = models.IntegerField(
        choices=CHOICES_office_days,
        default=5,
        help_text="per week"
    )
    full_time_percentage = models.IntegerField(
        default=100,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    responsibility = models.IntegerField(
        choices=CHOICES_responsibility,
        default=3,
        null=True,
    )
    pay = models.IntegerField(
        validators=[MaxValueValidator(99999999)],
        default=0,
    )
    holiday_days = models.IntegerField(
        default=20,
        validators=[MinValueValidator(0), MaxValueValidator(365)],
        help_text="per year"
    )
    schedule_type = models.IntegerField(
        choices=CHOICES_schedule_type,
        default=0,
    )
    starting_time = models.IntegerField(
        choices=CHOICES_starting_time,
        default=0,
        help_text="of the work day"
    )
    company_size = models.IntegerField(
        choices=CHOICES_company_size,
        default=1,
    )
    bring_pet = models.IntegerField(
        choices=CHOICES_yes_no,
        default=1,
        help_text="- Whether pets are allowed in the office"
    )
    own_computer = models.IntegerField(
        choices=CHOICES_yes_no,
        default=1,
        help_text="- Whether you need to bring your own computer"
    )
    office_type = models.IntegerField(
        choices=CHOICES_office_type,
        default=0,
        help_text="layout"
    )
    pet_sitter = models.IntegerField(
        choices=CHOICES_yes_no,
        default=1,
        help_text="available close to the office"
    )
    child_care = models.IntegerField(
        choices=CHOICES_yes_no,
        default=1,
        help_text="available close to the office"
    )
    freelance_hire = models.IntegerField(
        choices=CHOICES_freelance_hired,
        default=0,
        help_text="- Invoicing the company vs hired as an employee"
    )
    status = models.IntegerField(
        choices=CHOICES_status,
        default=0,
        help_text="of the job application"
    )
    job_description = models.TextField(
        default="Optinal notes",
    )
    # Match percentage
    match_percentage = models.IntegerField(default=0)

    def calculate_match_percentage(self):
        '''
        Calculate the match percentage between the current job and the dream job.

        The match percentage is calculated by comparing the current job 
        with the dream job 
        and calculating the percentage difference between each field. 
        The average percentage difference across all fields 
        is then calculated to determine the overall match percentage.

        The match percentage is used to rank the job applications based 
        on how closely they match the user's dream job criteria.
        '''
        # Retrieve the dream job for this user
        dream_job = Job.objects.filter(
            user=self.user, is_dream_job=True).first()

        if not dream_job:
            # If there's no dream job defined, return 0% match
            return 100

        total_fields = 0
        total_percentage = 0

        # Calculate match percentage for each field and accumulate the total
        for field in self._meta.fields:
            # Skip the fields that are not relevant for comparison
            if field.name not in [
                'id',
                'user',
                'job_to_apply',
                'employer',
                'slug',
                'is_dream_job',
                'status',
                'job_description',
                'match_percentage'
            ]:
                # Increment the total fields count
                total_fields += 1

                # Get the corresponding values for the current job and the dream job
                dream_value = getattr(dream_job, field.name)
                current_value = getattr(self, field.name)

                # Skip comparison for 'Not applicable' options
                if dream_value == 0 or current_value == 0:
                    # Subtract 1 from total_fields
                    total_fields -= 1
                    continue

                if dream_value == current_value:
                    field_percentage = 100  # Field values match exactly
                else:

                    '''
                    Calculate the maximum value between the dream job's 
                    value and the current job's value
                    '''
                    max_value = max(dream_value, current_value)

                    # Calculate the percentage difference from the maximum value
                    percentage_difference = abs(
                        dream_value - current_value) / max_value

                    '''
                    Subtract the percentage difference 
                    from 100 to get the match percentage
                    '''
                    field_percentage = 100 - percentage_difference * 100

                # Accumulate the match percentage to the total percentage
                total_percentage += field_percentage

        if total_fields > 0:
            # Calculate the average match percentage across all fields
            match_percentage = total_percentage / total_fields
        else:
            # If there are no fields to compare, return 0% match
            match_percentage = 0

        return match_percentage

    def save(self, *args, **kwargs):
        # Save the match percentage when saving th e job object
        self.match_percentage = self.calculate_match_percentage()
        super().save(*args, **kwargs)

    class Meta:
        # Order the job applications by match percentage
        ordering = ['-match_percentage']

    def __str__(self):
        # set the job_to_apply as the string representation of the job object
        return self.job_to_apply
