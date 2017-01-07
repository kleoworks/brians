# read each value in list and return a list where each value is multiplied by 5

def multiply(list, num):

    new_list = []

    for num in range(len(list)):

        new_list.append(list[num] * 5)

    return new_list


a = [2,4,10,16]

b = multiply(a,5)

print b
