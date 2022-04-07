from .models import AccessRequests, Department, User
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserForm, MyUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

# Create your views here.

def loginPage(request):
    page = 'sign-in'
    if request.user.is_authenticated:
        return redirect('welcome')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,'User does not exists!!!')

        user = authenticate(request, email=email,password=password)

        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request,'Username or password is incorrect!!!')


    context = {'page':page}
    return render(request,'user_management_module/login_signup.html',context)

def logoutPage(request):
    logout(request)
    return redirect('sign-in')

def signupPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request,'Error occurred during sign up!!!')

    return render(request,'user_management_module/login_signup.html',{'form':form})

def welcome(request):
    return render(request, 'module/welcome.html', {})

def profile(request, pk):
    user = User.objects.get(id=pk)
    requests = AccessRequests.objects.all()
    for req in requests:
        if req.user.id == user.id:
            requests = AccessRequests.objects.get(id=req.id)

    return render(request,'user_management_module/profile.html',{'user':user,'requests':requests})

def usersPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    users = User.objects.filter(
        Q(first_name__icontains = q)|
        Q(last_name__icontains = q)
    )
    page = 'users'
    departments = Department.objects.all()
    context = {'departments':departments,'page':page, 'users':users}
    return render(request, 'user_management_module/users.html', context)

def usersPageSearch(request, pk):
    page = 'users'
    department = Department.objects.get(id=pk)
    users = User.objects.all().filter(department = department)
    departments = Department.objects.all()
    context = {'users':users,'page':page,'departments':departments}
    return render(request, 'user_management_module/users.html',context)

def elevatedRequests(request, pk):
    user = User.objects.get(id=pk)
    requests = AccessRequests()
    requests.user = user
    requests.save()
    requests = AccessRequests.objects.all()
    for req in requests:
        if req.user.id == user.id:
            requests = AccessRequests.objects.get(id=req.id)
    return render(request,'user_management_module/profile.html',{'user':user,'requests':requests})


def accessRequests(request):
    departments = Department.objects.all()
    all_requests = AccessRequests.objects.all()
    context = {'departments':departments,'requests':all_requests}
    return render(request, 'user_management_module/access_requests.html',context)

def deleteUser(request,pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    return render(request,'user_management_module/delete.html',{'user':user})

def deleteRequest(request,pk):
    requests = AccessRequests.objects.get(id=pk)
    if request.method == 'POST':
        requests.delete()
        return redirect('access-requests')
    return render(request,'user_management_module/approve_deny.html',{'requests':requests})

def approveRequest(request,pk):
    page = 'approve'
    requests = AccessRequests.objects.get(id=pk)
    user = User.objects.get(id=requests.user.id)
    if request.method == 'POST':
        requests.approve = True
        requests.deny = False
        user.head_of_department = True
        requests.save()
        user.save()
        return redirect('access-requests')
    context = {'page':page,'requests':requests}
    return render(request,'user_management_module/approve_deny.html',context)

def denyRequest(request,pk):
    page = 'deny'
    requests = AccessRequests.objects.get(id=pk)
    user = User.objects.get(id=requests.user.id)
    if request.method == 'POST':
        requests.deny = True
        requests.approve = False
        user.head_of_department= False
        requests.save()
        user.save()
        return redirect('access-requests')
    context = {'requests':requests,'page':page}
    return render(request,'user_management_module/approve_deny.html',context)
    

def editUser(request,pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile',pk=user.id)
        else:
            messages.error(request,'Error occurred during updating user!!!')
    context={'form':form,'user':user}
    return render(request,'user_management_module/update_users.html',context)


def addUser(request):
    form = UserForm()
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('users-page')
        else:
            messages.error(request,'Error occurred during adding the user')
    context = {'form':form}
    return render(request,'user_management_module/add_users.html',context)
