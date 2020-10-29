from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    description = models.TextField(blank=True, null=True)
    projectTitle = models.CharField(max_length=13)
    StartDate = models.DateTimeField('StartDate')
    EndDate = models.DateTimeField('EndDate')

    def __str__(self):
        return self

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=13)
    task_description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField('created_date')
    finished_date = models.DateTimeField('finished_date')

    def __str__(self):
        return self


class Timer(models.Model):
    StartTime = models.TimeField(auto_now_add='true')
    EndTime = models.TimeField(auto_now='true')
    TotalTime = models.TimeField(default='true')

    def __str__(self):
        return self


class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TeamName = models.CharField(max_length=20)
    SizeOfTeam = models.IntegerField()
    TeamMembersList = [SizeOfTeam]
    #TeamMember = models.CharField(max_length=20)

    def __str__(self):
        return self

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