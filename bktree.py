import Levenshtein
import heapq

class BKTreeNode:
    def __init__(self, word):
        self.word = word
        self.children = {}

class BKTree:
    def __init__(self):
        self.root = None

    def add(self, word):
        if self.root is None:
            self.root = BKTreeNode(word)
            return
        current = self.root
        while True:
            dist = Levenshtein.distance(word, current.word)
            if dist == 0:
                return
            if dist not in current.children:
                current.children[dist] = BKTreeNode(word)
                return
            current = current.children[dist]
    
    def query(self, word, k):
        if self.root is None:
            return []
        heap = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            dist = Levenshtein.distance(word, node.word)
            if len(heap) < k:
                heapq.heappush(heap, (-dist, node.word))
            elif dist < -heap[0][0]:
                heapq.heapreplace(heap, (-dist, node.word))
            elif dist == -heap[0][0] and node.word > heap[0][1]:
                heapq.heapreplace(heap, (-dist, node.word))
            worst_dist = -heap[0][0] if len(heap) == k else float('inf')
            for child_dist, child_node in node.children.items():
                if abs(child_dist - dist) <= worst_dist:
                    stack.append(child_node)
        results = sorted(heap, key=lambda x: (x[0], x[1]), reverse=True)
        return [w for _, w in results]