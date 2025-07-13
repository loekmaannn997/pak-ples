import random
from algorithms import Sorting, Searching

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
