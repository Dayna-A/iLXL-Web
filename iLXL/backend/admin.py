from django.contrib import admin
from .models import Member, Project, Collaborator, Publication, Grant, Event, News

# Register your models here.
admin.site.register(Member)
admin.site.register(Collaborator)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Grant)
admin.site.register(Event)
admin.site.register(News)