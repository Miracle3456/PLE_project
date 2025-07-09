x = {'sst':90 , 'sci':90 , 'eng':56 , 'mtc':90}
x_dict={}

for key , value in x.items():
    if value >=80:
        grade = 'D1'
        x_dict[key] = grade
                
    elif value >=75:
        grade = 'D2'
        x_dict[key] = grade

    elif value >= 65:
       grade = 'C3'  
       x_dict[key] = grade       

    elif  value >= 55:
        grade = 'C4'
        x_dict[key] = grade
                
    elif value >= 50:
        grade = 'C5'
        x_dict[key] = grade
    elif value >= 45:
        grade = 'C6'
        x_dict[key] = grade

    elif value >= 30:
        grade = 'F9'  
        x_dict[key] = grade    
    elif value >= 101:
        grade = 'D4'
        x_dict[key] = grade
                

  
                
print(x_dict)