"""
https://stepik.org/lesson/13240/step/8?unit=3426
"""
class HeapMax:
    def __init__(self):
        self.heap = []

    def __sift_down(self, i: int):
        while 2 * i + 1 < len(self.heap):
            left = 2 * i + 1
            right = 2 * i + 2
            if right < len(self.heap) and self.heap[right] > self.heap[left]:
                j = right
            else:
                j = left
            if self.heap[i] >= self.heap[j]:
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def extract_max(self):
        heap_last = len(self.heap) - 1
        self.heap[0], self.heap[heap_last] = self.heap[heap_last], self.heap[0]
        max_value = self.heap.pop()
        self.__sift_down(0)
        print(max_value)

    def __sift_up(self, i: int):
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def insert(self, x: int):
        self.heap.append(x)
        self.__sift_up(len(self.heap) - 1)


if __name__ == "__main__":
    heap = HeapMax()
    n = int(input())
    for _ in range(n):
        operation = input()
        if operation == 'ExtractMax':
            heap.extract_max()
        else:
            num = int(operation.split()[-1])
            heap.insert(num)