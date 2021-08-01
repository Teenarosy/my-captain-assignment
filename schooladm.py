# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 20:25:18 2021

@author: Admin
"""

import csv
def write_intro_csv(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:
             writer.writerow(["name","age","contact number","E-mail_ID"])

        writer.writerow(info_list)


condition=True
student_num=1
while(condition):
    student_info=input("enter student information for student #{} in the following format(name age contact_number E-mail_ID):".format(student_num))

    student_info_list = student_info.split(' ')
    
    print("\n The entered information is -\n name:{}\n age:{}\n contact number:{}\n E-mail ID:{}".
          format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

    choice_check=input("Is the entered information correct?(yes/no):")
    if choice_check=="yes":
        
        condition_check=input("enter (yes/no) if you want to enter information for another student:")
        if condition_check =="yes":
            condition= True
            student_num=student_num+1
        elif condition_check== "no":
                condition=False
    elif choice_check=="no":
            print("\n Please re=enter the values!")