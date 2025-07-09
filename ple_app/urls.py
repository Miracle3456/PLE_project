from django.urls import path
from .views import StudentView , StudentResultView , StudentModelView , StudentDetailView , PdfGenerateView

urlpatterns = [
    path('home/' , StudentView.as_view() , name= 'home'),
    path('results/' , StudentResultView.as_view() , name = 'results'),
    path('students/' , StudentModelView.as_view(),name = 'students_list'),
    path('studentdetail/<int:pk>' , StudentDetailView.as_view() ,name = 'student_detail'),
    path('generate_pdf/' , PdfGenerateView.as_view() , name = 'generate_pdf')
]
