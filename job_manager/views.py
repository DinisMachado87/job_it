from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm  # Create a form for job creation/editing


class JobListView(LoginRequiredMixin, generic.ListView):
    template_name = 'job_manager/index.html'
    paginate_by = 15

    def get_queryset(self):
        return Job.objects.filter(user=self.request.user)


class AddJobView(View):
    def get(self, request, *args, **kwargs):
        form = JobForm()
        return render(request, 'job_manager/add_job.html', {'form': form})
        # if request.user.is_authenticated:

    def post(self, request, *args, **kwargs):
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('home')
        return render(request, 'job_manager/add_job.html', {'form': form})


class EditJobView(View):
    def get(self, request, *args, **kwargs):
        # Check if dream job exists for the current user
        dream_job = get_object_or_404(Job, slug='dream_job', user=request.user)
        form = JobForm(instance=dream_job)
        return render(request, 'job_manager/edit_job.html', {'form': form})

    def post(self, request, *args, **kwargs):
        dream_job = get_object_or_404(Job, slug='dream_job', user=request.user)
        form = JobForm(request.POST, instance=dream_job)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'job_manager/add_job.html', {'form': form})


class DeleteJobView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'job_manager/delete_job.html')


class EditDreamJobView(View):
    def get(self, request, *args, **kwargs):
        dream_job = get_object_or_404(Job, slug='dream_job', user=request.user)
        form = JobForm(instance=dream_job)
        return render(request, 'job_manager/edit_dream_job.html', {'form': form})

    def post(self, request, *args, **kwargs):
        dream_job = get_object_or_404(Job, slug='dream_job', user=request.user)
        form = JobForm(request.POST, instance=dream_job)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'job_manager/edit_dream_job.html', {'form': form})
