#stack using LinkedList
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Stack:
    def __init__(self):
        self.head=Node("head")
        self.size=0
    def push(self, x):
        self.size+=1
        node=Node(x)
        if(stack.size==0):
            self.head.next=node
        else:
            node.next=self.head.next
            self.head.next=node
    def pop(self):
        self.size-=1
    def printstack(self):
        curr=self.head.next
        while(curr):
            print(curr.val,end=' ')
            curr=curr.next
stack=Stack()
stack.push(1)
stack.push(2)
stack.printstack()
print()
stack.push(3)
stack.push(4)
stack.printstack()
#LinkedList
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
arr=[1,2,3,4,5,6,7,8,9]
l=LinkedList()
l.head=Node(arr[0])
curr=l.head
for i in range(1,len(arr)):
    node=Node(arr[i])
    while(curr.next!=None):
        curr=curr.next
    curr.next=node
    temp=l.head
    while(temp!=None):
        print(temp.val,end=' ')
        temp=temp.next
    print()
#queue 
from queue import Queue
q=Queue()
q.put(1)
print(list(q.queue))
q.put(2)
print(list(q.queue))
q.put(3)
print(list(q.queue))
print(q.queue[0])
q.get()
print(list(q.queue))
#dequeue
from collections import deque
d=deque()
d.append(1)
print(list(d))
d.append(2)
print(list(d))
d.popleft()
print(list(d))
d.append(3)
print(list(d))
d.pop()
print(list(d))






















