subjects = {
        'mtc':80,
        'sci':50,
        'eng':80,
        'sst':90
}
grades= {}
agg_list = []
for subject , mark in subjects.items():
    if mark >=85:
                grade = 'D1'
                agg_list.append(1)

    elif mark >=80:
                grade = 'D2'
                agg_list.append(2)

    elif mark >= 75:
                grade = 'C3'
                agg_list.append(3)


    elif mark >= 70:
                grade = 'C4'
                agg_list.append(4)

    elif mark >= 60:
                grade = "C5"
                agg_list.append(5)

    elif mark >= 50:
                grade = 'C6'
                agg_list.append(6)

    elif mark >= 45:
                grade = 'P7'
                agg_list.append(7)

    elif mark >= 35:
                grade = 'p8'
                agg_list.append(8)

    else:
                grade = 'F9'
                agg_list.append(9)

    grades[subject] = grade
    

for key , value in subjects.items():
        print(key , value)

