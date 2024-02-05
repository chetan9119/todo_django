from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display=('task','is_completed','created_at','updated_at')
    search_fields=('task',)



# Register your models here.
admin.site.register(Task, TaskAdmin)