def insert_val_at(index, my_list, value):

    new_list = []
    if index < 0 or index >= len(my_list):
        return False
    elif index == 0:
        new_list.append(value)
        new_list += my_list[:]
    else: # all other cases
        new_list += my_list[:index]
        new_list.append(value)
        new_list += my_list[index:]

    return new_list
