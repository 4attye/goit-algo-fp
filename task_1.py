# Функція сортування злиттям (merge sort)
def merge_sort(arr):
    # Базовий випадок: якщо масив має 0 або 1 елемент — він вже відсортований
    if len(arr) <= 1:
        return arr

    # Розділяємо масив на дві половини
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортуємо обидві половини і зливаємо їх
    return merge(merge_sort(left_half), merge_sort(right_half))

# Функція для злиття двох відсортованих масивів
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Поки не досягнуто кінця жодного з масивів, додаємо менший елемент у результат
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Додаємо залишки елементів з лівого або правого масиву, якщо такі є
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Функція для злиття двох відсортованих списків
def merge_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    a = l1.head
    b = l2.head

    # Порівнюємо вузли з обох списків та будуємо новий список
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    # Приєднуємо залишки одного зі списків
    tail.next = a or b

    # Створюємо новий об'єкт LinkedList з об'єднаним списком
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


# Клас вузла зв'язного списку
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Клас однозв'язного списку
class LinkedList:
    def __init__(self):
        self.head = None

    # Метод для вставки нового елемента в кінець списку
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    # Метод для виведення елементів списку
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next

    # Метод для реверсу списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Метод для сортування списку
    def sort_list(self):
        arr = []
        current = self.head

        # Перетворюємо список у масив
        while current:
            arr.append(current.data)
            current = current.next

        # Сортуємо масив за допомогою merge sort
        sorted_arr = merge_sort(arr)

        # Очищаємо список і заповнюємо його відсортованими значеннями
        self.head = None
        for value in sorted_arr:
            self.insert(value)

if __name__ == "__main__":

    # Створення двох зв'язних списків
    list1 = LinkedList()
    list2 = LinkedList()

    for i in [3, 1, 4, 2, 9, 0, 5]:
        list1.insert(i)

    for i in [6, 5, 8, 7, 10, 4, 1]:
        list2.insert(i)

    # Виведення початкових списків
    print("Початковий список 1:")
    list1.print_list()

    print("\nПочатковий список 2:")
    list2.print_list()

    # Сортування обох списків
    list1.sort_list()
    print("\nВідсортований список 1:")
    list1.print_list()

    list2.sort_list()
    print("\nВідсортований список 2:")
    list2.print_list()

    # Злиття двох відсортованих списків
    merged_list = merge_lists(list1, list2)
    print("\nОб'єднаний відсортований список:")
    merged_list.print_list()

    # Реверс об'єднаного списку
    merged_list.reverse()
    print("\nСписок після реверсу:")
    merged_list.print_list()