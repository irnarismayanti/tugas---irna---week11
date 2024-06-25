def search_drama(drama_list, query):
    # Fungsi untuk mencari drama berdasarkan judul
    results = []
    for drama in drama_list:
        if query.lower() in drama.lower():
            results.append(drama)
    return results

def main():
    # Daftar judul drama Korea
    dramas = [
        "Voice",
        "The First Responders",
        "Class of Lies",
        "Partner of Justice",
        "Train",
        "Tomorrow",
        "Memorist",
        "Mouse",
        "Signal",
        "Save Me"
    ]

    # Menampilkan daftar judul drama yang tersedia
    print("Daftar judul drama Korea yang tersedia:")
    for drama in dramas:
        print(f"- {drama}")

    while True:
        # Meminta input dari pengguna
        query = input("\nMasukkan judul drama yang ingin dicari (atau ketik 'exit' untuk keluar): ")

        # Keluar dari program jika pengguna mengetik 'exit'
        if query.lower() == 'exit':
            print("Terima kasih telah menggunakan program ini!")
            break

        # Mencari drama berdasarkan input pengguna
        results = search_drama(dramas, query.lower())

        # Menampilkan hasil pencarian
        if results:
            print("\nDrama yang ditemukan:")
            for drama in results:
                print(f"Judul: {drama}")
        else:
            print("\nDrama tidak ditemukan. Coba lagi.")

if __name__ == "__main__":
    main()
