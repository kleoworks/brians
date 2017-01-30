class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None


    def printAllVals(self):
        runner = self.head
        while (True):
            # print runner value
            print runner.value

            if runner.next == None:
                break;
            else:
                runner = runner.next


    def addFront(self, value):
        temp = self.head
        self.head = value
        value.next = temp


    ### seems like there should be a better way since there is a tail attribute??? Confused... ###
    def addBack(self, value):
        runner = self.head
        while(True):
            if runner.next != None:
                runner = runner.next
            else:
                runner.next = value
                break


    def insertBefore(self, nextVal, value):
        runner = self.head
        while(True):
            if runner.next == None:
                break # nextVal not found in linked List, don't add anything
            elif runner.next.value == nextVal:
                temp = runner.next
                runner.next = value
                value.next = temp
                break
            runner = runner.next


    def insertAfter(self, preVal, value):
        runner = self.head
        while(True):
            if runner.next == None:
                break # preVal not found in linked list, don't add anything
            elif runner.value == preVal:
                temp = runner.next
                runner.next = value
                value.next = temp
                break
            runner = runner.next


    def removeNode(self, value):
        runner = self.head
        previous = self.head
        while(True):
            if runner.value != value and runner.next == None:
                break # value not found in linked list so don't remove anything
            elif runner.value == value and runner == self.head:
                # removing the first node in the linked list
                value = runner.next
                self.head = value
                break
            elif runner.value == value and runner.next == None:
                # removing the last node in the linked list
                previous.next = None
                break
            elif runner.value == value:
                #removing a node somewhere in list but not at start or end
                previous.next = runner.next
                break

            previous = runner
            runner = runner.next

    def reverseList(self):
        node_list = []
        runner = self.head
        while (True):
            node_list.append(runner)
            if runner.next == None:
                break
            else:
                runner = runner.next

        node_list.reverse()

        for idx in range(len(node_list)):
            if idx == 0:
                self.head = node_list[idx]
                node_list[idx].next = node_list[idx + 1]
            elif idx == len(node_list) - 1:
                node_list[idx].next = None
            else:
                node_list[idx].next = node_list[idx + 1]


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


my_list = SinglyLinkedList()

my_list.head = Node('Alice')
my_list.head.next = Node('Chad')
my_list.head.next.next = Node('Debra')


# // tests
my_list.addFront(Node('Abraham'))
my_list.addBack(Node('Zeb'))
my_list.insertBefore('Zeb', Node('Peter'))
my_list.insertBefore('Zach', Node('Joe')) # should not work! no Zach in linked list
my_list.insertAfter('Peter', Node('Zach'))
my_list.insertAfter('Joe', Node('Rachel')) # should not work! no Joe in linked list
my_list.removeNode('Zeb')
my_list.removeNode('Chad')
my_list.printAllVals()
print '------------- reversing values -------------'
my_list.reverseList()
my_list.printAllVals()
print '------------- reversing values again yea -------------'
my_list.reverseList()
my_list.printAllVals()
