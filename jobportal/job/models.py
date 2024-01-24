from django.db import models

if __package__ is None or __package__ == '':
    from jobportal.users.models import User
    from jobportal.company.models import Company
else:
    from users.models import User
    from company.models import Company


# Create your models here.

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    salary = models.PositiveIntegerField(default=60000)
    location = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def ___str__(self):
        return self.title