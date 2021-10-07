# 1 - 5 is printed
def number_of_food_groups():
    return 5

print(number_of_food_groups())

# 2 - An error will be given the function - number_of_days_in_a_week_silico_or_triangle_sides() doesn't exist

#def number_of_military_branches():
    #return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# 3 - 5 will be printed - the line of code with the second return statement will never be reached -- the correct answer was an SyntaxError: Invalid Syntax
#3
# def number_of_books_on_hold():
#     return 5
#     ="keyword from-rainbow">return 10
# print(number_of_books_on_hold())


# 4 - 5 will be printed to the console. the "print(10)" will never be reached as the function will end at the return 5

def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# 5 - 5 will be printed inside the function, the second print(x) will print None since nothing is returned from the function there will be no value assigned to x

def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

def addition(b,c):
    return b+c
    return 10
print(addition(3,5))



b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

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