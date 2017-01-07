#part 1
# def draw_stars(list):
#
#     for element in list:
#         print '*' * element
#
# x = [4,6,1,3,5,7,25]
#
# draw_stars(x)


#part 2
def draw_stars(list):

    for element in list:
        if type(element) != int:
            print element[0].lower() * len(element)

        else:
            print '*' * element

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)
