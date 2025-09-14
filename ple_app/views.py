from django.views.generic import FormView , TemplateView , DetailView , ListView , View
from django.http import HttpResponse
from .forms import StudentForm
from django.shortcuts import render, get_object_or_404
from .models import Student_Model , GradesModel
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import generate_student_report
from django.utils import timezone
#import pdfkit



class StudentView(LoginRequiredMixin,FormView):
    #model = Student_Model
    template_name = 'index.html'
    form_class = StudentForm
    success_url = 'results'


    def form_valid(self , form):
        data = form.clean_data()
        result = data['results']
        agg_list = data['agg_list']
        student_name = data['student_name']
        grade = data['grade']
        SST = data['sst_value']
        SCI = data['sci_value']
        ENG = data['eng_value']
        MTC = data['mtc_value']
        Name_only = data['name_only']



        #Getting grading from cleaned data grade
        subject_values = [SST , SCI , ENG , MTC]
        subject_keys = ['SST','SCI','ENG','MTC']
        subject_dict={}
        subject_total = sum(subject_values)

        for key , value in zip(subject_keys , subject_values):
            if value >= 80:
                subject_dict[key] = 'D1'
            elif value >= 75:
                subject_dict[key] = 'D2'
            elif value >= 70:
                subject_dict[key] = 'C3'
            elif value >= 65:
                subject_dict[key] = 'C4'
            elif value >= 60:
                subject_dict[key] = 'C5'
            elif value >= 55:
                subject_dict[key] = 'C6'
            elif value >= 50:
                subject_dict[key] = 'P7'
            elif value >= 40:
                subject_dict[key] = 'P8'
            elif value <= 35:
                subject_dict[key] = 'F9'

        
        

        #Save to  a model
        student_instance = Student_Model.objects.create(Name = Name_only , SST = SST , MTC = MTC , ENG = ENG , SCI = SCI , AGG = agg_list  , Grade = grade)
        GradesModel.objects.create(
            student = student_instance,
            SST_GRADE = subject_dict['SST'] ,
            SCI_GRADE = subject_dict['SCI'] ,
            MTC_GRADE = subject_dict['MTC'] ,
            ENG_GRADE = subject_dict['ENG'])
            

        return render(self.request , 'results.html',{'result':  result , 'form': form , 'agg_list' :agg_list , 'student_name' : student_name , 'grade' : grade } )

class StudentResultView(TemplateView):
    template_name = 'results.html'



class StudentModelView(LoginRequiredMixin , ListView):
    model = Student_Model
    template_name = 'student_list_demo.html'
    context_object_name = 'student_list'

    

    

class StudentDetailView(LoginRequiredMixin , DetailView):
    model = Student_Model
    template_name = 'student_detail.html'
    context_object_name = 'description'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grades'] = GradesModel.objects.filter(student = self.object)
        return context


class PdfGenerateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        try:
            # Get student and grades
            student = get_object_or_404(Student_Model, pk=pk)
            grades = get_object_or_404(GradesModel, student=student)
            
            # Generate PDF
            pdf = generate_student_report(student, grades)
            
            # Create response
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{student.Name}_report_{timezone.now().strftime("%Y%m%d")}.pdf"'
            response.write(pdf)
            return response
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"PDF Generation Error: {str(e)}")
            # Return a more informative error response
            return HttpResponse(
                f"Error generating PDF. Please contact support. Error: {str(e)}",
                status=500,
                content_type="text/plain"
            )