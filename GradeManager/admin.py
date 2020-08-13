from django.contrib import admin

# Register your models here.
from .models import AvailableSemester,UploadedScores,Lecturer

admin.site.register(AvailableSemester)
admin.site.register(UploadedScores)
admin.site.register(Lecturer)
