class Node:


    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:


    def __init__(self):
        self.top_node = None
        self._count = 0

    def push(self, item):

        new_node = Node(item)
        new_node.next = self.top_node
        self.top_node = new_node
        self._count += 1

    def pop(self):

        if self.is_empty():
            raise IndexError("Стек порожній! Неможливо виконати pop().")

        popped_data = self.top_node.data
        self.top_node = self.top_node.next
        self._count -= 1
        return popped_data

    def peek(self):

        if self.is_empty():
            raise IndexError("Стек порожній! Неможливо виконати peek().")
        return self.top_node.data

    def clear(self):

        self.top_node = None
        self._count = 0

    def count(self):

        return self._count

    def size(self):

        return self._count

    def to_string(self):

        if self.is_empty():
            return "[]"

        elements = []
        current = self.top_node
        while current is not None:
            elements.append(str(current.data))
            current = current.next

        return "[" + " -> ".join(elements) + "]"

    def is_empty(self):

        return self.top_node is None

    def __str__(self):

        return self.to_string()



if __name__ == "__main__":
    my_stack = Stack()

    print("--- 1. Додавання елементів (push) ---")
    my_stack.push(11)
    my_stack.push(22)
    my_stack.push(33)

    print(f"Вміст стеку (toString): {my_stack.to_string()}")
    print(f"Кількість елементів (count): {my_stack.count()}")
    print(f"Кількість елементів (size): {my_stack.size()}")
    print(f"Елемент на вершині (peek): {my_stack.peek()}")

    print("\n--- 2. Вилучення елементів (pop) ---")
    popped_element = my_stack.pop()
    print(f"Вилучений елемент: {popped_element}")
    print(f"Стек після pop(): {my_stack.to_string()}")
    print(f"Нова вершина (peek): {my_stack.peek()}")

    print("\n--- 3. Очищення стеку (clear) ---")
    my_stack.clear()
    print(f"Стек після clear(): {my_stack.to_string()}")
    print(f"Розмір стеку після очищення (size): {my_stack.size()}")