# toss coin 5000 times, track how many heads and tails using random function

import random

heads = 0
tails = 0

for num in range(1,5000+1):
    toss = int(round(random.random())) # get random number, round it, and convert float to int
    if toss == 1:
        heads += 1
        print "Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(num, heads, tails)

    elif toss == 0:
        tails += 1
        print "Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(num, heads, tails)
