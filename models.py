from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class CourseModel(models.Model):
    Course_Name=models.CharField(max_length=70)

class RegisterModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    number=models.CharField(max_length=70)
    img=models.ImageField(upload_to='image/',null=True)
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    Certificate=models.ImageField(upload_to='image/',null=True)
    Join_Date=models.DateField(auto_now_add=True)
    Action=models.IntegerField(default=0)

class TrainerRegModel(models.Model):   
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    number=models.CharField(max_length=70)
    img=models.ImageField(upload_to='image/',null=True)
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True) 
    Join_Date=models.DateField(auto_now_add=True)




class TopicModel(models.Model):
    Trainer=models.ForeignKey(TrainerRegModel,on_delete=models.CASCADE,null=True)
    Topic=models.CharField(max_length=70)
    Start_Date=models.DateField(auto_now_add=True)
    End_Date=models.DateField()
    Action=models.IntegerField(default=0) 
 
class SetTrainingModel(models.Model):
    Trainer=models.ForeignKey(TrainerRegModel,on_delete=models.CASCADE,null=True)
    Trainee=models.ForeignKey(RegisterModel,on_delete=models.CASCADE,null=True)
    ActionTr=models.IntegerField(default=0)
    ActionTe=models.IntegerField(default=0)

class TrFeedBackModel(models.Model):
    Trainer=models.ForeignKey(TrainerRegModel,on_delete=models.CASCADE,null=True)
    Feedback=models.TextField(max_length=300)
    Date=models.DateField(auto_now_add=True)

class TeFeedBackModel(models.Model):
    Trainer=models.ForeignKey(TrainerRegModel,on_delete=models.CASCADE,null=True)
    Trainee=models.ForeignKey(RegisterModel,on_delete=models.CASCADE,null=True)
    Feedback=models.TextField(max_length=300)    
    Date=models.DateField(auto_now_add=True)

class TeIssueModel(models.Model):
    Trainee=models.ForeignKey(RegisterModel,on_delete=models.CASCADE,null=True)
    Issue=models.TextField(max_length=300)   
    Date=models.DateField(auto_now_add=True)
    Replay=models.TextField(max_length=300,null=True) 
    Action=models.IntegerField(default=0)  
    TeAction=models.IntegerField(default=0)  

class TrIssueModel(models.Model):
    Trainer=models.ForeignKey(TrainerRegModel,on_delete=models.CASCADE,null=True)
    Issue=models.TextField(max_length=300)   
    Date=models.DateField(auto_now_add=True)
    Replay=models.TextField(max_length=300,null=True) 
    Action=models.IntegerField(default=0) 
    TrAction=models.IntegerField(default=0)      

class TeAttendance(models.Model):
    Trainer=models.ForeignKey(TrainerRegModel,on_delete=models.CASCADE,null=True)
    Trainee=models.ForeignKey(RegisterModel,on_delete=models.CASCADE,null=True)
    Attendance=models.CharField(max_length=70)
    Date=models.DateField(auto_now_add=True)
    
class TrAttendance(models.Model):
    Trainer=models.ForeignKey(TrainerRegModel,on_delete=models.CASCADE,null=True)
    Attendance=models.CharField(max_length=70)
    Date=models.DateField(auto_now_add=True)

class TrleaveModel(models.Model):   
    Trainer=models.ForeignKey(TrainerRegModel,on_delete=models.CASCADE,null=True)
    Date=models.DateField()
    Reason=models.TextField(max_length=300,null=True)
    Action=models.IntegerField(default=0)

class TeleaveModel(models.Model):   
    Trainee=models.ForeignKey(RegisterModel,on_delete=models.CASCADE,null=True)
    Trainer=models.ForeignKey(TrainerRegModel,on_delete=models.CASCADE,null=True)
    Date=models.DateField()
    Reason=models.TextField(max_length=300,null=True)
    Action=models.IntegerField(default=0)   
    ActionTr=models.IntegerField(default=0)   

class TaskModel(models.Model):
    Trainer=models.ForeignKey(TrainerRegModel,on_delete=models.CASCADE,null=True)
    Trainee=models.ForeignKey(RegisterModel,on_delete=models.CASCADE,null=True)
    Subject=models.CharField(max_length=70)
    Start_Date=models.DateField(auto_now_add=True)
    End_Date=models.DateField()
    Action=models.IntegerField(default=0)

class SubmitTaskModel(models.Model):
    Trainer=models.ForeignKey(TrainerRegModel,on_delete=models.CASCADE,null=True)
    Trainee=models.ForeignKey(RegisterModel,on_delete=models.CASCADE,null=True)
    Task=models.ForeignKey(TaskModel,on_delete=models.CASCADE,null=True)
    Submit_Date=models.DateField(auto_now_add=True)
    work=models.FileField(upload_to='video/',null=True)
    Action=models.IntegerField(default=0)