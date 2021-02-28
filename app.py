# program rental mobil basis desktop
# import func
import func

# list dictionary
data_client = []
data_client.append({
    "nama" : "default",
    "merek" : "default",
    "hari"  : 0,
    "harga" : 0,
    "total" : 0
})

# pengulangan
lagi = "y"
while (lagi == "y" ):

# Menu Care car
    
    func.menu()

    x = input("input : ")
    if x == "a" :
        data = func.rental_mobil()
        data_client.append(data)

    elif x == "c" :
        func.daftar_client(data_client)

    lagi = input("lagi : ")
    if lagi == "n":
        break

