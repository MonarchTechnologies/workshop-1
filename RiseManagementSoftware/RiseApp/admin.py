from django.contrib import admin

from .models import TeamMember, Team, Project
# Register your models here.
class TeamMemberAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'email', 'password', 'role', 'team']
class ProjectAdmin(admin.ModelAdmin):
    fields = ['projectTitle', 'description', 'StartDate', 'EndDate']
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Team)
admin.site.register(Project, ProjectAdmin)