
import random
import datetime

# min only with if/else counter
#######################
#use two loops to sort
#inner loop looks for min value in list
#if a min value is found, it stores the index
#after completion of inner loop, it swaps the min index found with the outer loop control variable (counter value)
#at each iteration of outer loop, the inner loop is only checking the remaining indices in list (from the current counter value to the end of the list)

def selection_sort(list):

    if_counter = 0 #counts how many times if/else statement runs

    for counter in range(len(list)):

        index = counter
        min_num = list[index]
        min_idx = index

        while (index < len(list)):


            if (min_num > list[index]):
                min_num = list[index]
                min_idx = index
                if_counter+=1

            else:
                if_counter+=1

            index+=1


        list[counter], list[min_idx] = list[min_idx], list[counter]


    print "if/else counter:" , if_counter
    return list


#min and max version
#######################
#use two loops to sort
#use two counters for control: counter starts from 0 and is used for swapping minimum value, rev_counter starts from end of list and is used for swapping maximum value
#inner loop looks for min and max value in list
#stores the index if found in min_idx and max_idx
#after completion of inner loop, it swaps the min and max indices found with the outer loop control variables (counter and rev_counter)
#at each iteration of outer loop, the inner loop is only checking the remaining indices (between the current counter/index and the rev_counter)

def selection_sort_2(list):

    rev_counter = len(list) - 1
    counter = 0

    while (counter < rev_counter):

        index = counter
        min_num = list[index]
        min_idx = index
        max_num = list[index]
        max_idx = index


        while (index <= rev_counter):


            if (min_num > list[index]):
                min_num = list[index]
                min_idx = index

            if (max_num < list[index]):
                max_num = list[index]
                max_idx = index

            index += 1

        list[counter], list[min_idx] = list[min_idx], list[counter]
        list[rev_counter], list[max_idx] = list[max_idx], list[rev_counter]

        counter += 1
        rev_counter -= 1

    return list



#tests
a = [10,9,8,7,6,11,5,4,3,2,1] #unsorted list
print selection_sort(a)

#populate sample list with 100 values that are random numbers between 0 to 10000
random_list = []
for num in range(100):
    random_list.append(random.randint(0,10000))

#with only min and timed
start_time = datetime.datetime.now()
random_list = selection_sort(random_list)
end_time = datetime.datetime.now()
print random_list
print 'List took this much time to sort w/ only min: ', end_time - start_time

#with min and max and timed
start_time = datetime.datetime.now()
random_list = selection_sort_2(random_list)
end_time = datetime.datetime.now()
print random_list
print 'List took this much time to sort w/ min and max: ', end_time - start_time
