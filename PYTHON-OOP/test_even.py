import unittest

def isEven(n):

    return n % 2 == 0

# create a different class for each test
class IsEvenTests(unittest.TestCase):

    def testTwo(self):
        # this is a method of the unittest.TestCase class
        self.failUnless(isEven(2))

    def testThree(self):
        # this is a method of the unittest.TestCase class
        self.failIf(isEven(3))


if __name__ == '__main__':
    unittest.main()


# other methods:
# .assertTrue(my_val) -- use if expected result should be True
# .assertFalse(my_val) -- use if expected result should be False
