#variable declaration
height=1.78               #float data type, initialization of varaible
weight=60                 #int data type, initialization of varaible
bmi=weight/height**2      #formula=>  w/h**2 == w/(h)^2 same of other values as; w/h**n is equal to w/(h)^n
print("Value of bmi=(weight/(height)^2)",bmi)   #this print value of bmi
print("The Data type of bmi is: ",type(bmi))       #The Data type of bmi is:
print("The Data type of height is: ",type(height)) #The Data type of height is:
print("The Data type of weight is: ",type(weight)) #The Data type of weight is:
string1='This is string'  #initialization of a string
print("The value of string1 is",string1," and The data type of string1 is ",type(string1)) #printing value and data type of string1 is 
st1='ab' #initialization of a string
st2='cd' #initialization of a string
st3=st1+st2 #adding both strings
print(st3) #adding to strings
a=5   #initialization of an integer
b=10  #initialization of an integer
print("value is: a = "+str(a)+" and b = "+str(b)) #int to string conversion
print("value is: a = ",a," and b = ",b)
#<================================================ LIST BEHAVIOUR==================================================>
#1. Changing in both list, Original and Copied                 
x1=[1,5,6]
y1=x1
y1[1]=6
print("x1 list:",x1,"y1 list",y1) #it changes values in both list
#2. NO Changing in Original List
x2=[9,10,11]
y2=list(x1)
y2=x1[:]
y2[1]=15
print("x2 list",x2,"y2 list",y2) # No change in value of x
#<==================================================================================================================>
list=[1.57,562,890,2508.54]  #python list same as an array but it can store multiple datatype values in single list
print(list," and its type ",type(list)) #printing the list
list2=["lisa",1.68,"emma",1.78,",yh",25.6,"elon",5] #list containing multiple datatypes
print("List contating different types =>",list2, " and its type is: ",type(list2))
#A list can also have a sublist, Example:
list_with_sublist=[["lisa",1.68],["emma",1.78],["yh",25.6],["elon",52.5]] #A list can also contain multiple list in it, also known as sublist
print("List with sublist =>",list_with_sublist)
#slicing [start(included):end(excluded)] this allows u to access multiple elements of list
print(list2[2:6])
fam=["SK",1.73,"john",1.86,"MB",1.89]
print("Initial Values",fam)
fam[3]=1.76 #changing value of a list on index 3
print("After changing 3rd index = 1.76",fam)
fam[0:2]=["lisa",1.99] #changing value of a list from 0 to 1 index 
print("After changing 0 to 1 index using slicing",fam) 
fam=fam+["kaun talha", 101] #adding values to the list, they will be added on last
print(fam)
del(fam[2]) #del() is used to delete an element from the list, we can also remove multiple elements using slicing  
print(fam)
del(fam[3:5]) #delete values from 3 to 4 index in list fam
print(fam)
fam=fam+[10.5] #add value to the list
print(fam)
x=[1.81,1.99,1.36,1.58]
print("X list",x)
print("Maximum value in X list",max(x)) #print maximum value of x list (btw max() is builtin function)
print("Manimum value in X list",min(x)) #print manimum value of x list (btw min() is builtin function)
print(round(1.68,2)) #round off a number till 2digits
print(round(1.68))   #round off a number to the closest integer, no second parameter means by default its zero
floating_number=1.88
convert_to_integer=int(floating_number) #int() converts value into integer value 
print("After converting 1.88 into integer",convert_to_integer)
print("(2)^5",pow(2,5))   #2^5
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first + second # Merge first and second into full
full_sorted_descending = sorted(full,reverse=True) #reverse=True means sorted in descending order, reverse=False or dont give the argument reverse means ascending order
print("Sorted in Descending order",full_sorted_descending) # Print out full_sorted
full_sorted_ascending=sorted(full,reverse=False) 
print("Sorted in Descending order",full_sorted_ascending)
array=[5,63,3,2,2,1,51,1,2132,1,1,2,21,2]
print(sorted(array))
print(sorted(array, reverse=True))
#methods: A function that belongs to object, object is any data structure like string, float, int or even list
#for ex: 
listA=["H",15.5,"S",2]
print("2 is on index:"+str(listA.index(2))) #this is method because index is function which belong to the object which is list, index() gives index of a value from a list
#An other method is count(x);here x is any value;count(x) which gives how many times x appears in the list , fox ex:
counting=[1,2,2,2,3,3,3,3,3]
print("count(2) gives how many times '2' occur in the list: here 2 is occur:",counting.count(2),"times")
st='lis'
print("Before using capitalize()",st,"After using capitalize()",st.capitalize()) #string.capitalize(), capitalize the first letter of a string
print("Replacing lis to liza, Before:",st,"and After:",st.replace("s","za")) #string.replace(x,y) will replaced x to y in putput
#In python everything = object
#Objects have method associated, depending on type
#.index() method is used for both list and string, fpr ex:
stri="Soyam"
rt=["as","fer","dx"]
print("Index of Soyam string at 'y'",stri.index("y"))
print("Index of List=['as','fer','dx'] element at 'fer' is",rt.index("fer"))
#.append() method is used add element or a string to the list
rt.append("integration")
print("After adding 'integration' to the list using","append('Integration')",rt)
rt.append(1.51)
print("After adding 1.51 to the list using","append(1.51)",rt)
print("Before:",stri,";After using stri.upper() =>",stri.upper())  #this will convert all string into upper case
st5="SOYAM"
print("Before:",st5,";After using st5.upper()  =>",st5.lower())  #this will convert all string into lower case
areas = [11.25, 18.0, 20.0, 10.75, 9.50] # Create list areas
# Useing append twice to add 24.5 and 15.45
areas.append(24.5)
areas.append(15.45)
print(areas)# Print out areas
areas.reverse() #Reverse the orders of the elements in areas
print(areas) #print out areas
#User input
#========user_input=input("Enter your name: ")
#========print("Your name in upper case:",user_input.upp
#=======================================================>>>>>>Packages<<<<===============================================