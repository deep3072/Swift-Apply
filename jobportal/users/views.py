from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import RegisterUserForm
from .models import User
from django.contrib import messages
if __package__ is None or __package__ == '':
    # uses current directory visibility
    from jobportal.resume.models import Resume
    from jobportal.company.models import Company
else:
    # uses current package visibility
    # import users.models.User
    from resume.models import Resume
    from company.models import Company
# from jobportal.resume.models import Resume
# from jobportal.company.models import Company

# register recruiter only
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            new_recruiter = form.save(commit=False)
            new_recruiter.recruiter = True
            new_recruiter.username = new_recruiter.email
            new_recruiter.save()
            Company.objects.create(user=new_recruiter)
            messages.info(request, "Great, your account is created!")
            return redirect('login')
        else:
            messages.warning(request, "Something went wrong!")
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
        context = {
            'form': form
        }
        return render(request, 'users/register_recruiter.html', context)

# register applicant only
def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        # print(form)
        if form.is_valid():
            new_applicant = form.save(commit=False)
            new_applicant.applicant = True
            new_applicant.username = new_applicant.email
            new_applicant.save()
            Resume.objects.create(user=new_applicant)
            messages.info(request, "Great, your account is created!")
            return redirect('login')
        else:
            messages.warning(request, "Something went wrong!")
            return redirect('register-applicant')
    else:
        form = RegisterUserForm()
        context = {
            'form': form
        }
        return render(request, 'users/register_applicant.html', context)

#login user
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong!')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

# logout user
def logout_user(request):
    logout(request)
    messages.info(request, 'Logout Successful!')
    return redirect('login')
