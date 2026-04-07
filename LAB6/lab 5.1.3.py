import sys
from collections import defaultdict

def solve():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token
                
    tokens = get_tokens()
    
    try:
        n = int(next(tokens))
    except StopIteration:
        return
        
    adj = defaultdict(list)
    nodes = set()
    
    for _ in range(n):
        u = int(next(tokens))
        v = int(next(tokens))
        adj[u].append(v)
        adj[v].append(u)
        nodes.add(u)
        nodes.add(v)
        
    visited = set()
    tribes = []
    
    total_boys = 0
    total_girls = 0
    
    for node in nodes:
        if node not in visited:
            boys = 0
            girls = 0
            stack = [node]
            visited.add(node)
            
            while stack:
                curr = stack.pop()
                
                if curr % 2 != 0:
                    boys += 1
                else:
                    girls += 1
                    
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
                        
            tribes.append((boys, girls))
            total_boys += boys
            total_girls += girls
            
    valid_pairs = total_boys * total_girls
    
    for boys, girls in tribes:
        valid_pairs -= boys * girls
        
    print(valid_pairs)

if __name__ == '__main__':
    solve()
