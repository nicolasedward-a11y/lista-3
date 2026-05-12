from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    atual = head

    while atual is not None:
        anterior = atual
        comparar = atual.next

        while comparar is not None:

            if comparar.value == atual.value:
                anterior.next = comparar.next
                comparar = comparar.next
            else:
                anterior = comparar
                comparar = comparar.next

        atual = atual.next

    return head
