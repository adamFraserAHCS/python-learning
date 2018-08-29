class Node():

    def __init__(self):
        self.nextNode = None
        self.data = None

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data 

    def append(self, node2Add):
        if self.nextNode == None:
            self.setNext(node2Add)
        else:
            self.getNext().append(node2Add)

class linkedList():
    def __init__(self):
        self.root = Node()

    def __str__(self):
        printStr = "this list is empty :C"

        currentNode = self.root
        if(currentNode != None):
            printStr = ""
            while(currentNode.getNext() != Node):
                printStr += str(currentNode.getData()) + "\t"
                currentNode = currentNode.getNext()
            printStr += str(currentNode.getData()) + "\t"
        return printStr

    def append(self, data): 
        newNode = Node()
        newNode.setData(data)
        self.root.append(newNode)

    def count(self):
        currentNode = self.root
        tally = 0
        while currentNode != None:
            tally += 1
            currentNode = currentNode.getNext()
        return tally


    


root = Node()
root.setData("this is the root node")

seccond = Node()
seccond.setData("this is the seccond node")
root.append(seccond)

third = Node()
third.setData("this is the last node")
root.append(third)

print(root.getNext().getNext().getData())
