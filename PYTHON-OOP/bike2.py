class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        # show bikes price, max speed and total miles
        print "Price: ${}, Max speed: {}, Total miles ridden: {}".format(self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        # print "Riding" and increase total miles ridden by 10 miles
        print "Riding"
        self.miles+=10
        return self

    def reverse(self):
        # print "Reversing" and decrease total miles ridden by 5
        if self.miles - 5 < 0:
            print "Sorry I can not allow you to reverse, you need more mileage before you can do that!"
        else:
            print "Reversing"
            self.miles-=5
        return self


bike1 = Bike(200, '25mph')
bike2 = Bike(5000, '60mph')
bike3 = Bike(99, '5mph')

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
