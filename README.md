README
# Job it. 
 Job Search Management app

*The link to [Job it.](https://jobit-e6faad3e8aa6.herokuapp.com/)*

## Overview

The Job Search Management App is a web application designed to help users manage their job search process effectively. It allows users to set up their dream job preferences, track job applications, visualize job matches, and manage application statuses. The app provides a user-friendly interface for organising and optimising the job search process, helping users find jobs that best match their preferences.

## User Stories

#### Create Dream Job Preferences Profile:

As a user, I can create a profile with my dream job preferences so that I can set up my job search criteria.

- AC1: I can specify preferences such as relocation, commuting distance, work from home option, salary range, etc.

- AC2: I can save my preferences for future reference.

#### Add Job Profiles:

As a user, I can add job profiles to my profile to track jobs I want to apply to.

- AC1: I can add details such as job title, application deadline, position availability, application link, etc.

- AC2: I can specify criteria for each job profile, matching those of my dream job preferences.

#### Automatically Update Dream Job Preferences:

As a user, I want my dream job preference choices to be automatically updated when I add a new option with a new job profile, so that my preferences stay up-to-date.

- AC1: Whenever I add a new job profile, I am prompted to review and update my dream job preferences if needed.

#### Customize Job Profile Criteria Fields:

As a user, I can customize job profile criteria fields to tailor them to specific job requirements.

- AC1: I can add custom fields such as specific skills, certifications, or preferences related to the job.

#### View Job Ratings and Visualization:

As a user, I can view an overall automatic rating for each job profile and visualize it in a chart.

- AC1: The job rating is calculated based on the matching percentage between the job criteria and my dream job preferences.

- AC2: The job rating is displayed in a chart along with other relevant information about each job.

#### Choose Number of Top Matching Jobs:

As a user, I can choose how many of the top matching jobs I want to see in the chart for better visualization and comparison.

- AC1: I can specify the number of top matching jobs to be displayed in the chart settings.

#### Select Main Criteria for Job Matching Chart:

As a user, I can choose the main criteria of the jobs to be visible in the header of the job matching chart for easier comparison.

- AC1: I can select the criteria such as salary range, commuting distance, work from home option, etc., to be displayed in the chart header.

#### Access Job Management Board:

As a user, I have access to a job management board to help with managing job application status.

- AC1: I can track the status of each job application (e.g., applied, interview scheduled, rejected) on a centralized board.

- AC2: I can update the status of each job application as it progresses through the hiring process.

#### Automatically Calculate Commute Distance:

As a user, I want the commute distance to be automatically calculated for each job profile to make informed decisions.

- AC1: The commuting distance is calculated based on the job location and my preferred mode of transportation.

## Languages:

### Dependencies

### Standard library imports:

### Other tools:

[VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.

[GitHub](https://github.com/) was used to host the code of the website.

## Resolved bugs

## Debugging the Database

When originally attempting to run migrations or start the Django server, the following error occured:

> (!Warning]
django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.


During the process of debugging the database-related issues, several solutions were attempted to address the "Models aren't loaded yet" error. Each solution aimed to ensure that database queries were performed at the appropriate time and that Django models were fully initialized before accessing them.


1. **Moving Database Queries into Callable Methods**:
   Initially, I tried moving database queries into functions within the models.py file. For example, instead of directly assigning choices to fields, I defined methods to retrieve choices when needed. However, this approach didn't fully solve the problem because Django models weren't fully ready when the models.py file was loaded.

   ```
   class Location(models.Model):
       @staticmethod
       def get_choices():
           return Location.objects.values_list('id', 'choice')
   ```

2. **Reusable get_choices Function**:
   Another attempt was to create a reusable function to get choices for any model class. This function aimed to centralize the logic for retrieving choices. However, it faced the same issue as before because Django models weren't fully initialized at the time of import.

   ```
   def get_choices(model_class):
       return model_class.objects.values_list('id', 'choice')
   ```

3. **Using a Callable Class**:
   To overcome the issue with directly querying the database in functions called at import time, I tried using a callable class. This class, named ChoiceGetter, was instantiated by Django when it was ready to get the choices. However, it caused a new problem where Django expected choices to be an iterable, but it received a callable instead.

   ```
   class ChoiceGetter:
       def __call__(self, model_class):
           return model_class.objects.values_list('id', 'choice')
   ```

4. **Modifying the ChoiceGetter Class**:
   To fix the issue with Django expecting choices to be an iterable, I modified the ChoiceGetter class to return choices as a list or tuple when called. This ensured that the choices were in the correct format for Django's expectations.

   ```
   class ChoiceGetter:
       def __call__(self, model_class):
           choices = model_class.objects.values_list('id', 'choice')
           return list(choices)
   ```

5. **Moving Logic to View or Form**:
   Finally, I realized that forms are processed after all models are loaded in Django. So, I moved the logic of setting choices to the form. This ensured that models were fully loaded before attempting to access them, avoiding issues with models not being ready at the time of import.

   ```
   class JobForm(forms.ModelForm):
       def __init__(self, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.fields['schedule_type'].choices = get_choices(ScheduleType)
           # Other fields' choices set similarly...
   ``` 

By experimenting with these different approaches and considering the timing of model initialization, eventually the issues were resolved, leading to a stable and functional database implementation.


## Contributors

Dinis Machado

## Credits

[Code with Mosh](https://codewithmosh.com)

## Acknowledgments

A special thank you to the Oversight and discussion insight from my Code Institute mentor Juliia Konn