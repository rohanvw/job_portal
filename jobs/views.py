from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Job, Application
from .forms import JobForm


class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10


class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['already_applied'] = Application.objects.filter(
                job=self.object, applicant=self.request.user
            ).exists()
        return context


class JobCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('my_jobs')

    def test_func(self):
        return self.request.user.role == 'employer' or self.request.user.is_staff

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        messages.success(self.request, "Job created successfully!")
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'jobs/job_form.html'
    success_url = reverse_lazy('my_jobs')

    def test_func(self):
        job = self.get_object()
        return self.request.user == job.posted_by and (self.request.user.role == 'employer' or self.request.user.is_staff)

    def form_valid(self, form):
        messages.success(self.request, "Job updated successfully!")
        return super().form_valid(form)


class JobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('my_jobs')

    def test_func(self):
        job = self.get_object()
        return self.request.user == job.posted_by and (self.request.user.role == 'employer' or self.request.user.is_staff)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Job deleted successfully!")
        return super().delete(request, *args, **kwargs)


class MyJobsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Job
    template_name = 'jobs/my_jobs.html'
    context_object_name = 'jobs'

    def test_func(self):
        return self.request.user.role == 'employer' or self.request.user.is_staff

    def get_queryset(self):
        return Job.objects.filter(posted_by=self.request.user)


@login_required
def apply_to_job(request, pk):
    job = get_object_or_404(Job, pk=pk)

    if request.user.role != 'seeker' and not request.user.is_staff:
        messages.error(request, "Only Job Seekers can apply for jobs.")
        return redirect('job_detail', pk=pk)

    if job.posted_by == request.user:
        messages.error(request, "You cannot apply to your own job posting.")
        return redirect('job_detail', pk=pk)

    application, created = Application.objects.get_or_create(
        job=job, applicant=request.user
    )
    if created:
        messages.success(request, f"Successfully applied for '{job.title}'.")
    else:
        messages.warning(request, f"You have already applied for '{job.title}'.")

    return redirect('my_applications')


class MyApplicationsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Application
    template_name = 'jobs/my_applications.html'
    context_object_name = 'applications'

    def test_func(self):
        return self.request.user.role == 'seeker' or self.request.user.is_staff

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user)
