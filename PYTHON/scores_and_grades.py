#prompt user 10 times for test score between 60 and 100
#each time, display grade


#create empty list to store grades
grades = []

for num in range(10):
    #prompt user for Scores

    while (True):

        try:

            score = int(raw_input('Score: ')) # try converting to int....did user enter a number?!

            if (score >= 0 and score <=100): # check if number is valid

                grades.append(score) # append number to grades list
                break

            else:
                continue # if the number is not valid, try prompting user again

        except:

            pass # if user did not enter a number, try prompting user again


print 'Scores and Grades'

for grade in grades:

    if (grade >= 90):
        print 'Score: {}; Your grade is A'.format(grade)
    elif (grade >= 80):
        print 'Score: {}; Your grade is B'.format(grade)
    elif (grade >= 70):
        print 'Score: {}; Your grade is C'.format(grade)
    elif (grade >= 60):
        print 'Score: {}; Your grade is D'.format(grade)
    else:
        print 'Score: {} is not a passing grade!  You failed.'.format(grade)
