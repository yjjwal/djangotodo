from django.contrib import admin
from .models import Tasks

class TasksAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed','updated_at')
# Register your models here.
admin.site.register(Tasks,TasksAdmin)
