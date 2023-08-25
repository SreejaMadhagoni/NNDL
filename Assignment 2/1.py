#Function to take two strings from the user
def full(Fname, Lastname):
  print(Fname + " " + Lastname)  # FirstName Lastname Concatenation
firstname=input("Enter firstname: ")
Lastname = input("Enter Lastname: ")
full(firstname, Lastname)      #Function Call for full name
Fullname= firstname+Lastname
def string_alternative(str): #defining function for printing letters alternatively
  print(str[::2])
string_alternative(Fullname) #function call for string alternative