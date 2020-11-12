from django.contrib import admin

from .models import TeamMember
# Register your models here.
class TeamMemberAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username', 'email', 'password', 'groups', 'role']
admin.site.register(TeamMember, TeamMemberAdmin)