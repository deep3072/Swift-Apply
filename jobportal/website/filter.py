import django_filters

if __package__ is None or __package__ == '':
    from jobportal.job.models import Job
else:
    from job.models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['title', 'state', 'job_type', 'industry']
