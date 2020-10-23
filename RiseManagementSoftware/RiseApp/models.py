from django.db import models

# Create your models here.

class Project(models.Model):
    description = models.TextField(blank=True, null=True)
    projectTitle = models.CharField(max_length=13)
    StartDate = models.DateTimeField('StartDate')
    EndDate = models.DateTimeField('EndDate')

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=13)
    task_description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField('created_date')
    finished_date = models.DateTimeField('finished_date')


class Timer(models.Model):
    StartTime = models.TimeField(auto_now_add='true')
    EndTime = models.TimeField(auto_now='true')
    TotalTime = models.TimeField(default='true')

class Team(models.Model):
    TeamName = models.CharField(max_length=20)
    SizeOfTeam = models.IntegerField()
    TeamMembersList = []
    TeamMember = models.CharField(max_length=20)
    
    # def AddTeamMember(TeamMember):
    #     TeamMembersList.append(TeamMember)
    # def DeleteTeamMember(TeamMember):
    #     TeamMembersList.remove(TeamMember)
  # When adding new team members, code : object.TeamMembers.append 
  # Make Function in Views for Adding and Removing Team Members