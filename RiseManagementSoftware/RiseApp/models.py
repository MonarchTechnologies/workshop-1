from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import GroupManager
from django.contrib.auth.models import Group
# Create your models here.

class Project(models.Model):
    projectTitle = models.CharField(max_length=18)
    description = models.TextField(blank=True, null=True)
    StartDate = models.DateTimeField('StartDate')
    EndDate = models.DateTimeField('EndDate')


class Task(models.Model):
    task_name = models.CharField(max_length=13)
    task_description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField('created_date')
    finished_date = models.DateTimeField('finished_date')


class Timer(models.Model):
    StartTime = models.TimeField(auto_now_add='true')
    EndTime = models.TimeField(auto_now='true')
    TotalTime = models.TimeField(default='true')


#Work todO: create a Custom User, Fix form in admin, Create a Return Case for admin, and a View for Admin!!! Ultra Important!
class Team(Group):
      Team_Name = models.CharField(max_length=45)
      Team_id = models.IntegerField('id:')
      project = models.ForeignKey(Project, on_delete=models.CASCADE)

class TeamMember(User):
     
      #User Roles
      project_manager = 1
      frontend_design = 2
      frontend_dev = 3
      backend_dev = 4
      fullstack_dev = 5
      system_engineer = 6
      senior_software_engineer = 7 
      software_engineer = 8
      junior_software_engineer = 9
      mobile_app_designer = 10
      mobile_app_developer = 11
      android_dev = 12
      ios_dev = 13
      web_developer = 14  
      #Role Choices
      Roles_Choices = (
          (project_manager, 'project manager'),
          (frontend_design, 'frontend designer'),
          (frontend_dev, 'frontend developer'),
          (backend_dev, 'backend developer'),
          (fullstack_dev, 'fullstack developer'),
          (system_engineer, 'systems engineer'),
          (senior_software_engineer, 'senior software engineer'),
          (software_engineer, 'software engineer'),
          (junior_software_engineer, 'junior software engineer'),
          (mobile_app_designer, 'mobile app designer'),
          (mobile_app_developer, 'mobile app developer'),
          (android_dev, 'android developer'),
          (ios_dev, 'ios developer'),
          (web_developer, 'web developer')
      )

      role = models.PositiveBigIntegerField(choices=Roles_Choices, blank=True, null=True) 
      
      team = models.ForeignKey(Team, on_delete=models.CASCADE)

# class Team(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     TeamName = models.CharField(max_length=20)
#     SizeOfTeam = models.IntegerField()
#     #TeamMember = models.CharField(max_length=20)

#     def __str__(self):
#         return self

# def AddTeamMember(TeamMember):
#     TeamMembersList.append(TeamMember)
# def DeleteTeamMember(TeamMember):
#     TeamMembersList.remove(TeamMember)
# When adding new team members, code : object.TeamMembers.append 
# Make Function in Views for Adding and Removing Team Members
#
# _________________________________________________________________________________________________________________
# < EXPERIMENTAL DATASTRUCTURES BEYOND THIS POINT <> DO NOT ATTEMPT YET FOR THE LOGIC HAS NOT BEEN FULLY ANALYZED >
# _________________________________________________________________________________________________________________
#
# Teams = List DataStructure. Teams[Team1[TeamMembers], Team2[TeamMembers], Team[TeamMembers]]
# Can Define TeamMembers as Objects that Display Which Team They are a part of, etc.
# Method/Theory Make a List of List therfore every node is linked to the same root and data can be dynamically assigned,
# as well as easily retrieved, and when being edited, only one list is being changed. The size of the list changed, changes
# however the size was never assigned statically, it is given a soft limit define through its range in which 
# the next list in the list of list is created, example:
#  List[Team1[1,10], Team2[11,20], Team3[21,30]]
# 
#  if (List.Team3[].count = max - 5):
#      TeamCount = List.Count
#      NewListNumber = 'Team' + TeamCount+1
#      List.append[NewListNumber[List.Team3[].max + 1, List.Team3[].max + 9]]
#  
# The results of the previous <SHOULD> add a Team called Team4 with a range of [31, 40] so List would look as follows
# 
# List[Team1[1,10], Team2[11, 20], Team3[21, 30], Team4[31, 40]]
#  
# Or possibly use a linkedlist of List as the datastructure?
#
# Needs Testing.
#