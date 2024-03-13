from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm

# Create your views here.

'''
Index view
Checks if the user has a Dream Job object, 
if not, creates one before rendering the index page 
to make sure there are no errors when views search for the Dream Job slug.
The Dream jog slug is created using the user's id and the string 'dream_job_'
for uniqueness.
'''
class JobListView(LoginRequiredMixin, generic.ListView):
    template_name = 'job_manager/index.html'
    paginate_by = 5
    # Filtering the queryset to only show the user's jobs
    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)
# Overriding the default get method to check if the user has a Dream Job object
    def get(self, request):
        user_id = request.user.id
        dream_job_slug = f'dream_job_{user_id}'
        if not self.request.user.user_jobs.filter(slug=dream_job_slug).exists():
            # If user doesn't have a Dream Job object, create one
            Job.objects.create(
                user=request.user,
                slug=dream_job_slug,
                is_dream_job=True,
                job_description='Dream Job',
                job_to_apply='Dream Job',
                employer='Dream Employer'
            )
            # Redirect the user to Job chart index
            return redirect('home')
        else:
            # If user has a Dream Job object, proceed with default behavior
            return super().get(request)

class AddJobView(LoginRequiredMixin, View):
    # Create a new job to apply form
    def get(self, request):
        form = JobForm()
        return render(request, 'job_manager/add_job.html', {'form': form})
    # Save the new job to apply object
    def post(self, request):
        form = JobForm(request.POST)
        if form.is_valid():
            # Prepopulates id hidden fields
            job = form.save(commit=False)
            job.user = request.user
            job.is_dream_job = False
            # Create a slug for the job to apply
            job.slug = slugify(job.job_to_apply)
            # Calculate the match percentage with the method from the model
            job.match_percentage = job.calculate_match_percentage()
            job.save()
            return redirect('home')
        return render(request, 'job_manager/add_job.html', {'form': form})


class EditJobView(LoginRequiredMixin, View):
    # Edit an existing job to apply form
    def get(self, request, slug):
        # Retrieve the job to edit using the slug and the user
        job = get_object_or_404(Job, slug=slug, user=request.user)
        form = JobForm(instance=job)
        return render(request, 'job_manager/add_job.html', {'form': form})

    def post(self, request, slug):
        # Save the edited job to apply object
        job = get_object_or_404(Job, slug=slug, user=request.user)
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            # Prepopulates id hidden fields
            job = form.save(commit=False)
            job.user = request.user
            job.slug = slugify(job.job_to_apply)
            # Calculate the match percentage with the method from the model
            job.match_percentage = job.calculate_match_percentage()
            job.save()
            return redirect('home')
        # If the form is not valid, render the form with the errors
        return render(request, 'job_manager/add_job.html', {'form': form})


class DeleteJobView(LoginRequiredMixin, View):
    # Delete a job to apply object
    def get(self, request, slug):
        # Retrieve the job to delete using the slug and the user
        job = get_object_or_404(Job, slug=slug, user=request.user)
        return render(request, 'job_manager/delete_job.html', {'job': job})
    # Confirm the deletion of the job to apply object
    def post(self, request, slug):
        # Delete the job to apply object
        job = get_object_or_404(Job, slug=slug, user=request.user)
        job.delete()
        return redirect('home')

'''

EditDreamJobView is called automatically one first time 
after the user is created
to initiate a dream job object avoiding errors when the user tries to access 
the index page.

EditDreamJobView is a view that allows the user to edit their dream job.
The view retrieves the user's dream job using the slug and the user 
and renders the form with the user's dream job.
The view also saves the user's dream job object 
and recalculates the match percentage of all the user's jobs
in relation to the updated dream job fields.
More details about the match percentage calculation can be found in the model
where the method calculate_match_percentage is defined.
'''

class EditDreamJobView(LoginRequiredMixin, View):
    # Edit the user's dream job form
    def get(self, request):
        # Retrieve the user's dream job using the slug and the user
        user_id = request.user.id
        dream_job_slug = f'dream_job_{user_id}'
        dream_job = get_object_or_404(
            Job, slug=dream_job_slug, user=request.user)
        form = JobForm(instance=dream_job)
        # Render the form with the user's dream job
        return render(
            request, 'job_manager/create_dream_job.html', {'form': form})

    def post(self, request):
        # Save the user's dream job object
        # Retrieve the user's dream job using the slug and the user
        user_id = request.user.id
        dream_job_slug = f'dream_job_{user_id}'
        dream_job = get_object_or_404(
            Job, slug=dream_job_slug, user=request.user)
        form = JobForm(request.POST, instance=dream_job)
        if form.is_valid():
            # Prepopulates id hidden fields
            job = form.save(commit=False)
            job.user = request.user
            job.slug = dream_job_slug
            job.is_dream_job = True
            job.job_description = 'Dream Job'
            job.job_to_apply = 'Dream Job'
            job.employer = 'Dream Employer'
            # Set the match percentage to 100% for the dream job
            job.match_percentage = 100
            job.save()
            # Calculate the match percentage for all the user's jobs
            for job in Job.objects.filter(
                user=self.request.user, is_dream_job=False):
                job.match_percentage = job.calculate_match_percentage()
                job.save()
            # Redirect the user to Job chart index
            return redirect('home')
        else:
            # If the form is not valid, render the form with the errors
            return render(
                request, 'job_manager/create_dream_job.html', {'form': form})

class InstructionsView(generic.TemplateView):
    template_name = 'job_manager/instructions.html'