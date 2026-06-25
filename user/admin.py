from django.contrib import admin
from . models import *

# Register your models here.
class tblregisterAdmin(admin.ModelAdmin):
    list_display=("name","email","password","picture","batch","address","regdate")

admin.site.register(tblregister,tblregisterAdmin)

class batchAdmin(admin.ModelAdmin):
    list_display=("id","batchname")
admin.site.register(batch,batchAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=("id","title","picture","batch_name")
admin.site.register(Category,categoryAdmin)

class softwarekitAdmin(admin.ModelAdmin):
    list_display=("id","title","software_info","thumbnail","download_link","posted_date")
admin.site.register(softwareKit,softwarekitAdmin)

class mylectureAdmin(admin.ModelAdmin):
    list_display=("id","title","video_info","vlink","batch","Category","posted_date")
admin.site.register(mylecture,mylectureAdmin)

class mytaskAdmin(admin.ModelAdmin):
    list_display=("id","title","task_info","batch","taskfile","posted_date")
admin.site.register(mytask,mytaskAdmin)

class notesAdmin(admin.ModelAdmin):
    list_display=("id","title","notes_info","batch","posted_date")
admin.site.register(notes,notesAdmin)

class submittedtaskAdmin(admin.ModelAdmin):
    list_display=("id","userid","tid","title","upload_task","marks")
admin.site.register(submittedtask,submittedtaskAdmin)


