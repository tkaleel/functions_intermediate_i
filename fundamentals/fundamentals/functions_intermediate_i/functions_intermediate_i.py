# 1.
# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# # print(x[1][0])

# students[0]["last_name"] = "Bryant"
# # print(students[0])

# sports_directory["soccer"][0] = "Andres"
# # print(sports_directory['soccer'])

# z[0]["y"] = 30
# # print(z[0])


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# 2.
# def iterateDictionary(roster):
#     for position in range(len(roster)):
#         print(roster[position])

# iterateDictionary(students)

# 3.
# def iterateDictionary2(name, roster):
#     for position in range(len(roster)):
#         print(roster[position][name])

# iterateDictionary2("first_name", students)
# iterateDictionary2("last_name", students)

# 4.
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict.keys():
        print(len(some_dict[key]), key.upper())
        for num in range(len(some_dict[key])):
            print(some_dict[key][num])


printInfo(dojo)





