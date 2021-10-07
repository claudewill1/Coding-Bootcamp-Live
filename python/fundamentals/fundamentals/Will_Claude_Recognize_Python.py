num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize number
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary declaration and initialization
fruit = ('blueberry', 'strawberry', 'banana') # tuple declaration, initialize tuple
print(type(fruit))  # print type of value : output: <class 'string'>
print(pizza_toppings[1]) # print item in pizza topping list at index 1 : output: 'Sausage'
pizza_toppings.append('Mushrooms') # append new item 'Mushrooms' to end of pizza_toppings list
print(person['name']) # print dictionary value for name output : 'John'
person['name'] = 'George' # replace name value with 'George' 
person['eye_color'] = 'blue' # add key value pair of eye_color and 'blue' to dictionary
print(fruit[2]) # print element at index 2 of tuple fruit = 'banana'
# if else statement
if num1 > 45: # check to see if num1 is greater than 45
    print("It's greater") # print It's greater if true
else: # if false
    print("It's lower") # print it's lower

if len(string) < 5: #if else-if else statement for checking the length of a given string len() gets length of string
    print("It's a short word!")  # print this if string is less than 5 characters "It's a short word!"
elif len(string) > 15: # check if string is greater than 15 characters
    print("It's a long word!") # if greater than 15 characters print "It's a long word!"
else: # do this if previous two are false
    print("Just right!") # if string is greater than equal to 5 characters or string less than equal to 15 characters print 'Just Right!'

for x in range(5): # for loop to loop through the range of 5 numbers, first number being 0
    print(x) # print 0, 1, 2, 3, 4
for x in range(2,5): # loop through range 2 to 5
    print(x) # print 2, 3, 4
for x in range(2,10,3): # loop through range 2 to 10 step 3
    print(x) # print 2, 5, 8
x = 0 # declare x for counting variable
while(x < 5): # perform loop while x is less than 5
    print(x) # output for loop 0, 1, 2, 3, 4
    x += 1 # increase x by 1 at the end of each iteration

pizza_toppings.pop() # remove the last item off pizza_toppings list
pizza_toppings.pop(1) # remove item at index 1 of pizza_toppings list

print(person) # print: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
person.pop('eye_color') # remove eye color value and display to console: 'blue'
print(person) # print: {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings: # for loop to loop through values in pizza_toppings list
    if topping == 'Pepperoni': # if topping equals 'Pepperoni'
        continue # continue loop
    print('After 1st if statement') # print this after the first if statement is ran
    if topping == 'Olives': # if the topping is equal to 'Olives'
        break # break (end) loop

def print_hello_ten_times(): # declare and define a function 'print_hello_ten_times'
    for num in range(10): # prints 'Hello' 10 times while number in range of 10 with index starting at 0 and last index to print 9
        print('Hello') # Hello, Hello, Hello, Hello, Hello, Hello, Hello, Hello, Hello, Hello

print_hello_ten_times() # call print_hello_ten_times() function

def print_hello_x_times(x): #define print_hello_x_times(x) function, prints Hello x number of times with x being an argument passed in in the calling of the function
    for num in range(x): # loop from 0 to number of times input 
        print('Hello') # print 'Hello' for the number of times in a range

print_hello_x_times(4) #print_hello_x_times(4) with 4 passed in as argument printing "Hello" four times

def print_hello_x_or_ten_times(x = 10): # defined function prints hello the number of times passed in as an argument or a default of 10 times
    for num in range(x): # if a value is passed in as an argument 'Hello' will print that number of times, otherwise it will go to the default value of 10 times
        print('Hello')

print_hello_x_or_ten_times() #hello gets printed 10 times
print_hello_x_or_ten_times(4) # hello gets printed 4 times


"""
Bonus section
"""

# print(num3) # NameError: name 'num3' is not defined
# num3 = 72 # defines num3 as a number variable assigned the value of 72
# fruit[0] = 'cranberry'  # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team' favorite_team is not a defined key resulting in a KeyError
# print(pizza_toppings[7]) # returns IndexError: list index out of range, the list only has 5 items, the highest index would be 4 with the index of a list starting at 0
#   print(boolean) # IndentionError: unexpected indent given, there can not be any space before calling this or any other function
# fruit.append('raspberry') # no items can be .appended as the .append is not a built in function for tuples, error given: AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: 'tuple object has no attribute 'pop' tuples are immutable meaning their cannot be modified