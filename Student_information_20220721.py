from ast import Not


code=[]
name=[]
email=[]
phone=[]

def inputs():
    student_numbers=int(input("Please note the number of student: "))
    i=1
    while i <= student_numbers: #daxil edəcəyimiz tələbə sayını qeyd edirik
        if i!=1:
            print("Please, enter next student information")

        while True:
            student_code=input("Enter student ID: ")
            if len(student_code)==0:
                print("Do not leave the cell empty")
                continue
            else:
                code.append(student_code)
                break
        while True:
            student_name=input("Enter student name: ")
            if len(student_name)==0:
                print("Do not leave the cell empty")
                continue
            if len(student_name)<15:
                print("The number of characters in the name should not be more than 15.\n Please enter the student's name")
            if student_name == ["!,?,/,>,<,\,=,+,_,-,),(,*,&,^,%,$,$,#,.,,"]:
                print(" Do not use this symbols \n ('!,?,/,>,<,\,=,+,_,-,),(,*,&,^,%,$,$,#,')")
                continue
            else:
                name.append(student_name)
                break
        while True:
            student_email=input("Enter student email: ")
            if len(student_email)==0:
                print("Do not leave the cell empty")
                continue
            else:
                email.append(student_email)
                break
        while True:
            student_phone=input("Enter student phone: ")
            if len(student_phone)==0:
                print("Do not leave the cell empty")
                continue
            else:
                phone.append(student_phone)
                break
      
        i+=1

    query()
        
def query():
    item=input("ENTER the student's name: ")

    for s in name:
        if s==item:
            index_name = name.index(item)
            print("Student code is {},Student name is {},Student email is {},Student phone is {}".format(code[index_name],name[index_name],email[index_name],phone[index_name]))


  
    #pass

#proqram baslayir
inputs()

