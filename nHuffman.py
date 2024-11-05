import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def print_codes(node, code=''):
    if node.left:
        print_codes(node.left, code + '0')
    if node.right:
        print_codes(node.right, code + '1')
    if not node.left and not node.right:
        print(f"{node.symbol} -> {code}")

# Characters and their frequencies
chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [50, 9, 12, 13, 16, 45]

# Create a priority queue (min-heap)
nodes = [Node(freq[i], chars[i]) for i in range(len(chars))]
heapq.heapify(nodes)

# Build the Huffman tree
while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, new_node)

print_codes(nodes[0])
