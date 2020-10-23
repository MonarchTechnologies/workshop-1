from django.db import models

# Create your models here.

def Projects(models.Model):
  description = models.TextField(blank=True, null=True)
  projectTitle = models.CharField(max_length=13)
  StartDate = models.DateTimeField('StartDate')
  EndDate = models.DateTimeField('EndDate')
  
def Tasks(models.Model, models.ForeignKey(Projects, on_delete=models.CASCADE)):
  task_name = models.CharField(max_length=13)
  task_ description = models.TextField(blank=True, null=True)
  created_date = models.DateTimeField('created_date')
  finished_date = models.DateTimeField('finished_date')

def Timer():
  StartTime = models.TimeField(auto_now = false,auto_now_add=true)

  EndTime = models.TimeField(auto_now = true, auto_now_add = false)

  TotalTime = models.TimeField()

  #TotalTime = EndTime - StartTime
def Teams():
  TeamName = models.CharField(max_length=20)
  SizeOfTeam = models.IntegerField()
  TeamMembers = models.ListCharField(base_field=CharField(max_length=30),size = SizeOfTeam, max_length=(SizeOfTeam * 5))

  #When adding new team members, code : object.TeamMembers.append
# 