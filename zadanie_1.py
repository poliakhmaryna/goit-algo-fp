class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
             return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next   
            current.next = prev        
            prev = current             
            current = next_node        
        self.head = prev
        
    def insertion_sort(self):
        if not self.head or not self.head.next:
            return 
        sorted_head = None  
        current = self.head
        while current:
            next_node = current.next    
            if not sorted_head or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                sorted_cur = sorted_head
                while sorted_cur.next and sorted_cur.next.data < current.data:
                    sorted_cur = sorted_cur.next
                current.next = sorted_cur.next
                sorted_cur.next = current

            current = next_node  

        self.head = sorted_head

    def merge_sorted_lists(self, list1, list2):
        dummy = Node(0)      # тимчасова фіктивна голова
        tail = dummy

        a = list1
        b = list2

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a if a else b
        merged = LinkedList()
        merged.head = dummy.next
        return merged


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

#реверсуємо список
print("\nРеверсований список:")
llist.reverse_list()
llist.print_list()


# сортуємо
print ("\nВідсортований список:")
llist.insertion_sort()
llist.print_list()

# об'єднання два відсортованих  однозв'язних списки

# перший список
ll1 = LinkedList()
ll1.insert_at_end(1)
ll1.insert_at_end(3)
ll1.insert_at_end(5)
ll1.insert_at_end(10)
ll1.insert_at_end(50)
ll1.insert_at_end(100)
# другий список
ll2 = LinkedList()
ll2.insert_at_end(2)
ll2.insert_at_end(4)
ll2.insert_at_end(6)
ll2.insert_at_end(200)
ll2.insert_at_end(201)
# об’єднання
merged = ll1.merge_sorted_lists(ll1.head, ll2.head)
print("Об'єднаний список:")
merged.print_list()
