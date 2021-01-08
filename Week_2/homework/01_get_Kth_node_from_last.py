class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        target_node = self.head
        end_checker = self.head

        if k == 1:
            while target_node.next is not None:
                target_node = target_node.next
            return target_node
        elif k > 1:
            for i in range(k-1):
                end_checker = end_checker.next
            while end_checker.next is not None:
                end_checker = end_checker.next
                target_node = target_node.next
            return target_node
        else:
            return "Not valid K value"


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)

print(linked_list.get_kth_node_from_last(5).data)  # 7이 나와야 합니다!
