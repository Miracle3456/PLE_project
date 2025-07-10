from django.contrib import admin
from .models import Student_Model , GradesModel
# Register your models here.
admin.site.register(Student_Model)
admin.site.register(GradesModel)