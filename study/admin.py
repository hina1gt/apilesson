from django.contrib import admin
from .models import *

@admin.register(StudyCenter)
class StudyCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Teacher)
class TecherAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname')
    list_display_links = ('id', 'fullname')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname')
    list_display_links = ('id', 'fullname')