from collections import deque
from task_4 import draw_tree, heap_to_tree, max_heap


# Генерація градієнту кольорів від темного до світлого (в синіх тонах)
def generate_colors(n):
    colors = []
    for i in range(n):
        g = int(i * 255 / max(n - 1, 1))  # зелений від 0 до 255
        colors.append(f'#00{g:02X}FF')    # формуємо колір
    return colors

# Візуалізація кожного кроку обходу
def visualize_steps(visited_nodes, tree_root, title):
    colors = generate_colors(len(visited_nodes))
    for i, node in enumerate(visited_nodes):
        node.color = colors[i]
        draw_tree(tree_root, f"{title} — крок {i + 1}")

# DFS з використанням стеку
def dfs(root):
    visited = []
    stack = [root]
    seen = set()
    while stack:
        node = stack.pop()
        if node.id in seen:
            continue
        visited.append(node)
        seen.add(node.id)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited

# BFS з використанням черги
def bfs(root):
    visited = []
    queue = deque([root])
    seen = set()
    while queue:
        node = queue.popleft()
        if node.id in seen:
            continue
        visited.append(node)
        seen.add(node.id)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited


if __name__ == "__main__":
    numbers = [10, 2, 6, 5, 9, 3, 8, 1, 4, 2]
    to_tree = heap_to_tree(numbers)

    # DFS
    print("DFS (у глибину):")
    dfs_nodes = dfs(to_tree)
    visualize_steps(dfs_nodes, to_tree, "DFS")

    # Скидання кольорів
    for node in dfs_nodes:
        node.color = "skyblue"

    # BFS
    print("BFS (у ширину):")
    bfs_nodes = bfs(to_tree)
    visualize_steps(bfs_nodes, to_tree, "BFS")