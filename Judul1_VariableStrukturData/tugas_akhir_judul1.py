#Implementasi Singly Linked List untuk Daftar Belanja Skincare Olif

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SkincareList:
    def __init__(self):
        self.head = None

    def tambah_item(self, produk):
        new_node = Node(produk)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def cetak_daftar(self):
        print("Daftar Belanja Skincare:")
        curr = self.head
        while curr:
            print(f"- {curr.data}")
            curr = curr.next

#Main Program
if __name__ == "__main__":
    belanja = SkincareList()
    
    # Menambah data sesuai tugas
    belanja.tambah_item("Facial Wash")
    belanja.tambah_item("Toner")
    belanja.tambah_item("Serum")
    belanja.tambah_item("Sunscreen")

    belanja.cetak_daftar()