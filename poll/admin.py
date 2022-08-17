from django.contrib import admin
from . models import *

# Register your models here.
class AdminPoll(admin.ModelAdmin):
    list_display = ['position','Name_1','count_1','Name_2','count_2','date_created']
    
admin.site.register(Poll,AdminPoll)
