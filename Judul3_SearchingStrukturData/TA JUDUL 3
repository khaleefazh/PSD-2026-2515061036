def binary_search_sushi(data_antrean, target_nomor):
    low = 0
    high = len(data_antrean) - 1
    iterasi = 0
    
    while low <= high:
        iterasi += 1
        mid = (low + high) // 2
        
        # Mengecek nilai tengah
        if data_antrean[mid] == target_nomor:
            return mid, iterasi
        
        # Jika nomor target lebih kecil, cari di sebelah kiri
        elif target_nomor < data_antrean[mid]:
            high = mid - 1
            
        # Jika nomor target lebih besar, cari di sebelah kanan
        else:
            low = mid + 1
            
    return -1, iterasi

# Nomor antrean yang sedang menunggu dan sudah terurut
antrean_aktif = [101, 105, 110, 112, 115, 120, 124, 130]

print("SUSHI TEI WAITING LIST")
print(f"Antrean saat ini: {antrean_aktif}")
cari_nomor = int(input("Masukkan nomor antrean Anda: "))

indeks, total_cek = binary_search_sushi(antrean_aktif, cari_nomor)

if indeks != -1:
    print(f"\n[HASIL] Nomor antrean {cari_nomor} ditemukan!")
    print(f"Status: Masih dalam daftar tunggu di posisi ke-{indeks + 1}.")
    print(f"Sistem menemukan data Anda dalam {total_cek} kali langkah.")
else:
    print(f"\n[HASIL] Nomor antrean {cari_nomor} tidak ditemukan.")
    print("Kemungkinan nomor Anda sudah dipanggil atau salah input.")