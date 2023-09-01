#Taking input and assigning to a variable
grade = int(input("Enter score: "))

#else if case to determine grade using percentage
#if grade greater than 89 and less that 101 then print grade A will execute
if 101>grade>89:
    print("A")
#if grade greater than 79 and less that 90 then print grade B will execute
elif 90>grade>79 :
    print("B")
#if grade greater than 69 and less that 80 then print grade B will execute
elif 80>grade>69 :
    print("C")
#if grade greater than 59 and less that 70 then print grade B will execute
elif 70>grade>59 :
    print("D")
#else command if above conditions not met.
else:
    print("F")