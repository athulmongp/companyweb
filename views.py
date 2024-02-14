from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import*
from django.contrib.auth.decorators import login_required 
from django.conf import settings
from django.core.mail import send_mail
from random import randrange
import datetime

# admin home

def adminhomepage(request):
    trainer=TrainerRegModel.objects.filter()
    trainee=RegisterModel.objects.filter(Action=1)
    n=RegisterModel.objects.filter(Action=0)
    section=SetTrainingModel.objects.filter()
    noti=len(n)

    i=TrIssueModel.objects.filter(Action=0)
    issue=len(i)
    
    return render(request,'adminhome.html',{'trainer':trainer,'trainee':trainee,'noti':noti,'section':section,'issue':issue} )

# trainee home

def homepage(request):
    current_user=request.user
    uid=current_user.id
    t1=RegisterModel.objects.get(user=uid)
    data=RegisterModel.objects.get(user=uid)
    if SetTrainingModel.objects.filter(Trainee=t1):
        data1=SetTrainingModel.objects.filter(Trainee=t1, ActionTe=0)
        d5=TeIssueModel.objects.filter(TeAction=0,Action=1,Trainee=t1)
        noti=len(data1)+len(d5)
        d1=SetTrainingModel.objects.get(Trainee=data.id)
        d2=d1.Trainer.id
    
        d3=TaskModel.objects.filter(Trainee=t1,Action=0)
        d4=TopicModel.objects.filter(Trainer=d2, Action=0)

        return render(request,'home.html',{'data':data,'noti':noti,'d3':d3,'d4':d4})
    else:
        messages.error(request,'please wait, admin is set your training')

        return redirect('log')

# trainerhome

def thomepage(request):
    current_user=request.user
    uid=current_user.id
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data )
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    task=SubmitTaskModel.objects.filter(Trainer=data,Action=0)

    topic=TopicModel.objects.filter(Trainer=data,Action=0)
    return render(request,'thome.html',{'data':data,'noti':noti,'task':task,'topic':topic})

def topicok(request,did):
    data=TopicModel.objects.filter(id=did).update(Action=1)
    return redirect('thomepage')

def submittaskok(request,did):
    d=SubmitTaskModel.objects.get(id=did)
    d1=d.Task.id
    data=TaskModel.objects.filter(id=d1).update(Action=1)
    data1=SubmitTaskModel.objects.filter(id=did).update(Action=1)
    
    return redirect('thomepage')

def triok(request,did):
    data=TrIssueModel.objects.filter(id=did).update(TrAction=1)
    return redirect('thomepage')

def teiok(request,did):
    data=TeIssueModel.objects.filter(id=did).update(TeAction=1)
    return redirect('homepage')
# trainee registration

def regpage(request):
    data=CourseModel.objects.all()
    return render(request,'reg.html',{'data':data})

def registration(request):
    if request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        email=request.POST['eid']
        usname=request.POST['uname']
        num=request.POST['ph']
        # pswd=request.POST['pass']
        # cpswd=request.POST['cpass']
       
        
        co=request.POST.get('subselect')
        course=CourseModel.objects.get(id=co)

        # pos=request.POST['position']
       
        img=request.FILES.get('image')
        c=request.FILES.get('certificate')
        

        
        if User.objects.filter(username=usname).exists():
            print("1")
            return redirect('regpage')
        elif User.objects.filter(email=email).exists():
            print("2")
            return redirect('regpage')
        else:
            user=User.objects.create_user(first_name=fn,last_name=ln,email=email,username=usname)
            user.save()
            data=User.objects.get(id=user.id)
            customer=RegisterModel(number=num,img=img,user=data,Certificate=c,Course=course)
            customer.save()
            print("success")
            return redirect('log')

        

    else:
            print(" error")
            return redirect('regpage')


# admin add trainer and send mail

def trainerreg(request):
    data=CourseModel.objects.all()
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,"regtrainer.html",{'data':data,'noti':noti})

def tregistration(request):
    if request.method=='POST':
        fn=request.POST['fname']
        ln=request.POST['lname']
        email=request.POST['eid']
        usname=request.POST['uname']
        num=request.POST['ph']
        # pswd=request.POST['pass']
        # cpswd=request.POST['cpass']
       
        
        co=request.POST.get('subselect')
        course=CourseModel.objects.get(id=co)

        # pos=request.POST['position']
       
        img=request.FILES.get('image')
        # c=request.FILES.get('certificate')
        

        
        if User.objects.filter(username=usname).exists():
            print("1")
            return redirect('trainerreg')
        elif User.objects.filter(email=email).exists():
            print("2")
            return redirect('trainerreg')
        else:
            user=User.objects.create_user(first_name=fn,last_name=ln,email=email,username=usname)
            user.save()
            data=User.objects.get(id=user.id)
            customer=TrainerRegModel(number=num,img=img,user=data,Course=course)
            customer.save()
            print("success")

            em=TrainerRegModel.objects.get(user=user.id)
            username=em.user.username
            mail=em.user.email
            password=randrange(100000,1000000)
            print(password)
            p=em.user.id
            pa=str(password)
            print(pa)
            data=User.objects.get(id=p)
            data.set_password(pa)
            data.save()
    
    

            subject = 'Registeration'
            message = 'Registration is successfully complited!!!!'+' ' +' '+' '+'userid : '+username+' '+' '+' ' +',password :  '+str(password)
              

            recipient =mail  #  recipient =request.POST["inputTagName"]
            send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient])
            messages.success(request, 'add the trainer')
            return redirect('adminhomepage')
        

        

    else:
            print(" error")
            messages.error(request, 'error')
            return redirect('trainerreg')

# log in section   

def log(request):
    return render(request,'login.html')
def loginpage(request):
    if request.method=='POST':
        username = request.POST['ui']
        password = request.POST['pa']
        
        user= auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            if request.user.is_staff==1:
                print("admin")
       
                return redirect('adminhomepage')
                 
            else:
              current_user=request.user
              uid=current_user.id
              if RegisterModel.objects.filter(user=uid).exists():
                  return redirect('homepage')
              elif TrainerRegModel.objects.filter(user=uid).exists():
                  return redirect('thomepage')
              else:
                return redirect('log')
                  
              
        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            print("try again")
            return redirect('log')
    else:
        messages.error(request,'Invalid')
        print("try again")
        return redirect('log')
    
# admin approve and mail send   

def waitpage(request):
    return render(request,'wait.html')
def approve(request,uid):
    data=RegisterModel.objects.filter(id=uid).update(Action=1)
    em=RegisterModel.objects.get(id=uid)
    username=em.user.username
    mail=em.user.email
    name=em.user.first_name
    password=randrange(100000,1000000)
    print(password)
    p=em.user.id
    pa=str(password)
    print(pa)
    data=User.objects.get(id=p)
    data.set_password(pa)
    data.save()
    
    
    

    subject = 'Registeration'
    message = f'Hi {name},\n Registration is successfully complited!!!! \n  userid : {username} \n password :  {str(password)}'
              

    recipient =mail  #  recipient =request.POST["inputTagName"]
    send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient])
    return redirect('adminhomepage')

def regreject(request,did):
   
    data1=RegisterModel.objects.get(id=did)
    mail=data1.user.email
    name=data1.user.first_name
    subject = 'Registration'
    message =f'Hi {name},\n your Application is rejected'
    recipient =mail  #  recipient =request.POST["inputTagName"]
    send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient])
    
    em=RegisterModel.objects.get(id=did)
    em.user.delete()
    em.delete()
    return redirect('adminhomepage')

#  admin add coursepage

def coursepage(request):
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,'course.html',{'noti':noti})
def addcourse(request):
     if request.method == 'POST':
        Course=request.POST['course']
        data = CourseModel(Course_Name=Course)
        data.save()
        messages.success(request,"successfully added")
        return redirect('coursepage')

# admin notification

def anoti(request):
    data=RegisterModel.objects.filter(Action=0)
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,'anotification.html',{'data':data,'noti':noti})

# admin view feedback

def viewfeedbackpage(request):
    return render(request,'viewfeedback.html')

# trainer task section
def taskpage(request):
    current_user=request.user
    uid=current_user.id
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data )
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    return render(request,'task.html',{'data':data,'noti':noti})
def addtaskpage(request):
    current_user=request.user
    uid=current_user.id
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data, ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data )
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l

    trainee=RegisterModel.objects.all()
  
    
    return render(request,'addtask.html',{'data':data,'noti':noti,'trainee':trainee})

def addtask(request):
    if request.method == 'POST':
        subject=request.POST['sub']
        enddate=request.POST['end']
        select=request.POST['select']
        current_user=request.user
        uid=current_user.id
        trainer=TrainerRegModel.objects.get(user=uid)
        trainee=RegisterModel.objects.get(id=select)

        data = TaskModel(Trainer=trainer,Trainee=trainee,Subject=subject,End_Date=enddate)
        data.save()
        print("set")
        messages.success(request,'Task is added')
        return redirect('addtaskpage')
    return redirect('thomepage')

def pretaskpage(request):
    current_user=request.user
    uid=current_user.id
    trainer=TrainerRegModel.objects.get(user=uid)
    task=TaskModel.objects.filter(Trainer=trainer.id)

    
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data )
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=trainer,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l

    return render(request,'pretask.html',{'task':task,'data':data,'noti':noti})

def submittask(request,did):
    task=TaskModel.objects.get(id=did)

    return render(request,"submittask.html",{'task':task})
def uploadtask(request,did):
    current_user=request.user
    uid=current_user.id
    trainee=RegisterModel.objects.get(user=uid)
    task=TaskModel.objects.get(id=did)
    video=request.FILES.get('file')

    data=SubmitTaskModel(Trainer=task.Trainer,Trainee=trainee,Task=task,work=video)
    data.save()
    return redirect('homepage')


def viewtask(request,did):
    current_user=request.user
    uid=current_user.id
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data )
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    task=SubmitTaskModel.objects.filter(id=did)
    return render(request,'viewtask.html',{'task':task,'data':data,'noti':noti})


def teviewtask(request):
    current_user=request.user
    uid=current_user.id
    data=RegisterModel.objects.get(user=uid)
    task=SubmitTaskModel.objects.filter(Trainee=data.id)

    
    t1=RegisterModel.objects.get(user=uid)
    
    data1=SetTrainingModel.objects.filter(Trainee=t1, ActionTe=0)
    d5=TeIssueModel.objects.filter(TeAction=0,Action=1,Trainee=t1)
    noti=len(data1)+len(d5)
    return render(request,"teviewtask.html",{'data':data,'task':task,'noti':noti})

# trainer topic section

def topicpage(request):
    current_user=request.user
    uid=current_user.id
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data )
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    return render(request,'topic.html',{'data':data,'noti':noti})

def addtopicpage(request):
    current_user=request.user
    uid=current_user.id
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data )
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l

   
    return render(request,'addtopic.html',{'data':data,'noti':noti})
def addtopic(request):
    if request.method == 'POST':
        subject=request.POST['topic']
        Date=request.POST['date']
        
        current_user=request.user
        uid=current_user.id
        trainer=TrainerRegModel.objects.get(user=uid)

        data = TopicModel(Trainer=trainer, Topic=subject,End_Date=Date)
        data.save()
        print("set")
        messages.success(request,'Topic is added')
        return redirect('addtopicpage')
    return redirect('thomepage')
def pretopicpage(request):
    current_user=request.user
    uid=current_user.id
    trainer=TrainerRegModel.objects.get(user=uid)
    topic=TopicModel.objects.filter(Trainer=trainer.id)

    
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data)
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=trainer,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l

    return render(request,'pretopic.html',{'topic':topic,'data':data,'noti':noti})

def teviewtopic(request):
    current_user=request.user
    uid=current_user.id
    data=RegisterModel.objects.get(user=uid)
    t=SetTrainingModel.objects.get(Trainee=data.id)
    task=TopicModel.objects.filter(Trainer=t.Trainer)

    
    t1=RegisterModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainee=t1, ActionTe=0)
    d5=TeIssueModel.objects.filter(TeAction=0,Action=1,Trainee=t1)
    noti=len(data1)+len(d5)
    return render(request,"teviewtopic.html",{'data':data,'task':task,'noti':noti})

# add trainer feedback

def maintrfbpage(request):
    current_user=request.user
    uid=current_user.id
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    print(d1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data)
    d2=len(data2)
    print(d2)
    leave=TeleaveModel.objects.filter(Trainer=data,Action=1,ActionTr=0)
    l=len(leave)
    print(l)
    noti=d1+d2+l
    return render(request,'trfbpage.html',{'data':data,'noti':noti})

def trainerfbpage(request):
    current_user=request.user
    uid=current_user.id
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data)
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    return render(request,'trainerfb.html',{'data':data,'noti':noti})
def addtrainerfb(request):
    if request.method == 'POST':
        feedback=request.POST['fb']
        
        current_user=request.user
        uid=current_user.id
        trainer=TrainerRegModel.objects.get(user=uid)

        data = TrFeedBackModel(Trainer=trainer, Feedback=feedback)
        data.save()
        print("set")
        messages.success(request,'feedback is added')
        return redirect('trainerfbpage')
    return redirect('thomepage')

def trviewfb(request):
    current_user=request.user
    uid=current_user.id
    trainer=TrainerRegModel.objects.get(user=uid)
    tefb=TeFeedBackModel.objects.filter(Trainer=trainer.id)

    
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data)
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=trainer,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    return render(request,'trfbview.html',{'tefb':tefb,'data':data,'noti':noti})

# add trainee feedback

def traineefbpage(request):
    data=TrainerRegModel.objects.all()

    current_user=request.user
    uid=current_user.id
    t1=RegisterModel.objects.get(user=uid)
    data6=RegisterModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainee=t1, ActionTe=0)
    d5=TeIssueModel.objects.filter(TeAction=0,Action=1,Trainee=t1)
    noti=len(data1)+len(d5)
    return render(request,'tefeedback.html',{'data':data,'noti':noti,'data6':data6})
def addtraineefb(request):
    if request.method == 'POST':
        feedback=request.POST['fb']
        
        current_user=request.user
        uid=current_user.id
        trainee=RegisterModel.objects.get(user=uid)
        trainer=SetTrainingModel.objects.get(Trainee=trainee.id)
        t=trainer.Trainer

        data = TeFeedBackModel(Trainee=trainee,Trainer=t,Feedback=feedback)
        data.save()
        print("set")
        messages.info(request, 'Feedback Added')
        return redirect('traineefbpage')
    return redirect('homepage')




# set training coursepage

def setcoursepage(request):
    data=CourseModel.objects.all()
    n=RegisterModel.objects.filter(Action=0)
    
    noti=len(n)
    return render(request,'setcourse.html',{'data':data,'noti':noti})
def copage(request):
    course=request.POST['Course']
    cid=CourseModel.objects.filter(id=course)
    return redirect('settraining',course)
    

def settraining(request,cid):
    
    trainer=TrainerRegModel.objects.filter(Course=cid)
    trainee=RegisterModel.objects.filter(Course=cid)
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,'settraining.html',{'trainer':trainer,'trainee':trainee,'noti':noti})

def addtrainingsection(request):
    if request.method == 'POST':
        trainer=request.POST['trainer']
        trainee=request.POST['trainee']

        t1=TrainerRegModel.objects.get(id=trainer)
        t2=RegisterModel.objects.get(id=trainee)
        data=SetTrainingModel(Trainer=t1,Trainee=t2)
        data.save()
        messages.success(request,'Successfully set the training')
        return redirect('setcoursepage')
    
# trainer notification

def trnoti(request):
    current_user=request.user
    uid=current_user.id
    t1=TrainerRegModel.objects.get(user=uid)
    

    
    leave=TeleaveModel.objects.filter(Trainer=t1,Action=1,ActionTr=0)
    l=len(leave)

    data1=SetTrainingModel.objects.filter(Trainer=t1 , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=t1 )
    d2=len(data2)
    noti=d1+d2+l
    data=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=t1.id)
    
    return render(request,'trnotification.html',{'data1':data1,'data':data,'noti':noti,'t1':t1,'leave':leave})  
  
def teleaveok(request,did):
    data=TeleaveModel.objects.filter(id=did).update(ActionTr=1)
    return redirect('trnoti')

def ok(request,uid):
    data=SetTrainingModel.objects.filter(Trainer=uid).update(ActionTr=1)
    return redirect('trnoti')

# trainee notification

def tenoti(request):
    current_user=request.user
    uid=current_user.id
    t1=RegisterModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainee=t1, ActionTe=0)

    data=TeIssueModel.objects.filter(TeAction=0,Action=1,Trainee=t1)

    current_user=request.user
    uid=current_user.id
    t1=RegisterModel.objects.get(user=uid)
    data2=RegisterModel.objects.get(user=uid)
    data3=SetTrainingModel.objects.filter(Trainee=t1, ActionTe=0)
    d5=TeIssueModel.objects.filter(TeAction=0,Action=1,Trainee=t1)
    noti=len(data3)+len(d5)
    
    return render(request,'tenotification.html',{'data1':data1,'data':data,'data2':data2,'noti':noti})    

def teok(request,uid):
    data=SetTrainingModel.objects.filter(Trainee=uid).update(ActionTe=1)
    return redirect('tenoti')

# admin feedbackview

def afbview(request):
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,'afbview.html',{'noti':noti})
def atrfbview(request):
    data= TrFeedBackModel.objects.all()
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,'atrfbview.html',{'data':data,'noti':noti})

def atefbview(request):
    data= TeFeedBackModel.objects.all()
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,'atefbview.html',{'data':data,'noti':noti})

# trainee report issue
def teissuepage(request):
    current_user=request.user
    uid=current_user.id
    print(uid)
    data=RegisterModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainee=data, ActionTe=0)
    d1=len(data1)
    data2=TeIssueModel.objects.filter(TeAction=0,Action=1,Trainee=data)
    d2=len(data2)
    noti=d1+d2
    return render(request,'teissue.html',{'data':data,'noti':noti})

def addteissue(request):
    issue=request.POST['issue']
    current_user=request.user
    uid=current_user.id
    t1=RegisterModel.objects.get(user=uid)
    data=TeIssueModel(Trainee=t1,Issue=issue)
    data.save()
    messages.info(request, 'Send to admin')
    return redirect('teissuepage')

# trainer report issue
def trissuepage(request):
    current_user=request.user
    uid=current_user.id
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data)
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    return render(request,'trissue.html',{'data':data,'noti':noti})

def addtrissue(request):
    issue=request.POST['issue']
    current_user=request.user
    uid=current_user.id
    t1=TrainerRegModel.objects.get(user=uid)
    data=TrIssueModel(Trainer=t1,Issue=issue)
    data.save()
    messages.success(request,'successfully send the request')
    return redirect('trissuepage')

# admin view issues
def aviewissue(request):
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,'aviewissue.html',{'noti':noti})

def aviewtrissue(request):
    data=TrIssueModel.objects.filter(Action=0)
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,'aviewtrissue.html',{'data':data,'noti':noti})
def aviewteissue(request):
    data=TeIssueModel.objects.filter(Action=0)
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,'aviewteissue.html',{'data':data,'noti':noti})
# admin reply trainer issue
def replytrissue(request,did):
    data=TrIssueModel.objects.get(id=did)
    return render(request,'atrreply.html',{'data':data})
def sendreplytr(request,did):
    reply=request.POST['replay']
    data=TrIssueModel.objects.get(id=did)
    
    data.Replay=reply
    data.save()
    data1=TrIssueModel.objects.filter(id=did).update(Action=1)
    print('send reply')
    return redirect('aviewtrissue')

# admin reply trainee issue
def replyteissue(request,did):
    data=TeIssueModel.objects.get(id=did)
    
    return render(request,'atereply.html',{'data':data})
def sendreplyte(request,did):
    reply=request.POST['replay']
    data=TeIssueModel.objects.get(id=did)
    
    data.Replay=reply
    data.save()
    data1=TeIssueModel.objects.filter(id=did).update(Action=1)
    print('send reply')
    return redirect('aviewtrissue')

# trainer attendance section
def trattendancepage(request):
    current_user=request.user
    uid=current_user.id
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data)
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    return render(request,"trattendance.html",{'data':data,'noti':noti})

def trgiveattendance(request):
    current_user=request.user
    uid=current_user.id
    data3=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data3, ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data3)
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data3,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    t1=TrainerRegModel.objects.get(user=uid)
    data=SetTrainingModel.objects.filter(Trainer=t1.id)

    return render(request,"trgiveattendance.html",{'data':data,'data3':data3,'noti':noti})

def addteattendance(request):
    t=request.POST['trainee']
    attendance=request.POST['Attendance']
    current_user=request.user
    uid=current_user.id
    trainer=TrainerRegModel.objects.get(user=uid)
    trainee=RegisterModel.objects.get(id=t)
    data=TeAttendance(Trainer=trainer,Trainee=trainee,Attendance=attendance)
    data.save()
    messages.success(request, 'Added')
    return redirect('trgiveattendance')

def viewteattendance(request):
    current_user=request.user
    uid=current_user.id
    print(uid)
    data3=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data3, ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data3)
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data3,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    trainer=TrainerRegModel.objects.get(user=uid)
    data=TeAttendance.objects.filter(Trainer=trainer.id)
    if request.method=="POST":
        start=request.POST['start']
        End=request.POST['end']
        data4=TeAttendance.objects.filter(Trainer=trainer,Date__range=[start,End])
        return render(request,"viewteattendance.html",{'data4':data4,'data':data,'data3':data3,'noti':noti})
    return render(request,"viewteattendance.html",{'data':data,'data3':data3,'noti':noti})
def trownattendance(request):
    current_user=request.user
    uid=current_user.id
    print(uid)
    data3=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data3, ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data3)
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data3,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    trainer=TrainerRegModel.objects.get(user=uid)
    data=TrainerRegModel.objects.get(user=uid)
    if request.method=="POST":
        start=request.POST['start']
        End=request.POST['end']
        data4=TrAttendance.objects.filter(Trainer=trainer,Date__range=[start,End])
        return render(request,"trownattendance.html",{'data4':data4,'data':data,'data3':data3,'noti':noti})
    return render(request,"trownattendance.html",{'data':data,'data3':data3,'noti':noti})
# view trainee own attendance
def teviewattendance(request):
    current_user=request.user
    uid=current_user.id
    print(uid)
    data=RegisterModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainee=data, ActionTe=0)
    d1=len(data1)
    data2=TeIssueModel.objects.filter(TeAction=0,Action=1,Trainee=data)
    d2=len(data2)
   
    noti=d1+d2
    
    if request.method=="POST":
        start=request.POST['start']
        End=request.POST['end']
        att=TeAttendance.objects.filter(Trainee=data,Date__range=[start,End])
        return render(request,"teviewattendance.html",{'data':data,'noti':noti,'att':att})
    return render(request,"teviewattendance.html",{'data':data,'noti':noti})


# trainer request leave
def trleave(request):
    current_user=request.user
    uid=current_user.id
    data=TrainerRegModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainer=data , ActionTr=0)
    d1=len(data1)
    data2=TrIssueModel.objects.filter(TrAction=0,Action=1,Trainer=data)
    d2=len(data2)
    leave=TeleaveModel.objects.filter(Trainer=data,Action=1,ActionTr=0)
    l=len(leave)
    noti=d1+d2+l
    return render(request,"trleave.html",{'data':data,'noti':noti})

def addtrleave(request):
    date=request.POST['date']
    reason=request.POST['reason']
    current_user=request.user
    uid=current_user.id
    print(uid)
    trainer=TrainerRegModel.objects.get(user=uid)

    data=TrleaveModel(Trainer=trainer,Date=date,Reason=reason)
    data.save()
    messages.success(request,'Task is added')
    return redirect('trleave')
# trainee request leave
def teleave(request):
    current_user=request.user
    uid=current_user.id
    print(uid)
    data=RegisterModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainee=data, ActionTe=0)
    d1=len(data1)
    data2=TeIssueModel.objects.filter(TeAction=0,Action=1,Trainee=data)
    d2=len(data2)
    noti=d1+d2
    return render(request,"teleave.html",{'data':data,'noti':noti})

def addteleave(request):
    date=request.POST['date']
    reason=request.POST['reason']
    current_user=request.user
    uid=current_user.id
    print(uid)
    trainee=RegisterModel.objects.get(user=uid)
    trainer= SetTrainingModel.objects.get(Trainee=trainee)

    data=TeleaveModel(Trainee=trainee,Trainer=trainer.Trainer,Date=date,Reason=reason)
    data.save()
    messages.info(request, 'Send to admin')
    return redirect('teleave')

def aviewleave(request):
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,"aviewleave.html",{'noti':noti})

def aviewtrleave(request):
    data1=TrleaveModel.objects.filter(Action=0)
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,"aviewtrleave.html",{'data1':data1,'noti':noti})
def aviewteleave(request):
    data=TeleaveModel.objects.filter(Action=0)
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,"aviewteleave.html",{'data':data,'noti':noti})

def trleaveaccept(request,did):
    data=TrleaveModel.objects.filter(id=did).update(Action=1)
   
    data1=TrleaveModel.objects.get(id=did)
    mail=data1.Trainer.user.email
    name=data1.Trainer.user.first_name
    subject = 'Leave'
    message =f'Hi {name},\n your leave is approved'
              

    recipient =mail  #  recipient =request.POST["inputTagName"]
    send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient])
    return redirect('aviewleave')

def trleavereject(request,did):
    data=TrleaveModel.objects.filter(id=did).update(Action=1)
   
    data1=TrleaveModel.objects.get(id=did)
    mail=data1.Trainer.user.email
    name=data1.Trainer.user.first_name
    subject = 'Leave'
    message =f'Hi {name},\n your leave is rejected'
              

    recipient =mail  #  recipient =request.POST["inputTagName"]
    send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient])
    return redirect('aviewleave')


def teleaveaccept(request,did):
    data=TeleaveModel.objects.filter(id=did).update(Action=1)
   
    data1=TeleaveModel.objects.get(id=did)
    mail=data1.Trainee.user.email
    name=data1.Trainee.user.first_name
    subject = 'Leave'
    message =f'Hi {name},\n your leave is approved'
              

    recipient =mail  #  recipient =request.POST["inputTagName"]
    send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient])
    return redirect('aviewleave')

def teleavereject(request,did):
    data=TeleaveModel.objects.filter(id=did).update(Action=1)
   
    data1=TeleaveModel.objects.get(id=did)
    mail=data1.Trainee.user.email
    name=data1.Trainee.user.first_name
    subject = 'Leave'
    message =f'Hi {name},\n your leave is rejected'
              

    recipient =mail  #  recipient =request.POST["inputTagName"]
    send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recipient])
    return redirect('aviewleave')
def aedittrainerpage(request,did):
    data=TrainerRegModel.objects.get(id=did)
    co=CourseModel.objects.all()
    return render(request,"aedittrainer.html",{'data':data,'co':co})

def aedittrainer(request,did):
    if request.method=='POST':
        data=TrainerRegModel.objects.get(id=did)
        # data.img=request.FILES.get('image')
        old=data.img
        new=request.FILES.get('image')
        if old!=None and new==None:
            data.img=old
        else:
            data.img=new
        data.user.first_name=request.POST.get('fname')
        data.user.last_name=request.POST.get('lname')
        data.user.email=request.POST.get('eid')
        data.user.username=request.POST.get('uname')
        data.number=request.POST.get('ph')
        c=request.POST.get('course')

        course=CourseModel.objects.get(id=c)
        data.Course=course
        data.save()
        data.user.save()
        print("updated")
        return redirect('adminhomepage')
    return render(request,"aedittrainer.html",did)

def removetrainer(request,did):
    data=TrainerRegModel.objects.get(id=did)
    st=SetTrainingModel.objects.get(Trainer=did)
    st.delete()
    data.user.delete()
    data.delete()
    
    return redirect('adminhomepage')

def removetrainee(request,did):
    data=RegisterModel.objects.get(id=did)
    st=SetTrainingModel.objects.get(Trainee=did)
    st.delete()
    data.user.delete()
    data.delete()
    
    return redirect('adminhomepage')

def forgotpass(request):
    current_user=request.user
    uid=current_user.id
    t1=RegisterModel.objects.get(user=uid)
    data=RegisterModel.objects.get(user=uid)
    data1=SetTrainingModel.objects.filter(Trainee=t1, ActionTe=0)
    d5=TeIssueModel.objects.filter(TeAction=0,Action=1,Trainee=t1)
    noti=len(data1)+len(d5)
    return render(request,"forgotpassword.html",{'data':data,'noti':noti})

def setforgotpass(request):
    current_user=request.user
    uid=current_user.id
    t1=RegisterModel.objects.get(user=uid)
    if request.method=='POST':
        username=request.POST['op']
        newpass=request.POST['np']
        
        if t1.user.username==username:
            
            data=User.objects.get(id=t1.user.id)
            data.set_password(newpass)
            data.save()
            print("success")
            messages.info(request, 'password is changed')
            return redirect('log')
        else:
            print('wrong')
            return redirect('forgotpass')

    
    return redirect('forgotpass')



# adimin view attendance
def aviewattendance(request):
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    return render(request,"aviewattendance.html",{'noti':noti})

def agivetrattendance(request):
    data=TrainerRegModel.objects.all()
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    
    return render(request,"agivetrattendance.html",{'data':data,'noti':noti})
def addtrattendance(request):
    t=request.POST['trainer']
    attendance=request.POST['Attendance']
    trainer=TrainerRegModel.objects.get(id=t)

    data=TrAttendance(Trainer=trainer,Attendance=attendance)
    data.save()
    messages.success(request,'Added Attendance')
    return redirect('agivetrattendance')



def viewtrattendance(request):
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    if request.method=="POST":
        start=request.POST['start']
        End=request.POST['end']
        data=TrAttendance.objects.filter(Date__range=[start,End])
        
        
        return render(request,"viewtrattendance.html",{'data':data,'noti':noti})
    return render(request,"viewtrattendance.html",{'noti':noti})
def aviewteattendance(request):
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    if request.method=="POST":
        start=request.POST['start']
        End=request.POST['end']
        data=TeAttendance.objects.filter(Date__range=[start,End])
        
        return render(request,"aviewteattendance.html",{'data':data,'noti':noti})
    return render(request,"aviewteattendance.html",{'noti':noti})

def trcard(request,did):
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    data=TrainerRegModel.objects.get(id=did)
    return render(request,"trcard.html",{'data':data,'noti':noti})
def tecard(request,did):
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    data=RegisterModel.objects.get(id=did)
    return render(request,"tecard.html",{'data':data,'noti':noti})


def aviewtask(request,did):
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    data=SetTrainingModel.objects.get(id=did)
    task=SubmitTaskModel.objects.filter(Trainer=data.Trainer,Trainee=data.Trainee)
    return render(request,'aviewtask.html',{'task':task,'noti':noti})
def workpage(request,did):
    n=RegisterModel.objects.filter(Action=0)
    noti=len(n)
    task=SubmitTaskModel.objects.filter(id=did)
    return render(request,'workpage.html',{'task':task,'noti':noti})

def logout(request):
    auth.logout(request)
    return redirect('log')