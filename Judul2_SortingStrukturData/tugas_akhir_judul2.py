def tukar(arr, i, j): 
    temp = arr[i] 
    arr[i] = arr[j] 
    arr[j] = temp 


def urutan_makeup(nama):
    if nama == "cushion":
        return 1
    elif nama == "contour":
        return 2
    elif nama == "blush":
        return 3
    elif nama == "eyeshadow":
        return 4
    elif nama == "eyeliner":
        return 5
    elif nama == "maskara":
        return 6
    elif nama == "lipstik":
        return 7
    else:
        return 999  # kalau gak dikenal, taruh di belakang


def bubble_sort(arr, n): 
    for i in range(n - 1): 
        for j in range(n - i - 1): 
            if urutan_makeup(arr[j]) > urutan_makeup(arr[j + 1]): 
                tukar(arr, j, j + 1) 


def main(): 
    try: 
        n = int(input("Masukkan jumlah elemen make up: ")) 
    except ValueError: 
        print("Input tidak valid!") 
        return

    arr = [] 
    print("Masukkan elemen make up:")

    for i in range(n): 
        elemen = input().lower()
        arr.append(elemen)

    print(f"Array sebelum diurutkan: {arr}") 

    bubble_sort(arr, n) 

    print("Urutan make up yang benar:", end=" ") 
    for i in range(n): 
        print(arr[i], end=" ") 
    print() 


if __name__ == "__main__": 
    main()