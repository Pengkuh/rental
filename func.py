

# Daftar Mobil dan Harganya
merek = {
    "hb" : "Honda Brio",
    "mx" : "Mitsubitsi Expander",
    "ys" : "Yamaha Supra",
    "sc" : "Suzuki Carry",
    "ta" : "Toyota Avanza"
}
harga = {
    "hb" : 200000,
    "mx" : 250000,
    "ys" : 300000,
    "sc" : 150000,
    "ta" : 180000
}



# all Func

# Menu Rental Mobil
def menu ():
    print("\na. Rental Langsung\nb. Booking Mobil(MASIH PENGEMBANGAN)\nc. Data Client\n")

def tabel ():
    print("KODE NAMA")
    print(merek)
    print(" HARGA")
    print(harga,"\n")

# daftar client dafttar_client()
def daftar_client(data_client):
    for res in data_client:
        print("--------------------------")
        print(f"Nama     : {res['nama']}")
        print(f"Merek    : {res['jenis']}")
        print(f"Hari     : {res['hari']}")
        print(f"Harga    : {res['pay']}")
        print(f"Total    : {res['total']}")

# Rental Langsung rental_mobil()
def rental_mobil ():
    global merek
    global harga
 
    nama = input ("nama Lu      :   ")
    kode = input ("kode Mobil   :   ")
    hari = int(input ("Lama nya     :   "))
    jenis = merek[kode]
    pay = harga[kode]
    total = hari * pay

    # Masuk Ke Log
    res = {
    "nama" : nama,
    "merek" : jenis,
    "hari"  : hari,
    "harga" : pay,
    "total" : total
    }

    daftar_client(res)

    return res


       
