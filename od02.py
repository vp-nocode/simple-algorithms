import numpy as np
import pandas as pd

print('== example implementation of Stack on numpy.array ==')
class Stack:
    def __init__(self):
        self.items = np.array([])

    def is_empty(self):
        if self.items.size == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items = np.append(self.items, item)

    def pop(self):
        if not self.is_empty():
            last = self.items.size-1
            pop_item = self.items[last]
            self.items = np.delete(self.items, last)
            return pop_item
        else:
            return None

    def peek(self):
        if not self.is_empty():
            last = self.items.size-1
            pop_item = self.items[last]
            return pop_item
        else:
            return None

stack = Stack()

print(stack.is_empty())
print(stack.items)

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.items)

print(stack.is_empty())

print(stack.peek())
stack.pop()

print(stack.items)

print('== example implementation of Graph on pandas.DataFrame ==')
class Graph:
    def __init__(self):
        self.graph = pd.DataFrame(columns=['source', 'destination'])

    def add_edge(self, source, destination):
        new_edge = pd.DataFrame({'source': [source], 'destination': [destination]})
        self.graph = pd.concat([self.graph, new_edge], ignore_index=True)

    def print_graph(self):
        if self.graph.empty:
            print("The graph is empty.")
        else:
            for source in self.graph['source'].unique():
                destinations = self.graph[self.graph['source'] == source]['destination'].tolist()
                print(f"{source} -> {', '.join(map(str, destinations))}")

# Example usage:
g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()
