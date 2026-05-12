from src.my_node import MyNode


def has_cycle(head: MyNode) -> bool:
    lento = head
    rapido = head

    while rapido is not None and rapido.next is not None:
        lento = lento.next
        rapido = rapido.next.next

        if lento == rapido:
            return True

    return False
