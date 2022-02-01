import datetime

from django.shortcuts import render, redirect
from .models import Students, Myusers
from django.http import HttpRequest

# Create your views here.
def homepage(request):
    authenuser=Myusers.objects.filter(is_login=True)
    if len(authenuser ) == 1:
        context = {'mode': '', 'msg': '', 'list': Students.objects.all(), 'username': authenuser[0].username}
        if request.method == 'GET':
            if request.GET == {}:
                context['mode'] = 'insert'
            else:
                context['mode'] = request.GET['mode']
        else:
            context['mode'] = request.POST['mode']
            mode = request.POST['mode']
            if mode == 'insert':
                fnameQuery = request.POST['fname']
                lnameQuery = request.POST['lname']
                context['msg'] = f"{mode} successfully"
                Students.objects.create(fname=fnameQuery, lname=lnameQuery)
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


def deleteStudent(request,stid):
    Students.objects.filter(id=stid).delete()
    return homepage(request)


def updateStudent(request, sid):
    context={}
    if request.method == 'GET':
        context = {'rowid': sid,'mode':'update','list': Students.objects.all(),'username': Myusers.objects.get(is_login=True).username,'fname':Students.objects.get(id=sid).fname,'lname':Students.objects.get(id=sid).lname}
        return render(request, 'crud/home.html', context)
    else:
        context['mode'] = 'insert'
        context['list']= Students.objects.all()
        Students.objects.filter(id=sid).update(fname=request.POST['fname'], lname=request.POST['lname'])
        #return render(request, 'crud/home.html', context)
        return redirect(homepage)



def loginpage(request):
    context={}
    if request.method == 'GET':
        return render(request, 'crud/login.html')
    else:
        user = Myusers.objects.filter(email=request.POST['email'])
        if user:
            if user[0].password == request.POST['password']:
                user.update(is_login=True)
                return redirect(homepage)
            else:
                context['errormsg']="Incorrect password"
                return render(request, 'crud/login.html', context)
        else:
            context['errormsg']="User not found, Please check password and email or Register if you don't have an acoount"
            return render(request, 'crud/login.html',context)


def registerpage(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'crud/register.html')
    else:
        if request.POST['password'] == request.POST['cpassword']:
            Myusers.objects.create(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'], join_date=datetime.date.today(), login_time=datetime.datetime.now().time())
        else:
            context['errormsg']='Confirm password and password don not match'
        return render(request,'crud/register.html',context)



def welcomepage(request):
    Myusers.objects.update(is_login=False)
    return render(request, 'crud/welcome.html')
