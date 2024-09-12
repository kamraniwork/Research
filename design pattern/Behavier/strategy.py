# Define sorting strategies
class BubbleSort:
    def sort(self, arr):
        # Sorting logic
        return sorted(arr)

class MergeSort:
    def sort(self, arr):
        # Sorting logic
        return sorted(arr)

class QuickSort:
    def sort(self, arr):
        # Sorting logic
        return sorted(arr)

# Context class
class SortContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, arr):
        return self.strategy.sort(arr)

# Usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
context = SortContext(BubbleSort())
sorted_arr = context.execute_strategy(arr)
print(sorted_arr)
