
#Part 1

# students = [
#     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# for element in students:
#
#         print ' '.join(element.values())


#Part 2
users = {

    'Students': [
        {'first_name' : 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]

}

print 'Students'
counter = 1
for element in users['Students']:
    length = len(''.join(element.values()))
    student = ' '.join(element.values())
    print str(counter) + ' - ' + student + ' - ' + str(length)
    counter+=1

print 'Instructors'
counter = 1
for element in users['Instructors']:
    length = len(''.join(element.values()))
    instructor = ' '.join(element.values())
    print str(counter) + ' - ' + instructor + ' - ' + str(length)
    counter+=1
