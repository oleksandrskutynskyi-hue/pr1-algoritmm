class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self._count = 0

    def insert(self, value):

        if self.root is None:
            self.root = Node(value)
            self._count += 1
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                self._count += 1
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
                self._count += 1
            else:
                self._insert_recursive(current.right, value)

    def find(self, value):

        return self._find_recursive(self.root, value)

    def _find_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._find_recursive(current.left, value)
        else:
            return self._find_recursive(current.right, value)

    def delete(self, value):

        if self.find(value):
            self.root = self._delete_recursive(self.root, value)
            self._count -= 1
            return True
        return False

    def _delete_recursive(self, current, value):
        if current is None:
            return current

        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            # Випадок 1: Вузол не має дітей або має тільки одну дитину
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left



            min_node = self._find_min_node(current.right)
            current.value = min_node.value

            current.right = self._delete_recursive(current.right, min_node.value)

        return current

    def _find_min_node(self, current):
        while current.left is not None:
            current = current.left
        return current

    def get_min(self):

        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def get_max(self):

        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def count(self):

        return self._count

    def display(self):

        elements = []
        self._inorder_traversal(self.root, elements)
        return elements

    def _inorder_traversal(self, current, elements):
        if current is not None:
            self._inorder_traversal(current.left, elements)
            elements.append(current.value)
            self._inorder_traversal(current.right, elements)



if __name__ == "__main__":
    tree = BinarySearchTree()

    print("--- 1. Додавання елементів ---")
    elements_to_add = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for el in elements_to_add:
        tree.insert(el)

    print(f"Всі елементи дерева (впорядковано): {tree.display()}")
    print(f"Кількість елементів у дереві: {tree.count()}")

    print("\n--- 2. Пошук елементів ---")
    print(f"Чи є елемент 6 у дереві? {tree.find(6)}")
    print(f"Чи є елемент 99 у дереві? {tree.find(99)}")

    print("\n--- 3. Пошук мінімуму та максимуму ---")
    print(f"Найменший елемент: {tree.get_min()}")
    print(f"Найбільший елемент: {tree.get_max()}")

    print("\n--- 4. Видалення елементів ---")
    print("Видаляємо елемент 3 (вузол з двома дітьми)...")
    tree.delete(3)
    print(f"Дерево після видалення 3: {tree.display()}")
    print(f"Нова кількість елементів: {tree.count()}")

    print("\nВидаляємо лист (елемент 13)...")
    tree.delete(13)
    print(f"Дерево після видалення 13: {tree.display()}")
    print(f"Підсумкова кількість елементів: {tree.count()}")