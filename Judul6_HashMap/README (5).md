**Judul Program**

Data Ranking Player Mobile Game

**Deskripsi Program**

Program ini menggunakan struktur data Hash Map dengan metode Separate Chaining untuk menyimpan data ranking player game. Data yang disimpan itu ID Player sebagai key dan poin rank sebagai value. Metode Separate Chaining digunakan untuk menangani collision dengan bantuan linked list.

**Penjelasan Source Code**

Program terdiri dari class Node dan HashMapSeparateChaining. Class Node digunakan untuk menyimpan data pada linked list, sedangkan HashMapSeparateChaining digunakan untuk mengelola hash table. Fungsi insert() digunakan untuk menambah data, search() untuk mencari data berdasarkan key, remove_key() untuk menghapus data, dan display() untuk menampilkan seluruh isi hash table. Pada fungsi main(), program menambahkan beberapa data player, menampilkan data, mencari data tertentu, lalu menghapus salah satu data dan menampilkan hasilnya kembali.

**Penjelasan Output**

Saat program dijalankan, data player berhasil masuk ke dalam hash table. Beberapa data memiliki indeks hash yang sama sehingga disimpan dalam satu bucket menggunakan linked list. Setelah itu program mencari ID Player 111 dan berhasil menampilkan poin rank miliknya. Kemudian data dengan ID Player 111 dihapus dan saat hash table ditampilkan kembali, data tersebut sudah tidak ada sementara data lainnya tetap tersimpan dengan baik.

**Link Youtube**
https://youtu.be/s9XwmNaYnxE?feature=shared
