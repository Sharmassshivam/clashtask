from django.shortcuts import render, redirect
from .models import student
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth


def home(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm']:
            try:
                user = User.objects.get(username=request.POST['uname'])
                return render(request, 'signup.html', {"except": "username already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['uname'], password=request.POST['password'])
                phone = request.POST['phone']
                fname = request.POST['fname']
                fsurname = request.POST['sname']
                new = student(name=fname, surname=fsurname, phone=phone, user=user)
                new.save()
                return render(request, 'logged.html', {"new": new})

        return render(request, "signup.html", {"except": "your passwords didnt match TRY AGAIN !!!"})

    return redirect(home)


def check(request):
    if request.method == "POST":
        username = request.POST['lognam']
        password = request.POST['logpass']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            new2 = student.objects.get(name=request.POST['userame'])

            return render(request, 'logged.html', {"new": new2})

        return redirect(login)

    return redirect(login)
def instructions(request):
    print("hello")
