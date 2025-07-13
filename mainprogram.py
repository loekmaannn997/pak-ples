import random

class Sorting:
    def selection_sort(self, arr):
        for i in range(len(arr)):
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
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
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1

    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
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
        elif arr[mid] < target:
            return self.recursive_binary_search(arr, target, mid + 1, right)
        else:
            return self.recursive_binary_search(arr, target, left, mid - 1)

    def jump_search(self, arr, target):
        import math
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

def main():
    sorting = Sorting()
    searching = Searching()
    data = []
    sorted_data = []

    while True:
        print("\n=== MENU ===")
        print("1. Sorting")
        print("2. Searching")
        print("3. Keluar")
        choice = input("Pilih menu: ")

        if choice == '1':
            jumlah = int(input("Masukkan jumlah data yang ingin di-generate: "))
            data = [random.randint(1, 100) for _ in range(jumlah)]
            print("Data sebelum sorting:", data)

            print("Pilih metode sorting:")
            print("1. Selection Sort")
            print("2. Insertion Sort")
            print("3. Quick Sort")
            print("4. Bubble Sort")
            metode = input("Pilihan Anda: ")

            if metode == '1':
                sorted_data = sorting.selection_sort(data.copy())
            elif metode == '2':
                sorted_data = sorting.insertion_sort(data.copy())
            elif metode == '3':
                sorted_data = sorting.quick_sort(data.copy())
            elif metode == '4':
                sorted_data = sorting.bubble_sort(data.copy())
            else:
                print("Metode tidak ditemukan.")
                continue

            print("Data setelah sorting:", sorted_data)

        elif choice == '2':
            if not sorted_data:
                print("Data belum di-sort. Silakan lakukan sorting terlebih dahulu.")
                continue

            target = int(input("Masukkan nilai yang ingin dicari: "))
            print("Pilih metode searching:")
            print("1. Linear Search")
            print("2. Binary Search")
            print("3. Recursive Binary Search")
            print("4. Jump Search")
            metode = input("Pilihan Anda: ")

            if metode == '1':
                index = searching.linear_search(sorted_data, target)
            elif metode == '2':
                index = searching.binary_search(sorted_data, target)
            elif metode == '3':
                index = searching.recursive_binary_search(sorted_data, target, 0, len(sorted_data)-1)
            elif metode == '4':
                index = searching.jump_search(sorted_data, target)
            else:
                print("Metode tidak ditemukan.")
                continue

            if index != -1:
                print(f"Data {target} ditemukan di index ke-{index}")
            else:
                print(f"Data {target} tidak ditemukan.")

        elif choice == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()