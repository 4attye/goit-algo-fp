import uuid
import networkx as nx
import matplotlib.pyplot as plt


def heapify(arr, n, i):
    largest = i
    # Індекси лівого та правого дочірніх елементів
    l = 2 * i + 1
    r = 2 * i + 2

    # Якщо лівий дочірній елемент існує і більший за поточний largest — оновлюємо largest
    if l < n and arr[l] > arr[largest]:
        largest = l

    # Якщо правий дочірній елемент існує і більший за поточний largest — оновлюємо largest
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Якщо найбільший елемент не на поточній позиції i — міняємо місцями
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def max_heap(arr):
    n = len(arr)
    # Починаємо з останнього внутрішнього вузла і йдемо вгору до кореня
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Повертаємо перебудований масив у вигляді макс-куп
    return arr


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=1500, node_color=colors)
    plt.show()

def heap_to_tree(heap_list):
    # Якщо список порожній повертаємо None
    if not heap_list:
        return None

    # Створення списку вузлів
    nodes = [Node(val) for val in heap_list]

    for i in range(len(heap_list)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        # Призначення лівого та правого нащадка
        if left_index < len(heap_list):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap_list):
            nodes[i].right = nodes[right_index]

    # Повертаємо кореневий вузол
    return nodes[0]


if __name__ == "__main__":
    # Приклад купи
    numbers = [10, 2, 6, 5, 9, 3, 8]
    heap = max_heap(numbers)

    # Перетворення в дерево
    to_tree = heap_to_tree(heap)

    # Візуалізація
    draw_tree(to_tree, "Макс-купа як дерево")