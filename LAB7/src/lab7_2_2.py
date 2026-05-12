import csv


class DSU:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return False

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot  
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

        return True


def calculate_minimum_cable_length(filename="communication_wells.csv"):
    edges = []
    nodes = set()

    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                u = row[0].strip()
                v = row[1].strip()
                weight = float(row[2].strip())

                edges.append((weight, u, v))
                nodes.add(u)
                nodes.add(v)
    except FileNotFoundError:
        return f"Помилка: Файл {filename} не знайдено."
    except Exception as e:
        return f"Помилка зчитування файлу: {e}"

    if not nodes:
        return 0

    edges.sort()

    dsu = DSU(nodes)
    min_cable_length = 0
    edges_used = 0

    for weight, u, v in edges:
        if dsu.union(u, v):
            min_cable_length += weight
            edges_used += 1

    if edges_used == len(nodes) - 1:
        return min_cable_length
    else:
        return -1


if __name__ == "__main__":
    result = calculate_minimum_cable_length()

    if isinstance(result, float) and result.is_integer():
        print(int(result))
    else:
        print(result)
