import random
import math

class Sorting:
    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

class Searching:
    def linear_search(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    def binary_search(self, arr, target):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def recursive_binary_search(self, arr, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return self.recursive_binary_search(arr, target, left, mid - 1)
        else:
            return self.recursive_binary_search(arr, target, mid + 1, right)

    def jump_search(self, arr, target):
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        while prev < n and arr[min(step, n)-1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        for i in range(prev, min(step, n)):
            if arr[i] == target:
                return i
        return -1