class MathDojoI(object):
    def __init__(self):
        self.result = 0

    def add(self, num, *varNums):
        self.result += num
        if varNums:
            for num in varNums:
                self.result += num
        return self

    def subtract(self, num, *varNums):
        self.result -= num
        if varNums:
            for num in varNums:
                self.result -= num
        return self


class MathDojoII(object):
    def __init__(self):
        self.result = 0

    def add(self, num, *varNums):
        if type(num) == list:
            for number in num:
                self.result += number
        else: # not a list
            self.result += num

        if varNums:
            for num in varNums:
                if type(num) == list:
                    for number in num:
                        self.result += number
                else:
                    self.result += num
        return self


    def subtract(self, num, *varNums):
        if type(num) == list:
            for number in num:
                self.result -= number
        else: # not a list
            self.result -= num

        if varNums:
            for num in varNums:
                if type(num) == list:
                    for number in num:
                        self.result -= number
                else:
                    self.result -= num
        return self

class MathDojoIII(object):
    def __init__(self):
        self.result = 0

    def add(self, num, *varNums):
        if type(num) == list or type(num) == tuple:
            for number in num:
                self.result += number
        else: # not a list
            self.result += num

        if varNums:
            for num in varNums:
                if type(num) == list or type(num) == tuple:
                    for number in num:
                        self.result += number
                else:
                    self.result += num
        return self


    def subtract(self, num, *varNums):
        if type(num) == list or type(num) == tuple:
            for number in num:
                self.result -= number
        else: # not a list
            self.result -= num

        if varNums:
            for num in varNums:
                if type(num) == list or type(num) == tuple:
                    for number in num:
                        self.result -= number
                else:
                    self.result -= num
        return self


# tests
md1 = MathDojoI()
print md1.add(2).add(2,5).subtract(3,2).result

md2 = MathDojoII()
print md2.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result

md3 = MathDojoIII()
print md3.add((1),3,4).add([3, 5, 7, 8], (2, 4.3, 1.25)).subtract(2, [2,3], (1.1, 2.3)).result

# WHAT ABOUT A TUPLE OR LIST INSIDE ANOTHER TUPLE/LIST???!!!  -- YIKES!
