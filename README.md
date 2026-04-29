**a. Judul Program**

Program ini berjudul **“Implementasi Singly Linked List untuk Daftar Belanja Skincare”,** yang bertujuan untuk mengelola data daftar belanja menggunakan struktur data linked list.

**b. Deskripsi Singkat**

Program ini dibuat untuk membantu menyimpan dan menampilkan daftar belanja skincare dengan menggunakan struktur data **Singly Linked List**. Dalam program ini, setiap item skincare disimpan dalam bentuk node yang saling terhubung satu sama lain. Dengan menggunakan linked list, data dapat ditambahkan secara dinamis tanpa harus menentukan ukuran di awal seperti pada array. Program ini memungkinkan pengguna untuk menambahkan beberapa item skincare ke dalam daftar, kemudian menampilkannya secara berurutan sesuai dengan data yang telah dimasukkan.


**c. Source Code**

<img width="1316" height="805" alt="Screenshot 2026-04-29 200554" src="https://github.com/user-attachments/assets/3a4f57e6-fdea-4a69-9d4b-e488f831e7b7" />
<img width="1352" height="371" alt="Screenshot 2026-04-29 200630" src="https://github.com/user-attachments/assets/3f7e4359-4d80-47fb-a8fc-4b46bd815817" />

Program ini dimulai dengan pembuatan class `Node` yang berfungsi sebagai tempat penyimpanan data dalam linked list. Setiap node memiliki dua atribut, yaitu `data` yang berisi nama produk skincare dan `next` yang digunakan untuk menunjuk ke node berikutnya. Setelah itu, dibuat class `SkincareList` yang berfungsi untuk mengelola keseluruhan linked list, dengan atribut `head` sebagai penunjuk ke node pertama.

Untuk menambahkan data ke dalam list, digunakan method `tambah_item()`. Pada method ini, program akan membuat node baru berdasarkan data yang dimasukkan. Jika linked list masih kosong, maka node tersebut langsung dijadikan sebagai `head`. Namun jika sudah terdapat data, program akan menelusuri hingga ke node terakhir menggunakan perulangan, kemudian menambahkan node baru di bagian akhir list.

Selain itu, terdapat method `cetak_daftar()` yang digunakan untuk menampilkan seluruh isi linked list. Proses ini dilakukan dengan menelusuri setiap node mulai dari `head` hingga ke node terakhir, kemudian mencetak data yang tersimpan di dalamnya secara berurutan. Pada bagian utama program, dibuat objek dari `SkincareList`, lalu ditambahkan beberapa item seperti Facial Wash, Toner, Serum, dan Sunscreen menggunakan method yang telah dibuat, dan akhirnya ditampilkan ke layar.


**d. Output Program**

<img width="1207" height="290" alt="Screenshot 2026-04-29 200709" src="https://github.com/user-attachments/assets/8c39d139-90c7-4493-ad2b-04cce8e9325c" />
Output dari program ini menampilkan daftar belanja skincare yang telah dimasukkan sebelumnya. Program akan mencetak teks "Daftar Belanja Skincare:" sebagai judul, kemudian menampilkan setiap item seperti Facial Wash, Toner, Serum, dan Sunscreen dalam bentuk daftar. Urutan data yang ditampilkan sesuai dengan urutan saat data dimasukkan ke dalam linked list, karena proses penambahan dilakukan di bagian akhir (append). Hal ini menunjukkan bahwa struktur data linked list telah bekerja dengan baik, serta program dapat berjalan tanpa error dan menghasilkan output yang sesuai dengan tujuan yang diharapkan.


**e. Link YouTube**
https://youtu.be/P00aAvTf-Io?si=NoSEpcCeqKRts09U
