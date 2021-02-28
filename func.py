
# Daftar Mobil dan Harganya
merek = {
    "hb" : "Honda Brio",
    "mx" : "Mitsubitsi Expander"
}
harga = {
    "hb" : 200000,
    "mx" : 250000
}



# all Func

# Menu Rental Mobil
def menu ():
    print("\na. Rental Langsung\nb. Booking Mobil(MASIH PENGEMBANGAN)\nc. Data Client\n")

# daftar client dafttar_client()
def daftar_client(data_client):
    for res in data_client:
        print("--------------------------")
        print(f"Nama     : {res['nama']}")
        print(f"Merek    : {res['merek']}")
        print(f"Hari     : {res['hari']}")
        print(f"Harga    : {res['harga']}")
        print(f"Total    : {res['total']}")

# Rental Langsung rental_mobil()
def rental_mobil ():
    global merek
    global harga
 
    nama = input ("nama Lu      :   ")
    kode = input ("kode Mobil   :   ")
    hari = int(input ("Lama nya     :   "))
    merek = merek[kode]
    harga = harga[kode]
    total = hari * harga

    print("\n")
    print("Nama Pemesan : ",nama)
    print("Merek Mobil  : ",merek)
    print("Harga Mobil  : ",harga)
    print("Jumlah Hari  : ",hari)
    print('Total Biaya  : Rp.',"{:,}".format(int(total)).replace(',','.'))


    # Masuk Ke Log
    res = {
    "nama" : nama,
    "merek" : merek,
    "hari"  : hari,
    "harga" : harga,
    "total" : total
    }

    return res


       
