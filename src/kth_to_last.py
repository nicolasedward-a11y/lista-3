from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    lento = head
    rapido = head

    for _ in range(k):
        if rapido is None:
            return -1

        rapido = rapido.next

    while rapido is not None:
        lento = lento.next
        rapido = rapido.next

    if lento is None:
        return -1

    return lento.value
