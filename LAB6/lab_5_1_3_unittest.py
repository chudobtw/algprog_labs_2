import unittest
from collections import defaultdict

def calculate_marriages(n, pairs):
    adj = defaultdict(list)
    nodes = set()
    
    for u, v in pairs:
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
        
    return valid_pairs

class TestTribesMarriages(unittest.TestCase):
    
    def test_example_1_from_task(self):
        pairs = [(1, 2), (2, 4), (3, 5)]
        result = calculate_marriages(3, pairs)
        self.assertEqual(result, 4)

    def test_example_2_from_task(self):
        pairs = [(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)]
        result = calculate_marriages(5, pairs)
        self.assertEqual(result, 6)

    def test_two_separate_tribes_same_gender(self):
        pairs = [(2, 4), (3, 1)]
        result = calculate_marriages(2, pairs)
        self.assertEqual(result, 4)

    def test_single_tribe_no_marriages(self):
        pairs = [(2, 3)]
        result = calculate_marriages(1, pairs)
        self.assertEqual(result, 0)

    def test_multiple_disconnected_components(self):
        pairs = [(1, 2), (3, 4), (5, 6)]
        result = calculate_marriages(3, pairs)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
