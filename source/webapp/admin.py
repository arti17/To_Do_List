from django.contrib import admin
from . models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'full_description', 'status', 'date']
    list_filter = ['status']
    search_fields = ['description']
    fields = ['description', 'full_description', 'status', 'date']
    list_display_links = ['id', 'description', 'full_description']


admin.site.register(Task, TaskAdmin)
