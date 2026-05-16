**Judul:** Sistem Antrean Konser Taylor Swift (Queue Array)

**Deskripsi:**
Program ini dibuat untuk mensimulasikan sistem antrean fans (Swifties) yang mau masuk ke venue konser Taylor Swift. Tujuannya supaya proses masuk penonton lebih teratur dan gak melebihi kapasitas tempat yang ada. Struktur data yang dipakai adalah Queue Array. Alasan pakai metode ini karena sangat pas dengan prinsip antrean "siapa cepat dia dapat" (FIFO), dan juga lebih hemat memori karena slot yang sudah kosong bisa dipakai lagi buat penonton baru tanpa harus buat array baru.

**Source Code:**
<img width="1702" height="736" alt="image" src="https://github.com/user-attachments/assets/369fd694-cc34-4c1e-894d-e5a0e15ca87a" />
<img width="1693" height="743" alt="image" src="https://github.com/user-attachments/assets/cbbbb3be-e75e-49d1-b08f-1c66b68ec1c5" />
<img width="1701" height="574" alt="image" src="https://github.com/user-attachments/assets/6a9c6c66-82cd-4353-a57a-259538371004" />
<img width="1690" height="535" alt="image" src="https://github.com/user-attachments/assets/38c82fce-4769-4df1-856e-d286d810e2af" />
<img width="1700" height="572" alt="image" src="https://github.com/user-attachments/assets/a0427e8d-e57f-4f62-ab22-857e765fa241" />

Logika kodingan ini berpusat pada cara ngatur antrean biar bisa muter terus selama kuota masih ada. Dimulai dari fungsi (init) yang nyiapin tempat antrean dan pointer depan (front_idx) serta belakang (rear_idx) yang awalnya dikasih nilai -1 sebagai tanda kalau antrean masih kosong. Program ini juga punya fungsi buat ngecek kondisi antrean lewat (is_empty) dan (is_full) yang pakai rumus modulo (%) supaya pergerakan pointernya bisa melingkar di dalam array.

Pas ada fans yang datang, fungsi (enqueue) bakal ngecek kuota dulu; kalau aman, nomor tiketnya bakal dimasukin ke posisi paling belakang dan sistem otomatis ngasih tau estimasi waktu nunggunya. Kalau fans paling depan sudah boleh masuk venue, fungsi (dequeue) bakal jalan buat manggil orang tersebut dan majuin antrean ke orang berikutnya. Selain itu, ada fungsi (peek) buat ngintip siapa yang paling depan dan (display) buat ngeliat seluruh list fans yang lagi antre secara real-time. Semua ini diatur lewat menu interaktif di fungsi (main) yang sudah aman dari error kalau kita salah ketik input.

**Output:**
<img width="1824" height="748" alt="Screenshot 2026-05-15 152641" src="https://github.com/user-attachments/assets/688909d8-7c4e-4279-9744-6e111d07c572" />
<img width="1822" height="705" alt="image" src="https://github.com/user-attachments/assets/4193ae25-1102-4dc9-ab0c-253631ebaa8a" />
<img width="1824" height="225" alt="image" src="https://github.com/user-attachments/assets/10177fea-2d20-433f-ba12-63a48b3d181b" />

Jadi pas kita masukin nomor tiket (Enqueue) seperti ID 100 dan 101, program langsung nampilin konfirmasi kalau mereka sudah masuk list antrean bareng estimasi waktu tunggunya. Kita juga bisa liat urutan lengkapnya lewat menu "Tampilkan Semua Fans".

Pas kita pilih "Panggil Antrean" (Dequeue), program bakal manggil orang yang pertama kali daftar (ID 100) buat masuk ke venue, ini ngebuktiin kalau sistemnya sudah beneran FIFO. Kalau semua sudah masuk dan antrean kosong, program bakal ngasih tau dengan sopan kalau nggak ada lagi yang perlu dipanggil, jadi sistemnya tetap stabil.

**Link YouTube:**

https://youtu.be/rLpo-A21rpo?feature=shared
