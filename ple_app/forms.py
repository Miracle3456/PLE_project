from django import forms

class StudentForm(forms.Form):
    #model = StudentModel
    Name = forms.CharField(required=True , label='Name' )
    choices  = [
        ('SST' , 'Social Studies'),
        ('MTC' , 'Mathematics'),
        ('SCI' , 'Science'),
        ('ENG' , 'English')

    ]

    SST = forms.IntegerField(label='Social Studies',  required=True)
    ENG = forms.IntegerField(label = 'English' , required=True)
    SCI = forms.IntegerField(label='Science' , required=True)
    MTC = forms.IntegerField(label='Math' , required=True)
   

    def clean_data(self):
        cleaned_data = super().clean()
        sst_value = cleaned_data.get('SST')
        eng_value = cleaned_data.get('ENG')
        sci_value = cleaned_data.get('SCI')
        mtc_value = cleaned_data.get('MTC')
        Name = cleaned_data.get('Name')

        sst_value = int(sst_value)
        eng_value = int(eng_value)
        sci_value = int(sci_value)
        mtc_value = int(mtc_value)

        SST = sst_value
        SCI = sci_value
        ENG = eng_value
        MTC = mtc_value

        grades_dict = {}
        agg_list=[]

        subjects = {
            'Social Studies':sst_value,
            'English':eng_value,
            'Science':sci_value,
            'Mathematics':mtc_value
        }

        for subject , mark in subjects.items():
            if mark >=80:
                grade = 'D1'
                agg_list.append(1)
                grades_dict[subject] = grade

            elif mark >=75:
                grade = 'D2'
                agg_list.append(2)
                grades_dict[subject] = grade

            elif mark >= 65:
                grade = 'C3'
                agg_list.append(3)
                grades_dict[subject] = grade


            elif mark >= 55:
                grade = 'C4'
                agg_list.append(4)
                grades_dict[subject] = grade

            elif mark >= 50:
                grade = "C5"
                agg_list.append(5)
                grades_dict[subject] = grade

            elif mark >= 50:
                grade = 'C6'
                agg_list.append(6)
                grades_dict[subject] = grade

            elif mark >= 45:
                grade = 'P7'
                agg_list.append(7)
                grades_dict[subject] = grade

            elif mark >= 30:
                grade = 'p8'
                agg_list.append(8)
                grades_dict[subject] = grade

            elif mark >= 101:
                return f"Error ....Please Enter correct Marks"

            else:
                grade = 'F9'
                agg_list.append(9)
                grades_dict[subject] = grade

        results = []
        for key  , value in grades_dict.items():
            results.append({'subject':key, 'grade':value})
        
        agg_list = sum(agg_list)

        if agg_list <=12:
            grade = 1

        elif agg_list >= 13:
            grade = 2

        elif agg_list >= 25:
            grade = 3

        elif agg_list >= 36:
            grade = 4

        Name_only = Name.capitalize()
        Name = Name.upper()
        student_name = f"Name: {Name}"
        student_name = student_name.upper()
        

        return {
            'student_name':student_name,
            'results' :results,
            'agg_list':agg_list,
            'grade':grade,
            'sst_value':sst_value,
            'eng_value':eng_value,
            'sci_value':sci_value,
            'mtc_value':mtc_value,
            'name_only':Name_only,
            'SST':SST,
            'SCI':SCI,
            'ENG':ENG,
            'MTC':MTC


            
        } 
        