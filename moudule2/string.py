# a = '''aarsh'''
# print(a[0]) # string indexing 

# print(a[0:3]) # string slicing 

# print(len(a)); #length of the string 

# print(a.replace("a","h")) # replace the string 

# print(a.count("a"))  # tell the count in the string 

# print(a.find("r")) #tell the index of the charcater in the string 

# name = "   H  aRh   "
# print(name.strip()) #strip the spaces 


# name = "Harsh"
# age  = 19
# print(f" My name is {name} and i am {age} years old ")  # f sting and new meathod of concatination 

# print("hello\tdjango")  #tab space 

# a = "python in programming "
# print("python" in a)  // checking if the word exist in the string or not 

# name = "pyhthon"
# print("H"  + name[1:])  // this means slice and return .. start through index 1 and go till end 

# Assingment 1 
# name = input("ENTER YOUR NAME ")
# age = int(input("ENTER YOUR AGE "))
# college  = input("ENTER YOUR COLLEGE ")
# fav_programming_Language = input("ENTER YOUR FAVOURITE PROGRAMING LANGUAGE ")
# print() # empty space 

# print(f" Name : {name} \n Age : {age} \n College : {college} \n FavouriteProgrammingLanguage : {fav_programming_Language}")

# Assignment 2

# username  = input("Enter the username")
# print()
# print(" Uppercase : ", username.upper())
# print("Titlecase : " , username.title())
# print("Lowercase : " , username.lower())
# print("Lenth : " , len(username))
# print(username[0])
# print(username[-1])

# Assingment 3
username = "admin"
password = "user123"
userkanaam = input("Enter your username")
userkapass = input("Enter your pass")
if(username  == userkanaam.lower() and password == userkapass.lower()):
    print("Succefully Login !!")
else:
    print("Incorrect username and password")