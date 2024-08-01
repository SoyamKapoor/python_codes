# # Variable declaration
# height = 1.78  # float data type, initialization of variable
# weight = 60  # int data type, initialization of variable
# bmi = weight / height**2  # formula => w/h**2 == w/(h)^2 same of other values as; w/h**n is equal to w/(h)^n

# # Print BMI value and its data type
# print("Value of bmi=(weight/(height)^2) =>", bmi)  # this prints the value of bmi
# print("The Data type of bmi is:", type(bmi))  # The data type of bmi is:
# print("Value of height is:", height, "and the Data type of height is:", type(height))  # The data type of height is:
# print("Value of weight is:", weight, "and the Data type of weight is:", type(weight))  # The data type of weight is:

# #newline     \n
# print("Hello\nMy name is Soyam Kapoor\nSukkur IBA University")
# #String with multiple lines
# sst="""
# Hey
# Howareyou
# """
# print(sst[0])
# print(sst[1])
# print(sst[2])
# print(sst[3])
# print(sst[4])
# print(sst[5])
# print(sst[6])
# print(sst[7])
# print(sst[8])

# print("Lets printing complete multiline string using for loop")
# #Printing all using for loop
# for character in sst:
#     print(character)
# #Multiline Comment
# '''
# THIS 
# IS 
# MULTILIEN COMMENT
# '''
# #<========================================DATA TYPES IN PYTHON=====================================================>
# #Integer
# integer=9
# print("This is an integer Value",integer)

# #Float
# floating=6.58
# print("This is a floating Value",floating)

# #Complex no data type
# complex=complex(8,2)
# print("This is a complex value",complex,"The data type of complex value is ",type(complex))

# #String
# string_="Hello Programmers"
# print("This is a String",string_)

# #List  (Collection of multiple datatype values), The value are mutable(Values can be changed)
# listing=[8,8.6,[-4,5.2],["Appple","Banana"]]
# print("This is a list",listing)

# #Tuple (Similiar to list but its immutable(Values cannot be changed)
# tuple1=(("orangejuice","pineapplejuice"),("frenchfries","sandwich"))
# print("This is a tuple",tuple1)

# #Mapped data: dict
# dict1={"Name":"Soyam","age":19,"can Vote":True}
# print("This is a Mapped data:dict",dict1)

# #<===============================================================================================================>
# #                                    Operators in Python
# print("Addition 15+6=",15+6)
# print("Subtraction 15-6=",15-6)
# print("Multiplication 15*6=",15*6)
# print("Division 15/6=",15/6)
# print("Floor Division 15//6=",15//6)
# print("Modulus 15%6=",15%6)
# print("Exponential 5^3=",5**3)
# #<===============================================================================================================>
# #                                       Typecasting
# # Explicit Typecasting
# this="15"
# number=7
# print("The sum of 15+7 is",int(this)+number)

# # Implicit Typecasting
# first1=5
# second1=1.5
# print("The data type of 5 is",type(first1))
# print("The data type of 1.5 is",type(second1))
# print("The sum of 5 + 1.5 is ",first1+second1,"Datatype is",type(first1+second1)) #Python implicit typecasting has been done here
# #<===============================================================================================================>


# #Printing in python
# print("Hey",6,7,sep="?",end="562")
# print("Hello") # Hello is connected with the upper statement because of end used there, and ","sep="" means that whatever u print before that in the same print command will be seperated by that
# print("How's you")

# # String example
# string1 = 'This is string'  # or string1="This is string" you can use single or double quotation
# print("The value of string1 is", string1, "and The data type of string1 is", type(string1))  # printing value and data type of string1 

# # String concatenation
# st1 = 'ab'  # initialization of a string
# st2 = 'cd'  # initialization of a string
# st3 = st1 + st2  # adding both strings
# print("ab + cd =",st3)  # printing concatenated strings

# # Integer example
# a = 5  # initialization of an integer
# b = 10  # initialization of an integer
# print("Value is: a = " + str(a) + " and b = " + str(b))  # int to string conversion
# print("Value is: a =", a, "and b =", b)  # printing values directly

# # Slicing 
# # Syntax =>   variablename[start:stop:step]  
# #                                 Points to Remember
# # if step is not mentioned then by default its 1 
# # start is included and stop will be excluded
# # if start is not mentioned then by default its 0 index
# # if stop is not mentioned then by default it will go till last element, including last element as well in this case
# # if start, stop and step is not mentioned then it will print complete list
# # negative in list parameter, -1 starts from last element then so on to first element, 


# stringx="Gate Smashers"
# print("stringx=",stringx ,"and length of",stringx,"is",len(stringx)) # length of stringx

# substr1=stringx[5:10] 
# print("Value from stringx[5:10]",substr1)

# substr2=stringx[:10] 
# print("Value from stringx[:10]",substr2)

# substr3=stringx[5:] 
# print("Value from stringx[5:]",substr3)

# substr4=stringx[:] 
# print("Value from stringx[:]",substr4)

# substr5=stringx[-8:-3] #[-8:-3] means [len(stringx)-8:len(stringx)-3]
# print("Value from stringx[-8:-3]",substr5)  

# substr6=stringx[5::2] #no stop, 2 is step
# print("Value from stringx[5::2]",substr6)

# substr7=stringx[::-1] 
# print("Value from stringx[::-1]",substr7)

# substr8=stringx[5:12].upper() 
# print("Value from stringx[5:12].upper()",substr8)

# substr9=stringx[5:12].lower() 
# print("Value from stringx[5:12].lower()",substr9)

# # <================================================ LIST BEHAVIOR ==================================================>
# # 1. Changing in both list, Original and Copied                
# x1 = [1, 5, 6]
# y1 = x1  # After this, if you change value in 'y1' list then it also changes in 'x1' list
# print("When y1=x1, the Value of x1=", x1, "and the Value of y1=", y1)
# y1[1] = 6
# print("When y1[1]=6, the Value of x1=", x1, "and the Value of y1=", y1, "NOTE: There's change in original list x1 by changing value in y1 list")

# # 2. NO Changing in Original List
# x2 = [9, 10, 11]
# y2 = list(x2)
# y2 = x2[:]  # copying list using slicing
# print("When y2=list(x2), and y2=x2[:], the Value of x2=", x2, "and the Value of y2=", y2)
# y2[1] = 15
# print("When y2[1]=15, the Value of x2=", x2, "and the Value of y2=", y2, "NOTE: There's no change in original list x2")

# # <==================================================================================================================>
# list_example = [1.57, 562, 890, 2508.54]  # python list is same as an array but it can store multiple datatype values in single list
# print("Values of list", list_example, "and datatype of the list", type(list_example))  # printing the list

# list2 = ["lisa", 1.68, "emma", 1.78, ",yh", 25.6, "elon", 5]  # list containing multiple datatypes
# print("List containing different types =>", list2, "and its datatype is:", type(list2))

# # A list can also have a sublist, Example:
# list_with_sublist = [["lisa", 1.68], ["emma", 1.78], ["yh", 25.6], ["elon", 52.5]]  # A list can also contain multiple list in it, also known as sublist
# print("List with sublist =>", list_with_sublist)

# # Slicing [start(included):end(excluded)] this allows you to access multiple elements of list
# print(list2[2:6])

# fam = ["SK", 1.73, "john", 1.86, "MB", 1.89]
# print("Initial Values", fam)

# # changing value of a list
# fam[3] = 1.76  # changing value of a list on index 3
# print("After changing 3rd index = 1.76", fam)

# # changing value of a list from 0 to 1 index 
# fam[0:2] = ["lisa", 1.99]  # changing value of a list from 0 to 1 index 
# print("After changing 0 to 1 index using slicing", fam) 

# # adding values into the list
# print("Before", fam)
# fam = fam + ["kaun talha", 101]  # adding values to the list, they will be added last
# print("after fam + ['kaun talha', 101]=>",fam)

# #Deleting value from the list
# print("Before",fam)
# del fam[2]  # del() is used to delete an element from the list, we can also remove multiple elements using slicing  
# print("after deleting 2index element from the list using del fam[2]",fam)

# del fam[3:5]  # delete values from 3 to 4 index in list fam
# print("After deleting elements from 3 to 4 =>",fam)
# fam = fam + [10.5]  # add value to the list
# print("After fam = fam + [10.5] =>",fam)

# # List functions
# x = [1.81, 1.99, 1.36, 1.58]
# print("X list", x)
# print("Maximum value in X list using max(x)", max(x))  # print maximum value of x list (btw max() is builtin function)
# print("Minimum value in X list using min(x)", min(x))  # print minimum value of x list (btw min() is builtin function)
# print("round(1.68,2) =>",round(1.68, 2))  # round off a number to 2 digits
# print("round(1.68) =>",round(1.68))  # round off a number to the closest integer, no second parameter means by default it's zero

# # Type conversion
# floating_number = 1.88
# convert_to_integer = int(floating_number)  # int() converts value into integer value 
# print("After converting 1.88 into integer", convert_to_integer)
# print("(2)^5", pow(2, 5))  # 2^5

# # Merging and sorting lists
# first = [11.25, 18.0, 20.0]
# second = [10.75, 9.50]
# full = first + second  # Merge first and second into full
# full_sorted_descending = sorted(full, reverse=True)  # reverse=True means sorted in descending order
# print("Sorted in descending order", full_sorted_descending)  # Print out full_sorted
# full_sorted_ascending = sorted(full, reverse=False)  #reverse=False or don't give the argument reverse means ascending order
# print("Sorted in ascending order", full_sorted_ascending)

# # Another array example
# array = [5, 63, 3, 2, 2, 1, 51, 1, 2132, 1, 1, 2, 21, 2]
# print("Ascending order",sorted(array))
# print("Deascending order",(sorted(array, reverse=True)))

# # Methods: A function that belongs to object, object is any data structure like string, float, int or even list
# listA = ["H", 15.5, "S", 2]
# print("2 is on index:",listA.index(2))  # this is a method because index is a function which belongs to the object which is a list, index() gives the index of a value from a list

# # An other method is count(x); here x is any value; count(x) gives how many times x appears in the list, for example:
# counting=[1,1,1,1,1,2,2,2,3,3]
# print("Total no of ones =",counting.count(1),"Total no of twos =",counting.count(2),"Total no of threes =",counting.count(3))

# countingx = [1, 2, 2, 2, 3, 3, 3, 3, 3]
# print("count(2) gives how many times '2' occurs in the list: here 2 occurs:", countingx.count(2), "times")

# # String methods
# st = 'lis'
# print("Before using capitalize()", st, "After using capitalize()", st.capitalize())  # string.capitalize(), capitalize the first letter of a string
# print("Replacing 's' to 'za', Before:", st, "and After:", st.replace("s", "za"))  # string.replace(x, y) will replace x with y in output

# # In python everything is an object
# # Objects have methods associated, depending on type
# # .index() method is used for both list and string, for example:
# stri = "Soyam"
# rt = ["as", "fer", "dx"]
# print("Index of 'y' in Soyam:", stri.index("y"))
# print("Index of list ['as', 'fer', 'dx'] element 'fer' is", rt.index("fer"))

# # .append() method is used to add an element or a string to the list
# rt.append("integration")
# print("After adding 'integration' to the list using append('integration')", rt)
# rt.append(1.51)
# print("After adding 1.51 to the list using append(1.51)", rt)

# # String case conversion methods
# print("Before:", stri, "; After using stri.upper() =>", stri.upper())  # this will convert all string into upper case
# print("Before:", stri, "; After using stri.lower() =>", stri.lower())  # this will convert all string into lower case

# # Append and reverse methods
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# areas.append(24.5)
# areas.append(15.45)
# print("Areas", areas)
# areas.reverse()  # this will reverse the given list
# print("Reversed Areas", areas)
# print("Sorted in ascending order",sorted(areas,reverse=False))
# print("Sorted in Decending order",sorted(areas,reverse=True))

# # =======================================================>>>>>>Packages<<<<===============================================
# # Packages
# import numpy as np # np will be used as a object to create an numpy array here   
# this_is_array=np.array([1,2,3]) # here in this case you cannot use array without importing numpy and giving its reference np
# print("This is numpy array using np =>",this_is_array)

# #Array without using np
# from numpy import array   #this will only import array and we don't need use np this time
# this_is_array2=array([1,2,3,4])
# print("Numpy array without using np =>",this_is_array2)

# # Calculating circumference and area of a circle
# # Import the math package
# import math as m
# # Calculate C
# C = 2 * 0.43 * m.pi
# # Calculate A
# A = m.pi* 0.43 ** 2
# print("Circumference: ",round(C,4))
# print("Area: ",round(A,4))

# # Difference between python list and numpy array
# python_list=[1,2,3]
# numpy_array=np.array([1,2,3])
# print("python_list + python_list => [1,2,3] + [1,2,3] =",python_list+python_list)
# print("numpy_array + numpy_array => [1,2,3] + [1,2,3] =",numpy_array+numpy_array)

# # 2D Numpy array
# numpy_2Darray=np.array([[1,2,3,4,5,6],
#                     [7,8,9,10,11,12]])
# print("2D numpy array:\n",numpy_2Darray)
# print("numpy_2Darray.shape will tell you about rows & columns of 2D array, Here it is: (Rows, Columns)",numpy_2Darray.shape)

# np_baseball = np.array(numpy_2Darray)
# # Print out the 50th row of np_baseball
# print("Printing first row and all columns elements",numpy_2Darray[1,:])
# # Select the entire second column of np_baseball: np_weight_lb
# np_weight_lb=numpy_2Darray[:,1]
# # Print out height of 124th player
# print("Printing first row and 0 column element",numpy_2Darray[1,0])

# #<===============================================================================================================================================>
# # User input
# user_input=input("Enter your name: ")
# print("Your name in upper case:",user_input.upper())
# print("Your name in lower case:",user_input.lower())

# first_number=int(input("Enter First number: "))
# second_number=int(input("Enter Second number: "))
# print(first_number,"+",second_number,"=",first_number+second_number)


# alphabets="ABCDE"
# for i in alphabets:
#     print(i)

# String Methods
# ss="!!!Soyam!!!!!!!!!!!!!!!!!"
# print("len(ss)     =>",len(ss))  #Length of ss
# print("ss.upper()  =>",ss.upper())  #convert into uppercase
# print("ss.lower()  =>",ss.lower())  #convert into lowercase
# print("ss.rstrip()  =>",ss.rstrip("!"))  #remove all the trailing !
# print("ss.replace()  =>",ss.replace("Soyam","John"))  #convert into uppercase
# s2="This is a string"
# print("s2.split()  =>",s2.split(" "))  #splits string into a list
# blogHeading="introduction to js"
# print("blogHeading.capitalize() =>",blogHeading.capitalize()) #First letter of the word will be in upper case
# str11="Welcome to the Console!!!"
# print("Value of str11",str11)
# print("str11.center(50) =>",str11.center(50)) #Align to center using 50 spaces
# print("ss.count('!') =>",ss.count("!"))  #count how many ! are there in ss string
# print("ss.endswith('!') =>",ss.endswith("!"))
# sc="Welcome To Python"
# print("Welcome To Python =>",sc.endswith("to",4,10)) #Search if to is found between 4 to 10 index
# print("sc.find('P')  =>",sc.find("P")) #gives index of the string or gives -1 if not found
# print("sc.index('P') =>",sc.index("P")) #gives index of the string or gives Error Exception if not found
# sc="WelcomeToPython"
# print("sc.isalnum() =>",sc.isalnum()) #isalnum==alpha numeric means string made of A-Z, a-z, 0-9, Returns true if the string is alpha numeric
# sc="Welcome"
# print("sc.isalpha() =>",sc.isalpha()) #Just numbers are excluded, A-Z or a-z included strings
# sc="Welcome00"
# print("sc.isalpha() =>",sc.isalpha()) #Just numbers are excluded, A-Z or a-z included strings
# sc="this is a lower case string"
# print("sc.islower() =>",sc.islower())  #returns true if the complete string is in lower case
# sc="THIS IS UPPER CASE STRING"
# print("sc.isupper() =>",sc.isupper())  #returns true if the complete string is in upper case
# print("sc.isprintable() =>",sc.isprintable()) #Returns true if all the characeters are printable
# sc="\nwelcome" #here \n is not printable
# print("sc.isprintable() =>",sc.isprintable()) #Returns true if all the characeters are printable, else false
# sc="         "
# print("sc.isspace() =>",sc.isspace()) #Returns true if there is space present in string, else false
# sc="World Health Organization"
# print("sc.istitle() =>",sc.istitle()) #Returns true when first letter of each word is capital
# sc="this is a laptop"
# print("sc.title =>",sc.title()) # converts every first letter of word into capatalize
# sc="Python is Interprered Language"
# print("sc.startswith('`Python')",sc.startswith("Python")) #Returns true if the string starts with pytghon
# print("sc.swapcase()",sc.swapcase()) #swap upper case to lower and lower to upper case


# Loops / Conditional Statements 
#Conditional Operators: >, <, >=, <=, ==, !=

# if and else Condition
# a=int(input("Enter your age: "))
# if(a>18):
#     print("This is inside if block")
# else:
#     print("This is inside else block")
# print("This is outside the if-else block") 

# Elif Condition  (Same as if-else in Java/C++)
# a=float(input("Enter the number: "))
# if(a>0):
#     print(a,"is a positive number")
# elif(a==0): 
#     print(a,"is neither positive nor negative")
# else:
#     print(a,"is negative number")

# Nested if, else, and elif
# a=float(input("Enter a number from 0 to 100: "))
# if(a<0):
#     print(a,"is negative, not between 0 to 100")
# elif(a==0):
#     print(a,"is zero")
# else:
#     if(a>0 and a<=10):
#         print(a,"is between 0 to 10")
#     elif(a>10 and a<=50):
#         print(a,"is between 11 to 50")
#     elif(a>50 and a<=100):
#         print(a,"is between 51 to 100")
#     elif(a>100):
#        print(a,"is greater than 100")

import time
timestamp=time.strftime("%H:%M:%S") #This will give you H=Hour, M=Minute, S=Seconds
print("Current Time",timestamp)

timestamp_hour=int(time.strftime("%H"))
print("Hours:",timestamp_hour)

timestamp_minutes=int(time.strftime("%M"))
print("Minutes:",timestamp_minutes)

timestamp_seconds=int(time.strftime("%S"))
print("Seconds:",timestamp_seconds)

if(timestamp_hour>=5 and timestamp_hour<12):
    print("Good Morning sweetheart")
elif(timestamp_hour>=12 and timestamp_hour<18):
    print("Good Afternoon sweetheart")
elif(timestamp_hour>=18 and timestamp_hour<22):
    print("Good Evening sweetheart")
else:
    print("Good Night sweetheart")





