#use three loops to sort
#outer loop iterates through the entire array
#inner loop iterates from current index, in reverse, decrements at each iteration checking if it's value is smaller than any values in any lower indices
#if it finds a value that it is less than, it stores the index of that value for insertion later
#once the while loop is finished, a copy of the value being inserted is stored, and the inner for loop begins it's work to shift all values to the right by one, starting at the current index, decrementing until it has shifted all values (until it has hit the insertion point)
#after shifting the elements over by 1, the value is inserted, the to_insert flag is reset to False, and the outer loop continues at next index

import random
import datetime


def insertion_sort(list):

    to_insert = False

    for index in range(1,len(list)):

        rev_index = index

        while (rev_index > 0):

            if (list[index] < list[rev_index - 1]):

                insert_idx = rev_index - 1
                to_insert = True

            rev_index -= 1

        if (to_insert == True):

            #shift list values to right
            insert_value = list[index]

            for idx in range(index, insert_idx, -1):

                list[idx] = list[idx-1]

            list[insert_idx] = insert_value

            to_insert = False

    return list


#test
a = [1,5,2,4,0,12,32]
print insertion_sort(a)

#populate list with 100 random values between 0 - 10000
random_list = []
for num in range(100):
    random_list.append(random.randint(0,10000))

start_time = datetime.datetime.now()
random_list = insertion_sort(random_list)
end_time = datetime.datetime.now()

print random_list
print 'List took this much time to sort: ', end_time - start_time
