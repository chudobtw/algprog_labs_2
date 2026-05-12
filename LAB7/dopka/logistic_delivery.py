import csv
import heapq

def calculate_shortest_time(filename="logistics_routes.csv", start_node="Київ", end_node="Львів"):
    graph = {}

    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                
                u = row[0].strip()
                v = row[1].strip()
                time = float(row[2].strip())

                if u not in graph: graph[u] = []
                if v not in graph: graph[v] = []
                
                graph[u].append((v, time))
                graph[v].append((u, time))

    except FileNotFoundError:
        return f"Помилка: Файл {filename} не знайдено."
    except Exception as e:
        return f"Помилка зчитування файлу: {e}"

    if start_node not in graph or end_node not in graph:
        return -1

    min_times = {node: float('inf') for node in graph}
    min_times[start_node] = 0

    pq = [(0, start_node)]

    while pq:
        current_time, current_node = heapq.heappop(pq)

        if current_node == end_node:
            return current_time

        if current_time > min_times[current_node]:
            continue

        for neighbor, travel_time in graph[current_node]:
            time_to_neighbor = current_time + travel_time

            if time_to_neighbor < min_times[neighbor]:
                min_times[neighbor] = time_to_neighbor
                heapq.heappush(pq, (time_to_neighbor, neighbor))

    return -1

if __name__ == "__main__":
    result = calculate_shortest_time("dopka/logistics_routes.csv", "Київ", "Львів")

    if isinstance(result, float) and result.is_integer():
        print(int(result))
    else:
        print(result)