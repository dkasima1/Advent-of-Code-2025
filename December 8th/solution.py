import os
import heapq
import math

class solution:

    input_arr = []
    heap = []
    parent = []
    size = []

    def read_txt_file(self, filepath):
        with open(filepath, 'r') as f:
            for line in f:
                curr = line.strip()
                curr = curr.split(',')
                for i in range(len(curr)):
                    curr[i] = int(curr[i])
                self.input_arr.append(curr)
    
    def build_heap(self):
        for i in range(len(self.input_arr)):
            for j in range(i+1, len(self.input_arr)):
                node1 = self.input_arr[i]
                node2 = self.input_arr[j]
                dist = math.sqrt((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2 + (node1[2] - node2[2])**2)
                heapq.heappush(self.heap, (dist, i, j))
    
    def make_set(self):
        for i in range(len(self.input_arr)):
            self.parent.append(i)
            self.size.append(1)
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        if self.size[root1] >= self.size[root2]:
            self.size[root1] += self.size[root2]
            self.parent[root2] = root1
        else:
            self.size[root2] += self.size[root1]
            self.parent[root1] = root2
    
    def compress_tree(self):
        for i in range(len(self.parent)):
            self.find(i)
    
    def add_circuits(self, count):
        for i in range(count):
            smallest = heapq.heappop(self.heap)
            node1 = smallest[1]
            node2 = smallest[2]
            self.union(node1, node2)
            if self.size[self.parent[node1]] == len(self.parent) or self.size[self.parent[node2]] == len(self.parent):
                print(self.input_arr[node1][0] * self.input_arr[node2][0])
                break
        self.compress_tree()
    
    def find_q2_answer(self):
        self.add_circuits(len(self.heap))
    
    def find_q1_answer(self, circuits):
        maxHeap = []
        countDict = {}
        for i in range(len(self.parent)):
            if self.parent[i] in countDict:
                countDict[self.parent[i]] += 1
            else:
                countDict[self.parent[i]] = 1
        for k,v in countDict.items():
            heapq.heappush(maxHeap, (-1 * v, k))
        power = 1
        for i in range(circuits):
            val = heapq.heappop(maxHeap)
            power *= (val[0] * -1)
        return power

if __name__ == "__main__":
    print(os.getcwd())
    final = solution()
    final.read_txt_file('./input.txt')
    final.build_heap()
    final.make_set()
    # final.add_circuits(1000)
    # print(final.find_q1_answer(3))
    final.find_q2_answer()