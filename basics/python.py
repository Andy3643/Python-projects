

# naming variables
#     name = 'lorna'
#     school = 'Moringa'
#     first_name = 'Andy'
#     second_name ="Mulonga"



#Data types
    # list => ["apple", "banana", "cherry"]
    # tuple => ("apple", "banana", "cherry")
    # integers => 1.2,3,4,5
    # string => "vehicle", "person"
    # float => 0.9, 18.68
    # dictionaries => equivalent ya objects in JS 
                # student = {
                #     'name' :'Kevin',
                #     'age' : '13',
                #     'form' : 'One Blue'
                # }
    #booleans => True or False values


#string methods
    # len() - find number of characters in the string
    # slicing [2:5] - slicing characters in a string
    #upper() - changes all characters to uppercase
    #lower() - changes all characters to lowercase
    #strip()- removes white spaces
    #replace('h','j') -  replace a character in a string with another string
 
#escape characters
        # txt = "We are the so-called \"Vikings\" from the north."
        # print(txt)

#booleans
        #True
            #any declared variable
            #any whole number
        #False
            #empty strings
            #empty lists
            # 0
            #empty tuple
            #empty dictionary

#operators
    # + addition
    # - subtraction
    # = assignmemt
    # * multiplication
    # / division
    # % modulus
    # > greater  than
    # < less than
    # ** exponential 3**2 = 9

#python lists
    #subjects = ["chem",'compscience','biology','physics']
    #lists are mutable i.e one can add or delete items from the list, re arrange items etc
   #list sorting 
        # marks = [ 23,56,12,9,34,90]
        # marks.sort(reverse=True)
        # print(marks)

        # marks = [ 23,56,12,9,34,90]
        # sorted_marks = sorted(marks, reverse=True)
        # print(marks)
        # print(sorted_marks)
    # slicing 
#         fruits = ['apple','oranges','mangoes']
        #append - Add a input to the end of the list
        #pop - deletes the last input in the list/can also specify position
                # fruits = ['apple','oranges','mangoes']
                # fruits.pop(0)
                # print(fruits)
        #extend - adds a list to a list 
                    # fruits = ['apple','oranges','mangoes']
                    # greens = ['kales','spinach','cabbage']
                    # fruits.extend(greens)
                    # print(fruits)
#conditionals
    # age = 17
    # if age >=18 :
    #     print('Get an ID')
    # else:
    #     print ('Stay at home')

# loops
    #while loop - continues as long as a condition is True
    #for loop =  used for iterating in a list
        # fruits = ["apple", "banana", "cherry"]
        # for x in fruits:
        #     print(x)

#functions
    #blocks of code working together to achieve a particular task.
    #declared using the word def
# def my_function():
#     print('Hello world')
# my_function()


# Object Oriented Programing in python

#classes in python 

class Person:
    def __init__(self,name,age):
       self.name = "Joshua"
       self.age = 24
    #class methods
# @classmethod
# def save_person (cls):
#     pass

# class Woman(Person):
#     def __init__(self,height):
#         Person.__init__(self,name,age)
#         self.height = 167
# class Man: