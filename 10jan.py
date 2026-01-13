#Student Result
name = input("Enter Student name : ")
n = int(input("Enter number of subjects : "))
i = 1
total_marks = 0
for i in range(1,n+1):
    marks = int(input(f"Enter marks of subject {i} : "))
    total_marks += marks


average_marks = total_marks/n

print("\n\t |RESULT SUMMARY|")
print("Student name : ",name)
print("Total marks : ",total_marks)
print("Average marks : ",average_marks)