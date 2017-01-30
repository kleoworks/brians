class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        # decrease health by 1
        self.health -= 1
        return self

    def run(self):
        # decrease health by 5
        self.health -= 5
        return self

    def displayHealth(self):
        # print name and health
        print "{}'s health: {}".format(self.name, self.health)
        return self


animal1 = Animal('Cat')
animal1.walk().walk().walk().run().run().displayHealth()


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

dog1 = Dog('Misty')
dog1.walk().walk().walk().run().run().pet().displayHealth()


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "this is a dragon!"
        super(Dragon, self).displayHealth()

dragon1 = Dragon('Petes')
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()


dog1.pet()
