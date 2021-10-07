#1 5 is printed
def number_of_food_groups():
    return 5
print(number_of_food_groups())


#2 - An error will be given the function - number_of_days_in_a_week_silico_or_triangle_sides() doesn't exist
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())


#3 - 5 will be printed - the line of code with the second return statement will never be reached -- 
# the correct answer was an SyntaxError: Invalid Syntax
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())


#4 - 5 will be printed to the console. the "print(10)" will never
#  be reached as the function will end at the return 5
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())


#5 - 5 will be printed inside the function, the second print(x) will print None since nothing is returned 
# from the function there will be no value assigned to x
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)


#6 - 3 and then 5 will be printed followed by a TypeError. As the add() function doesn't
# return anything nothing can be added in the print function following the function declaration
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))


#7 - 25 is printed to console as both numbers are converted to strings then concatenated with +
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))


#8 100 will be printed by the function and then 10 will be returned and printed by the print() 
# outside the function the return 7 line will never be reached.
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())


#9 the first call in the first print() will be 7, the second call in the second print() will be 14
# the third call will print 21 the return 3 will never be reached
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))


#10 - 8 is printed, the line return 10 is never reached as the function ends at the first return statement
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))


#11 - the output to console will be 500, 500, 300, 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)


#12 - console output 500, 500, 300, 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)


#13 console output 500, 500, 300, 300
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)


#14 - console output 1, 3, 2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()


#15 - console output 1, 3, 5, 10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)