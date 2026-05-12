from src.my_node import MyNode


def has_cycle(head: MyNode) -> bool:
    if head is None:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False 