from Student import *

name=input("Enter student name: ")
n=int(input("Enter number of grades: "))

grades=[]

for i in range(n):
    grade=float(input("Enter grade: "))
    grades.append(grade)

print("Student: ",name)
print("Avg: ",Avg(grades))
print("Max: ",Max(grades))
print("Min: ",Min(grades))
print("Status: ",status(grades))