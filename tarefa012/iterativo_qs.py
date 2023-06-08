import random
import time

class QuickSort:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort(self, arr):
        stack = []
        stack.append((0, len(arr) - 1))

        while stack:
            low, high = stack.pop()
            if low < high:
                pi = self.partition(arr, low, high)
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))

    def sort(self, arr):
        self.quicksort(arr)

class TesteQuickSort:
    def generate_random_array(self, size):
        return [random.randint(0, 1000) for _ in range(size)]

    def test(self, sizes):
        for size in sizes:
            arr = self.generate_random_array(size)
            
            # QuickSort
            qs = QuickSort()
            start_time = time.time()
            qs.sort(arr)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Tempo de execução do QuickSort para {size} elementos: {execution_time} segundos.")

teste = TesteQuickSort()
teste.test([100, 1000, 10000])
