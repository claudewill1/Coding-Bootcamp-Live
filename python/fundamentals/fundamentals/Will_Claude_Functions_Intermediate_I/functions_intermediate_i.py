"""
1. Update Values in Dictionaries and Lists

    Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    Change the last_name of the first student from 'Jordan' to 'Bryant'
    In the sports_directory, change 'Messi' to 'Andres'
    Change the value 20 in z to 30

"""
print("Update Values In Dictioanries and Lists\n")
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# part 1
x[1][0] = 15
print(x)
# part 2
students[0]['last_name'] = 'Bryant'
print(students)
# part 3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
# part 4
z[0]['y'] = 30
print(z)

"""
2. Iterate Through a List of Dictionaries

Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary
 in the list and prints each key and the associated value. For example, given the following list:
"""
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
print("\nIterate Through a List of Dictionaries\n")
def iterateDictionary(lst):
    for dic in lst:
        print(", ".join(f"{key} - {val}" for key,val in dic.items()))
iterateDictionary(students) 

"""
3. Get Values From a List of Dictionaries

Create a function iterateDictionary2(key_name, some_list) that, given a list of 
dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
"""
print("\nGet Values From a List of Dictionaries:\n")
def iterateDictionary2(key_name, lst):
    for i in range(0,len(lst)):
        print(lst[i][key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

print('\n')

"""
4. Iterate Through a Dictionary with List Values

Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
"""
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
print("Iterate Through A Dictionary with List Values")
def printInfo(some_dict):
    count = 7
    for key, values in some_dict.items():
        print(f"{count} ::",key.upper())
        if(isinstance(values,list)):
            for val in values:
                print(val)
        count+=1        

printInfo(dojo)
    
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
