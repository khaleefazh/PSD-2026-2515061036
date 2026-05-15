**Judul:** Sistem Antrean Konser Taylor Swift (Queue Array)

**Deskripsi:**
Program ini dibuat untuk mensimulasikan sistem antrean fans (Swifties) yang mau masuk ke venue konser Taylor Swift. Tujuannya supaya proses masuk penonton lebih teratur dan gak melebihi kapasitas tempat yang ada. Struktur data yang dipakai adalah Queue Array. Alasan pakai metode ini karena sangat pas dengan prinsip antrean "siapa cepat dia dapat" (FIFO), dan juga lebih hemat memori karena slot yang sudah kosong bisa dipakai lagi buat penonton baru tanpa harus buat array baru.

**Source Code:**
<img width="1700" height="745" alt="image" src="https://github.com/user-attachments/assets/5cd56d59-8574-4f6f-8217-4608eed673ee" />
<img width="1693" height="743" alt="image" src="https://github.com/user-attachments/assets/cbbbb3be-e75e-49d1-b08f-1c66b68ec1c5" />
<img width="1701" height="574" alt="image" src="https://github.com/user-attachments/assets/6a9c6c66-82cd-4353-a57a-259538371004" />
<img width="1701" height="829" alt="image" src="https://github.com/user-attachments/assets/7c16a2e6-a550-4134-8d91-eeb32a94801a" />
<img width="1703" height="234" alt="image" src="https://github.com/user-attachments/assets/0719ba48-dff6-4ddf-8017-e0009a696d17" />

Logika kodingan ini berpusat pada cara ngatur antrean biar bisa muter terus selama kuota masih ada. Dimulai dari fungsi (init) yang nyiapin tempat antrean dan pointer depan (front_idx) serta belakang (rear_idx) yang awalnya dikasih nilai -1 sebagai tanda kalau antrean masih kosong. Program ini juga punya fungsi buat ngecek kondisi antrean lewat (is_empty) dan (is_full) yang pakai rumus modulo (%) supaya pergerakan pointernya bisa melingkar di dalam array.

Pas ada fans yang datang, fungsi (enqueue) bakal ngecek kuota dulu; kalau aman, nomor tiketnya bakal dimasukin ke posisi paling belakang dan sistem otomatis ngasih tau estimasi waktu nunggunya. Kalau fans paling depan sudah boleh masuk venue, fungsi (dequeue) bakal jalan buat manggil orang tersebut dan majuin antrean ke orang berikutnya. Selain itu, ada fungsi (peek) buat ngintip siapa yang paling depan dan (display) buat ngeliat seluruh list fans yang lagi antre secara real-time. Semua ini diatur lewat menu interaktif di fungsi (main) yang sudah aman dari error kalau kita salah ketik input.

**Output:**
<img width="1826" height="790" alt="image" src="https://github.com/user-attachments/assets/eb724dd1-b7fb-4451-a35f-f1860d78467e" />
<img width="1824" height="714" alt="image" src="https://github.com/user-attachments/assets/e14b5a2a-d3e9-4a1f-8247-351ef82a11a9" />
<img width="1826" height="291" alt="image" src="https://github.com/user-attachments/assets/d94f9010-87a2-497e-ba04-3ad40789753b" />

Jadi pas kita masukin nomor tiket (Enqueue) seperti ID 100 dan 101, program langsung nampilin konfirmasi kalau mereka sudah masuk list antrean bareng estimasi waktu tunggunya. Kita juga bisa liat urutan lengkapnya lewat menu "Tampilkan Semua Fans".

Pas kita pilih "Panggil Antrean" (Dequeue), program bakal manggil orang yang pertama kali daftar (ID 100) buat masuk ke venue, ini ngebuktiin kalau sistemnya sudah beneran FIFO. Kalau semua sudah masuk dan antrean kosong, program bakal ngasih tau dengan sopan kalau nggak ada lagi yang perlu dipanggil, jadi sistemnya tetap stabil.

**Link YouTube:**

[Tempel Link YouTube Kamu di Sini]
