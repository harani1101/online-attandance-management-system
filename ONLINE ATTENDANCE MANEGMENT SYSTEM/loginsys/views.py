from django.shortcuts import render
from django.contrib.auth.models import User,auth
from loginsys.models import Newuser
from django.contrib import messages
from loginsys.models import Newhuser
from loginsys.models import Meet
from loginsys.models import Meetreg
from loginsys.models import chkbox
from loginsys.models import check
from django.db  import connection
from loginsys.models import Query
from django.core.mail import send_mail
import re
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


def tablesjoin(request):
    cursor=connection.cursor()
    cursor.execute("select loginsys_chkbox.id,loginsys_chkbox.meet_code,loginsys_check.username from loginsys_chkbox join loginsys_check on loginsys_chkbox.id=loginsys_check.id")
    result=cursor.fetchall()
    displaydata=Meet.objects.all()
    return render(request,'attendance.html',{'dis':result,"data2":displaydata})

def firstpage(request):
    #if (user.is_authenticated):
        #return render(request,'meettable1.html')
    #else:
    return render(request,'first.html')
def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    if request.method=='POST':
         name=request.POST['name']
         email=request.POST['email']
         message=request.POST['message']
         Query(name=name,email=email,message=message).save()
         messages.success(request,request.POST['name']+" , your query has been successfully posted..please wait for your answer.")
         subject='QUERY ALERT !!'
         message=request.POST['message']
         sendfrom='settings.EMAIL_HOST_USER'
         toaddress=[request.POST['email'],'attendancemanagementsystem4@gmail.com']
         send_mail(subject,message,sendfrom,toaddress)
         return render(request,'contactus.html')
    else:
        return render(request,'contactus.html')
    return render(request,'contactus.html')

def userreg(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        if User.objects.filter(username=username).exists():
            messages.info(request,'user already registered')
            return render(request,'registration.html')
        user=User.objects.create_user(username=username,password=password1,first_name=first_name,email=email,last_name=last_name)
        user.save()
        Newuser(first_name=first_name,last_name=last_name,username=username,email=email,password1=password1).save()
        messages.success(request," HI "+request.POST['first_name']+ " !! you are successfully registered. Please enter your correct credentials to login into the page ")
        subject='sign up verification for OAMS '
        message="Verfication and alert mail..  Hi user You have been successfully registered in the online attendence management system. Please use your correct credentials to login into the website"
        sendfrom='settings.EMAIL_HOST_USER'
        toaddress=[request.POST['email']]#['attendancemanagementsystem4@gmail.com']
        send_mail(subject,message,sendfrom,toaddress)
        return render(request,'registration.html')
    else:
        return render(request,'registration.html')

def loginpage(request):
    if request.method =='POST':
        try:
            userdetails=Newuser.objects.get(username=request.POST['username'],password1=request.POST['password1'])
            print("username=",userdetails)
            request.session['username']=userdetails.username
            return render(request,'meettable.html')
        except Newuser.DoesNotExist as e:
            messages.success(request,'username/password invalid...')
    return render(request,'login.html')
def logout(request):
    try:
       del request.session['username']
    except:
       return render(request,'first.html')
    #auth.logout(request)
    return render(request,'first.html')

def userreg1(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Already registered as user')
            return render(request,'registration1.html')
        user=User.objects.create_user(username=username,password=password1,first_name=first_name,email=email,last_name=last_name)
        user.save()
        Newhuser(first_name=first_name,last_name=last_name,username=username,email=email,password1=password1).save()
        messages.success(request," Hello "+request.POST['first_name']+ " !! you are successfully registered. Please enter your correct credentials to login into the page ")
        subject='SIGN UP VERIFICATION FOR OAMS '
        message="Verfication and alert mail..  Hi user You have been successfully registered in the online attendence management system. Please use your correct credentials to login into the website"
        sendfrom='settings.EMAIL_HOST_USER'
        toaddress=[request.POST['email']]#['attendancemanagementsystem4@gmail.com']
        send_mail(subject,message,sendfrom,toaddress)
        return render(request,'registration1.html')
    else:
        return render(request,'registration1.html')

def loginpage1(request):
    if request.method =='POST':
        try:
            username=request.POST.get('username',False)
            password1=request.POST.get('password1',False)
            user = auth.authenticate(username=username,password=password1)
            userdetails=Newhuser.objects.get(username=request.POST['username'],password1=request.POST['password1'])
            print("username=",userdetails)
            request.session['username']=userdetails.username
            return render(request,'meettable1.html')
        except Newhuser.DoesNotExist as e:
            messages.success(request,'username/password invalid...')
    return render(request,'login1.html')
def logout1(request):
    try:
       del request.session['username']
    except:
        return render(request,'first.html')
    #auth.logout(request)
    return render(request,'first.html')

def meetdet1(request):
    if request.method =='POST':
        meet_name=request.POST['meet_name']
        timedate=request.POST['timedate']
        meet_code=request.POST['meet_code']
        Meet(meet_name=meet_name,timedate=timedate,meet_code=meet_code).save()
        messages.success(request,"The New Meeting "+request.POST['meet_name']+ " have been saved successfully")
        return render(request,'meetdet1.html')
    else:
        return render(request,'meetdet1.html')

def showresults1(request):
    displaydata=Meet.objects.all()
    return render(request,'meettable1.html',{"data1":displaydata})

def showresults(request):
    displaydata=Meet.objects.all()
    return render(request,'meettable.html',{"data":displaydata})

#def showresults2(request):
 #   displaydata=Meet.objects.all()
  #  return render(request,'attendance.html',{"data2":displaydata})

def usermeetreg(request):
    regex1="([6-9]{1}[0-9]{9})"
    q=re.compile(regex1)
    if request.method =='POST':
            name=request.POST['name']
            email=request.POST['email']
            contact_number=request.POST['contact_number']
            college_name=request.POST['college_name']
            city=request.POST['city']
            meet_code=request.POST['meet_code']
            if re.search(q,contact_number):
                Meetreg(name=name,email=email,contact_number=contact_number,college_name=college_name,city=city,meet_code=meet_code).save()
                messages.success(request,request.POST['name']+ " have successfully registered for the meeting ")
                return render(request,'meetregister.html')
            else:
                messages.info(request,'invalid contact number!')
                return render(request,'meetregister.html')
    else:
        return render(request,'meetregister.html')
def usermeetreg1(request):
    regex1="([6-9]{1}[0-9]{9})"
    q=re.compile(regex1)
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        contact_number=request.POST['contact_number']
        college_name=request.POST['college_name']
        city=request.POST['city']
        meet_code=request.POST['meet_code']
        if re.search(q,contact_number):
            Meetreg(name=name,email=email,contact_number=contact_number,college_name=college_name,city=city,meet_code=meet_code).save()
            messages.success(request,request.POST['name']+ " have successfully registered for the meeting ")
            return render(request,'addparticipant1.html')
        else:
            messages.info(request,'invalid contact number!')
            return render(request,'addparticipant1.html')
    else:
        return render(request,'addparticipant1.html')

def viw(request):
    if request.method =='POST':
        meet_code=request.POST.get('meet_code')
        #chkbox(meetname1=meetname1,schedule=schedule).save()
        meetsearchobj=Meetreg.objects.raw('SELECT * FROM loginsys_meetreg WHERE meet_code="'+meet_code+'"')
        return render(request,'viw1.html',{"result":meetsearchobj})
    else:
        meetobj=Meetreg.objects.raw('select * from loginsys_meetreg')
        return render(request,'viw1.html',{"result":meetobj})
def viewmem(request):
    x=chkbox.objects.last()
    print(x)
    messages.info(request,'Mark attendance for '+str(x))
    if request.method == 'POST':
        if  request.POST.get('username'):
            saverecord=check()
            saverecord.username=request.POST.get('username')
            saverecord.save()
            return render(request,'viewmember1.html')
        meet_code=request.POST.get('meet_code')
        chkbox(meet_code=meet_code).save()
        meetsearchobj=Meetreg.objects.raw('SELECT * FROM loginsys_meetreg WHERE meet_code="'+meet_code+'"')
        return render(request,'viewmember1.html',{"result":meetsearchobj})
    else:
        meetobj=Meetreg.objects.raw('select * from loginsys_meetreg')
        return render(request,'viewmember1.html',{"result":meetobj})

def profile(request,pk=None):
    obs= User.objects.all()
    '''if pk:
        user=User.objects.get(pk=pk)'''
    if request.method == "POST":
        user=request.user
        un=request.POST["username"]
        fn = request.POST["first_name"]
        ln = request.POST["last_name"]
        e = request.POST["email"]
        print(e)
        ll= request.POST["last_login"]
        dj=request.POST["date_joined"]
        ul1=user.request.POST["UploadLink"]
        print(ul1)
        obs =user(username=un,first_name=fn,last_name=ln,email=e,last_login=ll,date_joined=dj,UploadLink=ul1)
        obs.save()
    sample={'obs':obs}
    return render(request, "profile.html",sample)


  
        

    
