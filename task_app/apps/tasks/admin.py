from django.contrib import admin
from .models import Tasks


# Register your models here.
@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_at', 'created_by')
    search_fields = ('title', 'content', 'created_by__username')
    list_filter = ('status', 'created_by')
