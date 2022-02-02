import datetime
import http.client

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Students, Myusers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import AddTracks, InsertStudent
from django.views.generic import *
from .models import *
from django.views import View
from django.views.decorators.http import ConditionalGetMiddleware, condition, conditional_page
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def homepage(request):
    loggeduser = Myusers.objects.filter(is_login=True)
    if len(loggeduser) != 0 and request.session.has_key('username'):
        authenuser = Myusers.objects.filter(username=request.session['username'])
        context = {'mode': '', 'msg': '', 'list': Students.objects.all(), 'username': authenuser[0].username,
                   'insertstudent': InsertStudent()}
        if request.method == 'GET':
            if request.GET == {}:
                context['mode'] = 'insert'
            else:
                context['mode'] = request.GET['mode']
        else:
            context['mode'] = request.POST['mode']
            mode = request.POST['mode']
            if mode == 'insert':
                context['msg'] = f"{mode} successfully"
                insertstudentpost = InsertStudent(request.POST)
                insertstudentpost.save()
            elif mode == 'selectby':
                query = request.POST['query']
                context['msg'] = f"{mode} successfully"
                context['list'] = Students.objects.filter(fname=query)
                print(f"Search {query}")
            else:
                print("unavalible")
        return render(request, 'crud/home.html', context)
    else:
        return redirect(loginpage)


def deleteStudent(request, stid):
    Students.objects.filter(id=stid).delete()
    return homepage(request)


class UpdateStudentView(View):
    def get(self, request, sid):
        context = {'rowid': sid, 'mode': 'update', 'list': Students.objects.all(),
                   'username': Myusers.objects.get(is_login=True).username,
                   'updatestudent': InsertStudent(instance=Students.objects.get(id=sid))}
        return render(request, 'crud/home.html', context)

    def post(self, request, sid):
        InsertStudent(request.POST, instance=Students.objects.get(id=sid)).save()
        return redirect(homepage)


def loginpage(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'crud/login.html')
    else:
        user = Myusers.objects.filter(email=request.POST['email'])
        authuser = authenticate(username=user[0].username, password=user[0].password)
        if user:
            if user[0].password == request.POST['password'] and authuser is not None:
                user.update(is_login=True)
                request.session['username'] = user[0].username
                login(request, authuser)
                return redirect(homepage)
            else:
                context['errormsg'] = "Incorrect password"
                return render(request, 'crud/login.html', context)
        else:
            context[
                'errormsg'] = "User not found, Please check password and email or Register if you don't have an acoount"
            return render(request, 'crud/login.html', context)


def registerpage(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'crud/register.html')
    else:
        if request.POST['password'] == request.POST['cpassword']:
            Myusers.objects.create(username=request.POST['username'], email=request.POST['email'],
                                   password=request.POST['password'], join_date=datetime.date.today(),
                                   login_time=datetime.datetime.now().time())
            User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                     password=request.POST['password'], is_staff=True)
        else:
            context['errormsg'] = 'Confirm password and password don not match'
        return render(request, 'crud/register.html', context)


def welcomepage(request):
    request.session.clear()
    logout(request)
    Myusers.objects.update(is_login=False)
    return render(request, 'crud/welcome.html')


def logined():
    loggeduser = Myusers.objects.filter(is_login=True)
    if len(loggeduser) != 0:
        return True
    else:
        return False


class Tracksinsertview(CreateView):
    model = Tracks
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        if not logined():
            return redirect(loginpage)
        else:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addtrack'] = AddTracks()
        context['tracklist'] = Tracks.objects.all()
        context['username'] = Myusers.objects.get(is_login=True).username
        return context

    success_url = reverse_lazy('Trackshomepage')


class UpdateTrackView(View):
    def get(self, request, tid):
        context = {'rowid': tid, 'trackmode': 'update', 'tracklist': Tracks.objects.all(),
                   'username': Myusers.objects.get(is_login=True).username,
                   'updatetrack': AddTracks(instance=Tracks.objects.get(tr_id=tid))}
        return render(request, 'crud/tracks_form.html', context)

    def post(self, request, tid):
        AddTracks(request.POST, instance=Tracks.objects.get(tr_id=tid)).save()
        return redirect('Trackshomepage')


def deleteTrack(request, trid):
    Tracks.objects.filter(tr_id=trid).delete()
    return redirect('Trackshomepage')
