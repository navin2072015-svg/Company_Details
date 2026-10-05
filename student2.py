#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 22:05:55 2026

@author: pgcp-esd
"""
from abc import ABC, abstractmethod

# 1. The Abstract Blueprint (Abstraction Layer)
class AbstractStudent(ABC):
    
    @abstractmethod
    def calculateGpa(self):
        """Abstract method to calculate GPA. Must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def display(self):
        """Abstract method to display details. Must be implemented by subclasses."""
        pass
   
# 2. The Concrete Implementation
class Student(AbstractStudent):
   
    def __init__(self, studid, sname, m1, m2, m3):
        self.id = studid
        self.name = sname
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.gpa = 0.0
        
    # Implementing the abstract method
    def calculateGpa(self):
        self.gpa = (1/3) * self.m1 + (1/2) * self.m2 + (1/4) * self.m3
        return self.gpa
    
    # Implementing the abstract method
    def display(self):
        print("\n Students Details ...")
        print("_____________________ ")
        print(f"STUDENT ID {self.id}")
        print(f"NAME {self.name}")
        print(f"M1  {self.m1}")
        print(f"M2  {self.m2}")
        print(f"M3 {self.m3}")
        print(f"GPA  {self.gpa}")
        
    def genrate(self):
        pass
    
def menu():
    student_list = []
     
    while True:
        print("\n Student Information menu")
        print("1. Add new Students ")
        print("2. Display all Students")
        print("3. Search by ID ")
        print("4. Search by Name ")
        print("5. Calculate GPA of a Student")
        print("6. Exit ")
         
        choice = input("Enter your choice (1 - 6): ")
         
        if choice == '1':
            try:
                count = int(input("How many student you want to add? "))
                for i in range(1, count + 1):
                    print("Enter the details of the students ...")
                    studid = input("Enter the student id : ")
                    sname = input("Enter the student name : ")
                    m1 = int(input("Enter the marks m1  : "))
                    m2 = int(input("Enter the marks m2 : "))
                    m3 = int(input("Enter the marks m3 : "))
                     
                    New_Students = Student(studid, sname, m1, m2, m3)
                    student_list.append(New_Students)
                
                print(f"\n Successfully Added   {count} student(s) .")

            except ValueError:
                print("Error: Please enter numbers only for counts and marks.")
                
        elif choice == '2':
            print("\n Students Details")
            for student in student_list:
                student.display()
        
        elif choice == '3':
            search_id = input("Enter student ID to search: ")
            found = False
            for student in student_list:
                if student.id == search_id:
                    student.display()
                    found = True
                    break
            if not found:
                print("Student not found.")
                
        elif choice == '4':
            search_name = input("Enter student Name to search: ")
            found = False
            for student in student_list:
                if student.name.lower() == search_name.lower():
                    student.display()
                    found = True
            if not found:
                print("Student not found.")
                
        elif choice == '5':
            search_id = input("Enter student ID to calculate GPA: ")
            found = False
            for student in student_list:
                if student.id == search_id:
                    gpa = student.calculateGpa()
                    print(f"Calculated GPA for {student.name}: {gpa:.2f}")
                    found = True
                    break
            if not found:
                print("Student not found.")
                
        elif choice == '6':
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice. Please select from 1 to 6.")

if __name__ == "__main__":
    menu()
