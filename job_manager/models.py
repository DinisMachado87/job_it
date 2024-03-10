from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Job criteria choices variables
CHOICES_office_days = (
    (0, 'Not applicable'),
    (1, 'Working from home'),
    (2, '1'),
    (3, '2'),
    (4, '3'),
    (5, '4'),
    (6, '5'),
    (7, '6'),
    (8, '7')
)
CHOICES_responsibility = (
    (0, 'Not applicable'),
    (1, 'Manager'),
    (2, 'Supervisor'),
    (3, 'Team Leader'),
    (4, 'Employee')
)
CHOICES_schedule_type = (
    (0, 'Not applicable'),
    (1, 'Fixed'),
    (2, 'Flexible'),
    (3, 'Remote')
)
CHOICES_starting_time = (
    (0, 'Not applicable'),
    (1, '6:00am'),
    (2, '6:30am'),
    (3, '7:00am'),
    (4, '7:30am'),
    (5, '8:00am'),
    (6, '8:30am'),
    (7, '9:00am'),
    (8, '9:30am'),
    (9, '10:00am'),
    (10, '10:30am'),
    (11, '11:00am'),
    (12, '11:30am'),
    (13, '12:00pm'),
    (14, '12:30pm'),
    (15, '1:00pm'),
    (16, '1:30pm'),
    (17, '2:00pm'),
    (18, '2:30pm'),
    (19, '3:00pm'),
    (20, '3:30pm'),
    (21, '4:00pm'),
    (22, '4:30pm'),
    (23, '5:00pm'),
    (24, '5:30pm'),
    (25, '6:00pm'),
    (26, '6:30pm'),
    (27, '7:00pm'),
    (28, '7:30pm'),
    (29, '8:00pm'),
    (30, '8:30pm'),
    (31, '9:00pm'),
    (32, '9:30pm'),
    (33, '10:00pm'),
    (34, '10:30pm'),
    (35, '11:00pm'),
    (36, '11:30pm'),
    (37, '12:00am'),
    (38, '12:30am'),
    (39, '1:00am'),
    (40, '1:30am'),
    (41, '2:00am'),
    (42, '2:30am'),
    (43, '3:00am'),
    (44, '3:30am'),
    (45, '4:00am'),
    (46, '4:30am'),
    (47, '5:00am'),
    (48, '5:30am'),
)
CHOICES_company_size = (
    (0, 'Not applicable'),
    (1, 'Small'),
    (2, 'Medium'),
    (3, 'Large')
)
CHOICES_yes_no = (
    (0, 'Not applicable'),
    (1, 'Yes'),
    (2, 'No')
)
CHOICES_freelance_hired = (
    (0, 'Not applicable'),
    (1, 'Freelance'),
    (2, 'Employed')
)
CHOICES_office_type = (
    (0, 'Not applicable'),
    (1, 'Open'),
    (2, 'Cubicle'),
    (3, 'Private')
)
CHOICES_status = (
    (0, 'Not applicable'),
    (1, 'Considering'),
    (2, 'Applied'),
    (3, 'Interviewing'),
    (4, 'Rejected'),
    (5, 'Accepted')
)


class Job(models.Model):
    """ Job class """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_jobs"
    )
    # Dream job reference
    is_dream_job = models.BooleanField(default=False)
    # Job description
    job_to_apply = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    job_description = models.TextField()
    # job criteria
    commute_time = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(120)],
        help_text="Commute time in minutes"
    )
    office_days = models.IntegerField(
        choices=CHOICES_office_days,
        default=5,
        help_text="Number of office days per week"
    )
    full_time_percentage = models.IntegerField(
        default=100,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Percentage of full-time commitment"
    )
    responsibility = models.IntegerField(
        choices=CHOICES_responsibility,
        default=3,
        null=True,
        help_text="Job responsibility level"
    )
    pay = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00,
        help_text="pay for the job"
    )
    holiday_days = models.IntegerField(
        default=20,
        validators=[MinValueValidator(0), MaxValueValidator(365)],
        help_text="Number of holiday days per year"
    )
    schedule_type = models.IntegerField(
        choices=CHOICES_schedule_type,
        default=0,
        help_text="Type of work schedule"
    )
    starting_time = models.IntegerField(
        choices=CHOICES_starting_time,
        default=0,
        help_text="Starting time of the work"
    )
    company_size = models.IntegerField(
        choices=CHOICES_company_size,
        default=1,
        help_text="Size of the company"
    )
    bring_pet = models.IntegerField(
        choices=CHOICES_yes_no,
        default=1,
        help_text="Whether pets are allowed in the office"
    )
    own_computer = models.IntegerField(
        choices=CHOICES_yes_no,
        default=1,
        help_text="Whether you need to bring your own computer"
    )
    office_type = models.IntegerField(
        choices=CHOICES_office_type,
        default=0,
        help_text="Type of office layout"
    )
    pet_sitter = models.IntegerField(
        choices=CHOICES_yes_no,
        default=1,
        help_text="Availability of pet sitter close to the office"
    )
    child_care = models.IntegerField(
        choices=CHOICES_yes_no,
        default=1,
        help_text="Availability of child care close to the office"
    )
    freelance_hire = models.IntegerField(
        choices=CHOICES_yes_no,
        default=0,
        help_text="If you will be invoicing the company or hired as an employee"
    )
    status = models.IntegerField(
        choices=CHOICES_status,
        default=0,
        help_text="Current status of the job application"
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
            return 0

        total_fields = 0
        total_percentage = 0

        # Calculate match percentage for each field and accumulate the total
        for field in self._meta.fields:
            if field.name not in [
                    'id', 'user', 'job_to_apply', 'slug', 'is_dream_job', 'status']:
                # Increment the total fields count
                total_fields += 1

                # Get the corresponding values for the current job and the dream job
                dream_value = getattr(dream_job, field.name)
                current_value = getattr(self, field.name)

                # Skip comparison for 'Not applicable' options
                if dream_value == 0 or current_value == 0:
                    continue

                if dream_value == current_value:
                    field_percentage = 100  # Field values match exactly
                else:

                    # Calculate the percentage difference
                    # between the current job and the dream job
                    field_percentage = 100 - abs(dream_value - current_value)
                    # Ensure percentage doesn't go negative
                    field_percentage = max(field_percentage, 0)

                # Accumulate the percentage difference to the total percentage
                total_percentage += field_percentage

        if total_fields > 0:
            # Calculate the average match percentage across all fields
            match_percentage = total_percentage / total_fields
        else:
            # If there are no fields to compare, return 0% match
            match_percentage = 0

        return match_percentage

    # Save the match percentage to the database
    class Meta:
        ordering = ['-match_percentage']

    def __str__(self):
        return self.job_to_apply
