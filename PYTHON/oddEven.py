# count from 1 to 2000, say if odd or even

def odd_even():

    for num in range(1, 2000+1):

        if (num % 2 == 0):
            print 'Number is {}. This is an even number.'.format(num)

        else:
            print 'Number is {}. This is an odd number.'.format(num)

odd_even()
