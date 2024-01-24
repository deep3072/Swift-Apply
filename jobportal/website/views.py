from django.shortcuts import render

if __package__ is None or __package__ == '':
    from jobportal.job.models import Job
else:
    from job.models import Job

# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def job_listing(request):
    jobs = Job.objects.filter(is_available=True)
    context = {
        'Jobs': jobs
    }
    return render(request, 'website/job_listing.html', context)
