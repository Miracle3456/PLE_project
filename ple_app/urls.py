from django.urls import path
from .views import StudentView , StudentResultView , StudentModelView , StudentDetailView , PdfGenerateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('home/' , StudentView.as_view() , name= 'home'),
    path('results/' , StudentResultView.as_view() , name = 'results'),
    path('students/' , StudentModelView.as_view(),name = 'students_list'),
    path('studentdetail/<int:pk>' , StudentDetailView.as_view() ,name = 'student_detail'),
    path('generate_pdf/<int:pk>/' , PdfGenerateView.as_view() , name = 'generate_pdf')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)