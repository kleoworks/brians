class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed =  speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = self.set_tax()
        self.display_all()

    def display_all(self):

        print 'Price: {}'.format(self.price)
        print 'Speed: {}'.format(self.speed)
        print 'Fuel: {}'.format(self.fuel)
        print 'Mileage: {}'.format(self.mileage)
        print 'Tax: {}'.format(self.tax)

    def set_tax(self):
        if self.price > 10000:
            return .15
        else:
            return .12


print "Car 1"
car1 = Car(2000, '35mph', 'Full', '15mpg')
print "------------------------"
print "Car 2"
car2 = Car(2000, '5mph', 'Not Full', '105mpg')
print "------------------------"
print "Car 3"
car3 = Car(2000, '15mph', 'Kind of Full', '95mpg')
print "------------------------"
print "Car 4"
car4 = Car(2000, '25mph', 'Full', '25mpg')
print "------------------------"
print "Car 5"
car5 = Car(2000, '45mph', 'Empty', '25mpg')
print "------------------------"
print "Car 6"
car6 = Car(20000000, '35mph', 'Empty', '15mpg')
print "------------------------"
