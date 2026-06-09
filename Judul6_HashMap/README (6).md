**Judul Program**

Data Ranking Player Mobile Game

**Deskripsi Program**

Program ini menggunakan struktur data Hash Map dengan metode Separate Chaining untuk menyimpan data ranking player game. Data yang disimpan itu ID Player sebagai key dan poin rank sebagai value. Metode Separate Chaining digunakan untuk menangani collision dengan bantuan linked list.

**Penjelasan Source Code**
<img width="920" height="416" alt="image" src="https://github.com/user-attachments/assets/17bc94a8-f7a3-47ec-8d51-d2b5cd6a7e47" />
<img width="920" height="419" alt="image" src="https://github.com/user-attachments/assets/27f94275-933d-4ead-a1a1-5a006be7a77a" />
<img width="916" height="410" alt="image" src="https://github.com/user-attachments/assets/64e714a9-b399-464d-b76d-3fb23d89edca" />
<img width="926" height="436" alt="image" src="https://github.com/user-attachments/assets/f1e5284c-5aaf-4980-96c0-acbdfb7a4591" />
Program terdiri dari class Node dan HashMapSeparateChaining. Class Node digunakan untuk menyimpan data pada linked list, sedangkan HashMapSeparateChaining digunakan untuk mengelola hash table. Fungsi insert() digunakan untuk menambah data, search() untuk mencari data berdasarkan key, remove_key() untuk menghapus data, dan display() untuk menampilkan seluruh isi hash table. Pada fungsi main(), program menambahkan beberapa data player, menampilkan data, mencari data tertentu, lalu menghapus salah satu data dan menampilkan hasilnya kembali.

**Penjelasan Output**
<img width="910" height="364" alt="image" src="https://github.com/user-attachments/assets/2b8b678b-fe6f-4407-9797-630b1848768a" />
Saat program dijalankan, data player berhasil masuk ke dalam hash table. Beberapa data memiliki indeks hash yang sama sehingga disimpan dalam satu bucket menggunakan linked list. Setelah itu program mencari ID Player 111 dan berhasil menampilkan poin rank miliknya. Kemudian data dengan ID Player 111 dihapus dan saat hash table ditampilkan kembali, data tersebut sudah tidak ada sementara data lainnya tetap tersimpan dengan baik.

**Link Youtube**
https://youtu.be/s9XwmNaYnxE?feature=shared
