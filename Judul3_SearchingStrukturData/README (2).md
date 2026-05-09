**Judul: Implementasi Binary Search pada Sistem Waiting List Sushi Tei**

**Deskripsi Singkat**

Program ini adalah simulasi waiting list Sushi Tei untuk mengecek nomor antrean dalam daftar yang sudah terurut secara ascending. Algoritma yang digunakan adalah Binary Search dengan kompleksitas O(log n), yang bekerja membagi dua area pencarian secara berulang hingga data ditemukan. Metode ini jauh lebih cepat dan efisien dibandingkan pencarian manual satu per satu.

**Source Code**


<img width="1919" height="1006" alt="Screenshot 2026-05-09 200728" src="https://github.com/user-attachments/assets/b153091c-5e12-4cc9-bba7-1e0b07e004dc" />
<img width="1919" height="1006" alt="Screenshot 2026-05-09 200728" src="https://github.com/user-attachments/assets/f5e0a395-dc18-4565-8a78-e23e3a0a0e72" />

Logika kode dimulai dengan menentukan batas pencarian melalui variabel low dan high. Program lalu menghitung titik tengah (mid) untuk membagi area data. Jika nomor antrean cocok dengan nilai tengah, posisi dan jumlah iterasi akan dikembalikan; namun jika lebih kecil, pencarian geser ke kiri, dan jika lebih besar geser ke kanan. Jika pencarian selesai tanpa hasil, program memberikan nilai -1 sebagai tanda data tidak ada.

**Output Program**

<img width="1918" height="1001" alt="Screenshot 2026-05-09 205941" src="https://github.com/user-attachments/assets/bcd53a18-f887-4fe0-8711-b394b44c8cdb" />

Output menampilkan dua kondisi utama, yaitu saat nomor ditemukan dan saat tidak ditemukan. Jika ditemukan, sistem menampilkan posisi antrean dan jumlah langkah yang dibutuhkan algoritma. Jika tidak ditemukan, sistem memberi tahu bahwa nomor mungkin sudah dipanggil atau input salah.

**Link YouTube**

(https://youtu.be/gp8nvOwCZJg) 
