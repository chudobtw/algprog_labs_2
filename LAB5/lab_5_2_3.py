from collections import deque

def min_knight_moves(n, start, end):
    row_moves = [2, 2, -2, -2, 1, 1, -1, -1]
    col_moves = [-1, 1, 1, -1, 2, -2, 2, -2]
    
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))
    
    while queue:
        x, y, dist = queue.popleft()
        
        if (x, y) == end:
            return dist
            
        for i in range(8):
            nx = x + row_moves[i]
            ny = y + col_moves[i]
            
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
                
    return -1

def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            n = int(lines[0].split('#')[0].strip())
            
            start_str = lines[1].split('#')[0].strip().split(',')
            start = (int(start_str[0]), int(start_str[1]))
            
            end_str = lines[2].split('#')[0].strip().split(',')
            end = (int(end_str[0]), int(end_str[1]))
            
    except FileNotFoundError:
        print("Помилка: файл input.txt не знайдено.")
        return
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return

    result = min_knight_moves(n, start, end)

    try:
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(str(result) + '\n')
        print(f"Успіх! Результат ({result}) записано у файл output.txt.")
    except Exception as e:
        print(f"Помилка при записі у файл: {e}")

if __name__ == "__main__":
    main()