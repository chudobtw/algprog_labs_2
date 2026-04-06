class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.color = "RED"
        self.parent = None
        self.left = None
        self.right = None

class RBPriorityQueue:
    def __init__(self):
        self.NIL = Node(None, -1)
        self.NIL.color = "BLACK"
        self.root = self.NIL

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, value, priority):
        new_node = Node(value, priority)
        new_node.left = self.NIL
        new_node.right = self.NIL

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if new_node.priority >= x.priority:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y == None:
            self.root = new_node
        elif new_node.priority >= y.priority:
            y.left = new_node
        else:
            y.right = new_node

        if new_node.parent == None:
            new_node.color = "BLACK"
            return

        if new_node.parent.parent == None:
            return

        self._fix_insert(new_node)

    def _fix_insert(self, k):
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"

    def _minimum(self, node):
        while node.right != self.NIL:
            node = node.right
        return node

    def _maximum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def extract_max(self):
        if self.root == self.NIL:
            print("Помилка: Черга порожня!")
            return None
        
        z = self._maximum(self.root)
        val = z.value
        pri = z.priority
        
        self._delete_node(z)
        return {"value": val, "priority": pri}

    def _transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _delete_node(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            
        if y_original_color == "BLACK":
            self._fix_delete(x)

    def _fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = "BLACK"

    def peek(self):
        if self.root == self.NIL:
            return None
        max_node = self._maximum(self.root)
        return {"value": max_node.value, "priority": max_node.priority}

    def _inorder_print(self, node):
        if node != self.NIL:
            self._inorder_print(node.left)
            print(f"Пріоритет: {node.priority} | Завдання: {node.value}")
            self._inorder_print(node.right)

    def print_queue(self):
        print("\n--- Поточний стан черги (за спаданням пріоритету) ---")
        if self.root == self.NIL:
            print("Черга порожня")
        else:
            self._inorder_print(self.root)
        print("-----------------------------------------------------")


if __name__ == "__main__":
    queue = RBPriorityQueue()
    
    queue.insert("Підготуватися до екзамену з програмування", 100)
    queue.insert("Піти поїсти", 75)
    queue.insert("Катка в КС2(Фейсит)", 40)
    queue.insert("Переробити балкон під чілзон", 60)
    queue.insert("Вивчити ПДР для іспиту", 90)
    queue.print_queue()
    
    print("\nЩо зараз перше в черзі (peek)?", queue.peek())
    
    print("\nПочинаємо виконувати задачі:")
    task1 = queue.extract_max()
    print("Виконано:", task1)
    
    task2 = queue.extract_max()
    print("Виконано:", task2)
    
    print("\nЩо залишилось після виконання двох найпріоритетніших завдань?")
    queue.print_queue()