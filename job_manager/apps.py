from django.apps import AppConfig


class JobManagerConfig(AppConfig):
    '''
    Job manager app configuration class
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'job_manager'
