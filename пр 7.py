class Node:


    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:


    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def enqueue(self, item):

        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._count += 1

    def dequeue(self):

        if self.is_empty():
            raise IndexError("Черга порожня! Неможливо виконати dequeue().")

        dequeued_data = self.head.data
        self.head = self.head.next
        self._count -= 1


        if self.head is None:
            self.tail = None

        return dequeued_data

    def peek(self):

        if self.is_empty():
            raise IndexError("Черга порожня! Неможливо виконати peek().")
        return self.head.data

    def clear(self):

        self.head = None
        self.tail = None
        self._count = 0

    def count(self):

        return self._count

    def size(self):

        return self._count

    def to_string(self):

        if self.is_empty():
            return "[]"

        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next

        return "[" + " -> ".join(elements) + "]"

    def is_empty(self):

        return self.head is None

    def __str__(self):

        return self.to_string()



if __name__ == "__main__":
    my_queue = Queue()

    print("--- 1. Додавання елементів у чергу (enqueue) ---")
    my_queue.enqueue(12)
    my_queue.enqueue(25)
    my_queue.enqueue(8)

    print(f"Вміст черги: {my_queue.to_string()}")
    print(f"Перший елемент у черзі (peek): {my_queue.peek()}")
    print(f"Кількість елементів (count/size): {my_queue.count()}")

    print("\n--- 2. Вилучення елементів з черги (dequeue) ---")
    first_out = my_queue.dequeue()
    print(f"Вилучено перший елемент: {first_out}")
    print(f"Черга після dequeue: {my_queue.to_string()}")
    print(f"Новий перший елемент (peek): {my_queue.peek()}")

    print("\n--- 3. Очищення черги (clear) ---")
    my_queue.clear()
    print(f"Черга після clear(): {my_queue.to_string()}")
    print(f"Розмір черги після очищення: {my_queue.size()}")