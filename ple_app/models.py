from django.db import models
from django.urls import reverse

class Student_Model(models.Model):
    Name = models.CharField(max_length=30 , null = False)
    SST = models.IntegerField(null=False)
    ENG = models.IntegerField(null=False)
    SCI = models.IntegerField(null=False)
    MTC = models.IntegerField(null=False)
    AGG = models.IntegerField(null=True)
    TOTAL = models.IntegerField(null=True)
    Grade = models.IntegerField(null=True)
    Student_image = models.ImageField(null = True , upload_to='images/' , default = 'images/images/profile-icon.jpg')
    Date_Created = models.DateTimeField(auto_now_add=True , null=False)



    def get_absolute_url(self):
        return reverse('student_detail' , args=[self.pk])
    
    def __str__(self):
        return self.Name
    
  
    

class GradesModel(models.Model):
    student = models.ForeignKey(Student_Model , on_delete=models.CASCADE)
    
    SST_GRADE = models.CharField(max_length=30)
    SCI_GRADE = models.CharField(max_length=30)
    ENG_GRADE = models.CharField(max_length=15)
    MTC_GRADE = models.CharField(max_length=15)
    

    def get_absolute_url(self):
        return reverse('student_detail' , args=[self.pk])


    def __str__(self):
        return f"{self.student} Marks"
    

    
