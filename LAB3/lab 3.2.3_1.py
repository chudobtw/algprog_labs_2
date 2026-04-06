import os

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_horizontal_tree(root):
    if not root:
        return
        
    rows, cols = 40, 100
    canvas = [[" "] * cols for _ in range(rows)]
    
    def draw_branch(node, r, c, dir_x, h_step, v_step):
        if not node:
            return
            
        if node.right:
            char = "\\" if dir_x == -1 else "/"
            canvas[r - max(1, v_step // 2)][c + (dir_x * h_step) // 2] = char
            draw_branch(node.right, r - v_step, c + dir_x * h_step, dir_x, max(2, h_step - 2), max(2, v_step // 2))

        for i, ch in enumerate(str(node.data)):
            canvas[r][c + i] = ch
            
        if node.left:
            char = "/" if dir_x == -1 else "\\"
            canvas[r + max(1, v_step // 2)][c + (dir_x * h_step) // 2] = char
            draw_branch(node.left, r + v_step, c + dir_x * h_step, dir_x, max(2, h_step - 2), max(2, v_step // 2))

    start_r = 18 
    start_c = 40
    root_str = str(root.data)
    
    for i, ch in enumerate(root_str):
        canvas[start_r][start_c + i] = ch
        
    if root.left:
        canvas[start_r][start_c - 4:start_c - 1] = ["-", "-", "-"]
        draw_branch(root.left, start_r, start_c - 6, -1, 6, 8)
        
    if root.right:
        canvas[start_r][start_c + len(root_str) + 1:start_c + len(root_str) + 4] = ["-", "-", "-"]
        draw_branch(root.right, start_r, start_c + len(root_str) + 5, 1, 6, 8)

    for row in canvas:
        line = "".join(row).rstrip()
        if line:
            print(line)

def build_tree(elements):
    if not elements or elements[0].upper() in ("N", "NONE"):
        return None
        
    root = Node(int(elements[0]))
    queue = [root]
    idx = 1

    while queue and idx < len(elements):
        curr = queue.pop(0)

        if idx < len(elements) and elements[idx].upper() not in ("N", "NONE"):
            curr.left = Node(int(elements[idx]))
            queue.append(curr.left)
        idx += 1
        
        if idx < len(elements) and elements[idx].upper() not in ("N", "NONE"):
            curr.right = Node(int(elements[idx]))
            queue.append(curr.right)
        idx += 1
        
    return root

def inorder_traversal(node, result=None):
    if result is None:
        result = []
    
    if node:
        inorder_traversal(node.left, result)
        result.append(node.data)
        inorder_traversal(node.right, result)
        
    return result

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "inorder_invert.txt")
    
    if not os.path.exists(filename):
        print(f"Помилка: файл не знайдено за шляхом: {filename}")
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().replace(',', ' ').split()
        
    print(f"Початкові дані з файлу: {content}\n")

    original_tree = build_tree(content)
    
    if original_tree:
        inorder_result = inorder_traversal(original_tree)
        print("In-order")
        print(inorder_result)

        inorder_strings = [str(num) for num in inorder_result]

        new_tree_root = build_tree(inorder_strings)
        
        print_horizontal_tree(new_tree_root)
        
    else:
        print("Дерево порожнє")

if __name__ == "__main__":
    main()