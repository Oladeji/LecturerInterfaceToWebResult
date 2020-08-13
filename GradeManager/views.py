from django.shortcuts import render ,redirect
from .forms import UserLoginForm ,UserRegisterForm
from django.contrib.auth import  login, authenticate,logout
from django.contrib.auth.decorators import login_required
import requests
import json


def landing(request):
    return render(request,'GradeManager/landing.html')


def logout_view(request):
    return render(request,'Grademanager/logout_view.html')


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None) 

    if form.is_valid():
     
       username = form.cleaned_data.get('username')
       password = form.cleaned_data.get('password')
       user = authenticate(username=username,password=password)
       if not user :
               raise forms.ValidationError('This user does not exist')
       if not user.check_password(password):
                  raise forms.ValidationError('In Correct password')
       if not user.is_active:
                  raise forms.ValidationError('This user is not active')
       login(request,user)
       if next :
            return redirect(next)
       #return redirect('testing')
       return redirect('landing')
    else:
        form = UserLoginForm()
    context ={'form' : form }
    return render(request,'GradeManager/login_view.html',context)


def register_view(request):

        next = request.GET.get('next')
    #if request.method == 'POST':
        form = UserRegisterForm(request.POST or None) 
        if form.is_valid():
            user = form.save(commit=False)
            #form.save()
            username = form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            new_user = authenticate(username=username,password=password)
            login(request,new_user)
            if next :
                return redirect(next)
            return redirect('landing')
    #else:
    #    form = UserRegisterForm() 
        context ={'form' : form }
        return render(request,'GradeManager/register_view.html',context)




baseurl = 'http://192.168.0.111/'

@login_required
def availableCourses_view(request):
    courselist=""
    api=baseurl+'onlinecoursereg/api/Camp/getCourses'
    try:
          r = requests.get(api)
          courselist = json.loads(r.text)
          print('loaded')
          for i in  courselist: 
            print(i['MYCOURSEID'] ,' ==> ',i['MYCOURSENAME']) 
            print('_____________________________\n') 
    except  Exception as inst:
          print(inst)
    return render(request,'GradeManager/availableCourses_view.html',{'courselist':courselist})



@login_required
def displayCourse_view(request, csrid):  
    courselist={}
  #if request.method=='POST or None':
    ploads = {'csrid':csrid,'year':'1920'}
    #api='http://192.168.8.103/onlinecoursereg/api/Student/PythonPullForscoreEntry?data='+csrid
    api=baseurl+'onlinecoursereg/api/Student/Python'

    try:

          headers = {'content-type': 'application/json'}
          r = requests.post(api,json=ploads,headers=headers)
          courselist = json.loads(r.text)
          try:
             del request.session['courselist']
          except KeyError:
            pass
          request.session['courselist'] = courselist
          for i in  courselist: 
            print(i['MYSURNAME'] ,' ==> ',i['MYSTUDENTID']) 
            print('_____________________________\n') 
    except  Exception as inst:
          print(inst)
    return render (request,'GradeManager/displayCourse_view.html',{'courselist':courselist})
