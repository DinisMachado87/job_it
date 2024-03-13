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
    paginate_by = 10
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
            job.slug = slugify(job.job_to_apply)
            job.save()
            return redirect('home')
        return render(request, 'job_manager/add_job.html', {'form': form})


class EditJobView(LoginRequiredMixin, View):
    def get(self, request):
        # Check if dream job exists for the current user
        user_id = request.user.id
        dream_job_slug = f'dream_job_{user_id}'
        dream_job = get_object_or_404(Job, slug=dream_job_slug, user=request.user)
        # Renders the job to edit form
        form = JobForm(instance=dream_job)
        return render(request, 'job_manager/edit_job.html', {'form': form})

    def post(self, request):
        # prepopulates the id hidden fields
        user_id = request.user.id
        dream_job_slug = f'dream_job_{user_id}'
        dream_job = get_object_or_404(Job, slug=dream_job_slug, user=request.user)
        form = JobForm(request.POST, instance=dream_job)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'job_manager/add_job.html', {'form': form})


class DeleteJobView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'job_manager/delete_job.html')


class EditDreamJobView(LoginRequiredMixin, View):
    def get(self, request):
        user_id = request.user.id
        dream_job_slug = f'dream_job_{user_id}'
        dream_job = get_object_or_404(Job, slug=dream_job_slug, user=request.user)
        form = JobForm(instance=dream_job)
        return render(request, 'job_manager/create_dream_job.html', {'form': form})

    def post(self, request):
        user_id = request.user.id
        dream_job_slug = f'dream_job_{user_id}'
        dream_job = get_object_or_404(Job, slug=dream_job_slug, user=request.user)
        form = JobForm(request.POST, instance=dream_job)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.slug = dream_job_slug
            job.is_dream_job = True
            job.job_description = 'Dream Job'
            job.job_to_apply = 'Dream Job'
            job.employer = 'Dream Employer'
            job.save()
            print('Form is valid')
            return redirect('home')
        else:
            print("Form errors:", form.errors)
        return render(request, 'job_manager/create_dream_job.html', {'form': form})
