from django.shortcuts import render ,redirect
from .forms import UserLoginForm ,UserRegisterForm ,UploadedScoreForm
from django.contrib.auth import  login, authenticate,logout
from django.contrib.auth.decorators import login_required
import requests
import json
from django.http import HttpResponse ,HttpResponseNotFound 
#from openpyxl import Workbook
from django.conf  import settings
import openpyxl
from . DetailResult import DetailResult
from . generatescorelist import generatescorelist
from openpyxl.styles import Protection 
from . basicunit import basicunit ,MergebasicScorelist
from django.contrib import messages

def landing(request):
    return render(request,'GradeManager/landing.html')


def logout_view(request):
    return render(request,'Grademanager/logout_view.html')


def login_view(request):
  next = request.GET.get('next')
  if request.method == 'POST':
    form = UserLoginForm(request.POST) 
    if form.is_valid():

       username = form.cleaned_data.get('username')
       password = form.cleaned_data.get('password')
       user = authenticate(username=username,password=password)
       if not user :
               #raise forms.ValidationError('This user does not exist')
               print('This user does not exist 4')
               messages.error(request,"This user does not exist")
               
       if not user.check_password(password):
                  #raise forms.ValidationError('In Correct password')
                  print('This user does not exist 5') 
                  messages.error(request,"In Correct password")
                  
       if not user.is_active:
                  #raise forms.ValidationError('This user is not active')
                   print('This user does not exist 6')
                   messages.error(request,"This user is not active")
                   
       login(request,user)
       if next :
            return redirect(next)
       #return redirect('testing')
       return redirect('landing')
    else:
        for error in form.non_field_errors() :
            messages.error(request,error )  
            form = UserLoginForm()

    context ={'form' : form }
    return render(request,'GradeManager/login_view.html',context)

  context ={'form' : UserLoginForm() }
  return render(request,'GradeManager/login_view.html',context)


def register_view(request):

        next = request.GET.get('next')
        print(next)
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


@login_required
def availableCourses_view(request):
    courselist=""
    api=settings.BASE_URL+'/api/Camp/getCourses'
    try:
          r = requests.get(api)
          courselist = json.loads(r.text)
          messages.success(request, str (len(courselist))+ " Courses Successfully Loaded")
               
    except  Exception as inst:
          print(inst)
          messages.error(request,"Problem Loading Courses , Check Connection")
               
    return render(request,'GradeManager/availableCourses_view.html',{'courselist':courselist})

def processdata(request):  
  
    if request.method=='POST or None':
        print("A Post Message , Details Below")
        print(request.POST)
   
    return render(request,'GradeManager/landing.html')


@login_required
def displayCourse_view(request, csrid):  
    courselist={}
    if request.method=='POST or None':
        print("A Post Message , Details Below")
        url = request.POST.get("courselist")
        
        print(url)
    else: 
        ploads = {'csrid':csrid,'year':'1920'}
        #api='http://192.168.8.103/onlinecoursereg/api/Student/PythonPullForscoreEntry?data='+csrid
        api=settings.BASE_URL+'/api/Student/Python'

        try:
            headers = {'content-type': 'application/json'}
            r = requests.post(api,json=ploads,headers=headers)
            courselist = json.loads(r.text)

            request.session['courselist'] = courselist
            
        except  Exception as inst:
            print("See Error Details Below /n")
            print(inst)
    return render (request,'GradeManager/displayCourse_view.html',{'courselist':courselist})



@login_required
def downloadScoresheet_xls(request,ccode):
  #if request.method=='POST or None':
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Newusers.xls"'
    if request.session.has_key('courselist'):
         courselist = request.session['courselist']
         workbook = openpyxl.Workbook()
         #worksheet = workbook.create_sheet('Sheet1')
         worksheet=workbook.active

         worksheet.protection.sheet = True
         worksheet.protection.enable()
         hashed_password="Akoms"
         workbook.security.set_workbook_password(hashed_password, already_hashed=False)
         worksheet.protection.password = 'Deji'
         
         cell1 = worksheet['G7']

         cell1.value = "Can you change me?"

 
         worksheet.title='SCORESSHEET'
         col_start=0
         row_start=7
         worksheet.cell(row=2, column=2).value = 2
         SECRETKEY={
             "CCODE":"CCS111",
             "TOTAL":"7",
             "EMAIL":"AKOS",
             "CID":"123"
         }
         worksheet.cell(1 ,1).value=json.dumps(SECRETKEY)
         worksheet.cell(1 ,3).value=7
         worksheet.cell(3 ,2).value='THE POLYTECHNIC IBADAN'
         worksheet.cell(4 ,2).value='DEAPRTMENT'
         worksheet.cell(4 ,2).value='COURSE CODE SESSION SEMESTER '
         worksheet.cell(5 ,2).value='COURSE CODE : '+courselist[0]['MYCOURSEID']
        #  worksheet.range("B3", "E3").merge()
        #  worksheet.range("B4", "E4").merge()
        #  worksheet.range("B5", "E5").merge()
        #  worksheet.set_col_style(7, Style(fill=Fill(background=Color(255,0,0,0))))
        #  worksheet.set_cell_style(1, 1, Style(font=Font(bold=True)))
        #  worksheet.set_cell_style(1, 1, Style(font=Font(italic=True)))
        #  worksheet.set_cell_style(1, 1, Style(font=Font(underline=True)))
        #  worksheet.set_cell_style(1, 1, Style(font=Font(strikethrough=True)))
        #  worksheet.set_cell_style(1, 1, Style(fill=Fill(background=Color(255,0,0,0))))
        #  worksheet.set_cell_value(1, 2, datetime.now())
        #  worksheet.set_cell_style(1, 1, Style(format=Format('mm/dd/yy')))
         for index,row in  enumerate(courselist): 
           

             worksheet.cell(index+row_start ,col_start+1).value= index+1
             worksheet.cell(index+row_start ,col_start+2).value= row['MYSTUDENTID']
             worksheet.cell(index+row_start ,col_start+3).value= row['MYSURNAME']
             worksheet.cell(index+row_start ,col_start+4).value= row['MYMIDDLENAME']
             worksheet.cell(index+row_start ,col_start+5 ).value = row['MYFIRSTNAME']
            
             worksheet.cell(index+row_start ,col_start+6).value= row['MYSCORE']
             worksheet.cell(index+row_start ,col_start+6).protection = Protection(locked=False)  
             #Scorecell = worksheet['G8']

             #Scorecell.value = "what about me?"
 
         #cell2.style = Style(protection = Protection(locked=False))
             #cell2.protection = Protection(locked=False)  


         workbook.save(response)
    else:
        print('Nothing was passed in session')

    #wb.save("output.xlsx")
    #wb.save(response)
    return response


@login_required
def  uploadScoresheet_xls(request):
    context={}
    if request.method == 'POST' :
        
        form = UploadedScoreForm(request.POST,request.FILES)
        if form.is_valid():
            
            excel_file = request.FILES['scoresheetfile']
            lists = generatescorelist(excel_file)
            #json_string = json.dumps([ob.__dict__ for ob in lists])
            json_string = [ob.__dict__ for ob in lists]
            
            print(json_string)
  
            myCampId="myCampId"
            myFacId="myCampId"
            myDeptId="myCampId"
            myProgId="myCampId"
            myProgOptionId="myCampId"
            myAsetId="myCampId"
            myAsessionId="myCampId"
            mySemesterId="myCampId"
            myLevelTodo="myCampId"
            myCourseId="myCourseId"
          
            basicunits = basicunit( myCampId,myFacId,myDeptId,myProgId,myProgOptionId,myAsetId,myAsessionId,mySemesterId,myLevelTodo,myCourseId)
            api=settings.BASE_URL+'/api/Student/PythonScore'
            data = MergebasicScorelist(basicunits.__dict__,json_string)
            mydata = json.dumps(data.__dict__)

        try:
            headers = {'content-type': 'application/json'}
            r = requests.post(api,data=mydata,headers=headers)
            print(r)
            if r.status_code==200:
                messages.success(request, str(r.status_code) +"  Successfully Uploaded")
            else:
                messages.error(request,str(r.status_code) +" Problem loading data")
        except  Exception as inst:
            print("See Error Details Below /n")

            messages.error(request,inst)


    else :
        form = UploadedScoreForm()
    context={'form':form}
    return render(request,'GradeManager/uploadScoresheet_xls.html',context)

@login_required
def downloadScoreSheetPdf(request):

    print('Beginning file download with requests')

    #url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
    url='http://192.168.0.111/WebResult.WebApi/api/Student/PythonPullForScoreSheetPdf'
    r = requests.get(url)

    #with open('cat3.jpg', 'wb') as f:
        #f.write(r.content)

        # Retrieve HTTP meta-data
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.encoding)
    
    
    response = HttpResponse(r.content,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Newusers.pdf"'
    return response
    #return HttpResponseNotFound('Nothing Found')