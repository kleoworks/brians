class Underscore(object):

    def map(self, arg_func, arg_list):
        new_list = []
        map_func = arg_func
        for item in arg_list:
            new_list.append(map_func(item))
        return new_list

    def reduce(self):
        pass
        # varied reviews..... leaving for another time...

    def find(self, arg_func, arg_list):
        pass
        # i think this has to do with strings... leaving for another time...

    def filter(self,  arg_func, arg_list):
        new_list = []
        find_func = arg_func
        for item in arg_list:
            if find_func(item) == True:
                new_list.append(item)
        return new_list

    def reject(self):
        pass
        # not sure what this is...


_ = Underscore()

times2 = _.map(lambda x: x*2, [1,2,3,4])
print times2

filterLess10 = _.filter(lambda x: x < 10, [1,2,10,12,4])
print filterLess10
