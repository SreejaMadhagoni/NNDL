def centimeter(inches): #Centimeter Function Defination
    return inches * 2.54     #Formula For Centimter
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    e= int(input())    #enter elemts to list
    lst.append(e)      #add elemts to list
print(lst)
output_list = [centimeter(i) for i in lst]  #Centimeter List
print(output_list)
