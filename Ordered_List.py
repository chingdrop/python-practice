class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

#The base code is from listing 3.21a, then I added some code to create an ordered list.
#The textbook helped me in making an ordered list class.
class OrderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    #Ordered Lists are more precise with their addition of data items. 
    #Ordered Lists require the data objects to be aware of their place in the stack.
    def add(self,item):

        #previous and stop are variables created to control the iteration in step 1.
        current = self.head
        previous = None
        stop = False

        #Step 1 iterates through the list looking for the correct place to add the item.
        #The goal is to search for a greater item and set the previous variable. 
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        #Step 2 two decisions are made whether there is a previous object in the list.
        #If there is no previous object then temp creates a new object and assigns it to the beginning of the list. 
        #If there is a previous object then temp updates previous and creates a new object
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    #Ordered lists can be more efficient in the search method.
    #Extra conditions can make the search iteration stop interactively.
    def search(self,item):
        current = self.head
        #found and stop are booleans used to control the iteration process.
        found = False
        stop = False

        #The iteration will continue through the list until the object is found.
        #The iteration will also stop if the data object exceeds the search item. 
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() == item:
                    found = True
                else:
                    if current.getData() > item:
                        stop = True
                    else:
                        current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    #multCount is a method that counts the occurences of a specified item. 
    def multCount(self,item):
        #current is assigned to the first object in the list. 
        current = self.head
        #count is assigned to 0. 
        count = 0

        #while loop statement iterates through the entire list.
        while current != None:
            #Count increases when there is a match between the current list object and the item.
            if current.getData() == item:
                count = count + 1
            
            current = current.getNext()
        #returns the number of occurences recorded. 
        return count
                
mylist = OrderedList()

#The list provided in the assignment is added in random order.
#This is done to show that the list can order random data. 
mylist.add(31)
mylist.add(23)
mylist.add(18)
mylist.add(37)
mylist.add(26)
mylist.add(35)
mylist.add(23)
mylist.add(5)
mylist.add(10)
mylist.add(29)
mylist.add(14)
mylist.add(23)
mylist.add(2)
mylist.add(25)

#print statement showing the size of the list. 
print("Size of the list.")
print(mylist.size())

#print statement showing the search results of the list. 
print("Search results for 23 and 35.")
print(mylist.search(23))
print(mylist.search(35))

#print statement showing the occurence results of the list.
print("Multiple entry count for 23 and 35.")
print(mylist.multCount(23))
print(mylist.multCount(35))
