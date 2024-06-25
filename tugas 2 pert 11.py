def binary_search_odd(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Jika arr[mid] adalah angka ganjil
        if arr[mid] == target:
            return mid
        
        # Jika arr[mid] adalah angka genap atau lebih kecil dari target, cari di sebelah kanan mid
        elif arr[mid] % 2 == 0 or arr[mid] < target:
            left = mid + 1
        
        # Jika arr[mid] lebih besar dari target, cari di sebelah kiri mid
        else:
            right = mid - 1
    
    return -1  # Jika tidak ditemukan

def main():
    # Meminta input dari pengguna untuk angka-angka ganjil yang terurutkan
    input_str = input("Masukkan angka-angka ganjil terurutkan (pisahkan dengan spasi): ")
    arr = list(map(int, input_str.split()))
    
    # Memeriksa apakah arr terurut dan hanya berisi angka ganjil
    for i in range(len(arr) - 1):
        if arr[i] % 2 == 0 or arr[i] > arr[i + 1]:
            print("Maaf, input harus berupa angka ganjil yang terurut.")
            return
    
    # Meminta input dari pengguna untuk angka ganjil yang ingin dicari
    target = int(input("Masukkan angka ganjil yang ingin dicari: "))
    
    # Melakukan binary search untuk mencari angka yang ingin dicari
    index = binary_search_odd(arr, target)
    
    # Menampilkan hasil pencarian
    if index != -1:
        print(f"Angka ganjil {target} ditemukan pada indeks ke-{index}.")
    else:
        print(f"Angka ganjil {target} tidak ditemukan dalam array.")

if __name__ == "__main__":
    main()
