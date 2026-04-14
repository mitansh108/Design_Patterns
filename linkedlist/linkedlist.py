class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class SLL():
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            print(f"New node added is {new_node} ")
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        
    def traverse(self):
        if not self.head:
            print("LL is Empty")
        
        else:
            current = self.head
            while current is not None:
                print(current.val)
                current = current.next
            print("End of linked list")

    def insert_at(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            count = 0

            while current is not None and count < position:
                prev = current
                current = current.next
                count +=1
            
            prev.next = new_node
            new_node.next = current
    
    def delete(self, val):
        temp = self.head

        if temp.next is not None:
            if temp.val == val:
                self.head = temp.next
                return
            else:
                found = False
                prev = None
                while temp != None:
                    if val == temp.val:
                        found = True
                        break

                    prev = temp
                    temp = temp.next
                
                if found:
                    prev.next = temp.next
                    del temp
                    return 
                else:
                    print("Node not found")



            

sll = SLL()
sll.append(10)
sll.append(11)
sll.append(44)
sll.traverse()
sll.insert_at(3, 1)
sll.delete(64)
sll.traverse()


        
    

