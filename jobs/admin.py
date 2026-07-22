from django.contrib import admin
from .models import Job, Application


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company_name', 'location', 'salary', 'posted_by', 'date_posted']
    search_fields = ['title', 'company_name', 'description']
    list_filter = ['location', 'date_posted']



class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['job', 'applicant', 'date_applied']

admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)