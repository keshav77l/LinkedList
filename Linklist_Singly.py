class Node:
   def __init__(self,data=None,next=None):
      self.data=data
      self.next=next
class LinkedList:
   def __init__(self):
      self.head=None
   
   def insert_at_begining(self,data):
      node =Node(data,self.head)
      self.head = node
   def print(self):
      if self.head is None:
         print("Linked list is Empty")
         return
      itr = self.head    #if self.head is not empty.
      Llstr= ''

      while itr:
         Llstr +=str(itr.data) + '-->'
         itr =itr.next
      print(Llstr) 
   def insert_at_end(self,data):
      if self.head is None:    # if linked list is empty.
         self.head=Node(data,None)
         return 
      itr =self.head   #if head is pointing to some node but not at end
      while itr.next:
         itr =itr.next  #till the head point to null
      itr.next =Node(data,None)   #if itr.next become null that's points to end and itr.next to point to new node
   def insert_value(self,data_list):
      self.head=None
      for data in data_list:
         self.insert_at_end(data)
   def get_length(self):
      count=0
      itr =self.head
      while itr:
         count+=1
         itr=itr.next
      return count
   def remove_at(self,index):
      if index<0 or index>=self.get_length():
         raise Exception("Invalid index")
      if index==0:
         self.head=self.head.next
         return
      
      count=0
      itr=self.head
      while itr:
         if count==index-1:
            itr.next=itr.next.next
            break
         itr=itr.next
         count+=1
   def insert_at(self,index,data):
      if index<0 or index>=self.get_length():
         raise Exception("Invalid Index")
      if index==0:
         self.insert_at_begining(data)
         return
      
      count =0
      itr=self.head
      while itr:
         if count ==index-1:
            node= Node(data,itr.next)
            itr.next=node
            break

         itr =itr.next
         count+=1
if __name__=='__main__':
   Ll=LinkedList()
   # Ll.insert_at_begining(56)
   # Ll.insert_at_begining(5)
   # Ll.insert_at_begining(89)
   # Ll.insert_at_end(98)
   Ll.insert_value(["banana","mango","grapes","orange"])
   Ll.print()
   print("length of the Linked List=",Ll.get_length())
   # Ll.remove_at(3)
   # Ll.print()
   Ll.insert_at(0,"figs")
   Ll.print()
    