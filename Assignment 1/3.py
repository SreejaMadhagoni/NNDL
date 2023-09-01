def double(integer):     #function defination to take interger as input
    return integer*2.54  #returns inches to centimeter
lst =[]      #empty list
n = int(input("Enter number of elements : "))  #user enters number of elements in the list

for i in range(0, n):       #loop to enter elements in the list from 0 to n
    ele = int(input())      #enter element
    lst.append(ele)         #add element to list

print(lst)                   #print the list
output_list = [double(i) for i in lst]    #function call for every elemt in the list

print(output_list)        #prints output list in centimeters
