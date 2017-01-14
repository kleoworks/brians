#use two loops to create the sorting function
#both outer and inner loops are controlled with the counter variable, set equal to the length of the list, which decrements by 1 at each pass of the outer loop
#at each iteration of the outer loop, the largest value in the list will get moved to the largest index using it's inner for loop control
#using the counter variable allows the inner for loop to only compare the unsorted portion of the list, and not have to iterate through the already sorted portion each time
#the outer loop continues while the counter is greater than 0
#when the counter is equal to 0, the loop has reached it's 0 indexed value and all values in list have been sorted

import random
import datetime

def bubble_sort(list):

    counter = len(list)

    while (counter > 0):

        for index in range(counter):

            try:
                #check if value at adjacent index (+1) is greater than current index value
                #swap if it is
                if(list[index] > list[index+1]):
                    list[index], list[index+1] = list[index+1], list[index]
            except IndexError:
                #out of range, index error was caught, it's okay, move on!
                pass

        counter -= 1

    print list






#tests
a = [10,9,8,7,6,11,5,4,3,2,1] #unsorted list
bubble_sort(a)


#build list of 100 values, with random numbers between 0 and 10,000
random_list = []
for num in range(100):
    random_list.append(random.randint(0,10000))

#sort random list and tell how long it took to sort
start_time = datetime.datetime.now()

bubble_sort(random_list)

end_time = datetime.datetime.now()

print 'List took this much time to sort: ', end_time - start_time
