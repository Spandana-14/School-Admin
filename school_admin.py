#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv

def write_csv(stud_info1):
    with open("stud_info2.csv",'a',newline='') as Admin_csv:
        writer =csv.writer(Admin_csv)
        if Admin_csv.tell()==0:
            writer.writerow(["NAME","AGE","GENDER","DATE OF BIRTH","CONTACTNO.","EMAIL_ID","PERCENTAGE"])
        writer.writerow(stud_info2)

if __name__== '__main__':
    condi=True
    student_n=1    
    while (condi):
        student_info = input("Enter the details of student {} in the format(Name Age Gender Date_of_Birth ContactNo Email id Percentage):".format(student_n))
        stud_info2=student_info.split(' ')
        print("The entered info is\n Name={} \n Age={}\n Gender={}\n Date_of_birth{}\n ContactNo={} \n Email_id={}\n percentage={}\n".format(stud_info2[0],stud_info2[1],stud_info2[2],stud_info2[3],stud_info2[4],stud_info2[5],stud_info2[6]))
        check=input("Is the displayed info correct?(yes/no):")
        if(check=='yes'):
            write_csv(stud_info2)
            ch=input("Do you wish to continue(yes/no):")
            if (ch=='no'):
                condi=False
            elif (ch=='yes'):
                condi=True
                student_n=student_n+1
        elif(check=='no'):
            print("Pls re-enter proper details")
    print("The given details are properly updated in a file.\n Thank You for entering the details!! ")


# In[ ]:




