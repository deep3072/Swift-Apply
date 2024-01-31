from django.db import models
# from ..users.models import User
# from jobportal.users.models import User
if __package__ is None or __package__ == '':
    # uses current directory visibility
    from jobportal.users.models import User
else:
    # uses current package visibility
    # import users.models.User
    from users.models import User


# from django.apps import users
# MyModel1 = apps.get_model('app1', 'MyModel1')


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    upload_resume = models.FileField(upload_to='resume', null=True, blank=True)
    # add cv


    def __str__(self):
        return f'{self.fname} {self.lname}'
