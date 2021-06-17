import os
def inputData():
    nama = input("Nama              : ")
    ttl = input("Tempat/Tgl Lahir  : ")
    jenkel = input("Jenis kelamin     : ")
    alamat = input("Alamat            : ")
    rt_rw = input("\tRT/RW     : ")
    kel_desa = input("\tKel/Desa  : ")
    kecamatan = input("\tKecamatan : ")
    agama = input("Agama             : ")
    status = input("Status Perkawinan : ")
    pekerjaan = input("Pekerjaan         : ")
    kewarganegaraan = input("Kewarganegaraan   : ")
    berlaku = input("Berlaku hingga    : ")
    
    exist = os.path.isfile('data.txt')
    if exist == False:
        f = open("data.txt", "x")
        nomor = 1
    else:
        f = open("data.txt", "r")
        f = open("data.txt", "a")
        
    data = f'{nama}, {ttl}, {jenkel}, {alamat}, {rt_rw}, {kel_desa}, {kecamatan}, {agama}, {status}, {pekerjaan}, {kewarganegaraan}, {berlaku}\n'

    f.write(data)
    f.close()
    print("\nData berhasil diinput")
    
def lihatData():
    exist = os.path.isfile('data.txt')
    if exist == False:
        fileNotFound()
        return 0

    print(40*"=")
    all_data = []

    f = open("data.txt", "r")
    count = f.readlines() 
    lines = len(count)
    f.close()

    print("Banyak data : ",lines)
    if lines == 0:
        print("Data Kosong")
        return 0

    pilih = 0
    while(pilih == 0 or pilih > lines):
        question = f"Tampilkan data ke? (1-{lines}) : "
        pilih = int(input(question))
        pilihan = pilih - 1
    print("\n")

    f = open("data.txt", "r")
    for line in f:
        data = line.split(", ")
        all_data.append(data)
    f.close()

# show all data
#    for i in range(lines):
#        hasil = f"""        Nama             : {all_data[i][0]}
#        Tempat/Tgl Lahir : {all_data[i][1]}
#       Jenis kelamin    : {all_data[i][2]}
#        Alamat           : {all_data[i][3]}
#            RT/RW        : {all_data[i][4]}
#           Kel/Desa     : {all_data[i][5]}
#            Kecamatan    : {all_data[i][6]}
#        Agama            : {all_data[i][7]}
#        Status Perkawinan: {all_data[i][8]}
#        Pekerjaan        : {all_data[i][9]}
#        Kewarganegaraan  : {all_data[i][10]}
#        Berlaku hingga   : {all_data[i][11]}
#        """
#        print(hasil)

    hasil = f"""    Nama             : {all_data[pilihan][0]}
    Tempat/Tgl Lahir : {all_data[pilihan][1]}
    Jenis kelamin    : {all_data[pilihan][2]}
    Alamat           : {all_data[pilihan][3]}
        RT/RW        : {all_data[pilihan][4]}
        Kel/Desa     : {all_data[pilihan][5]}
        Kecamatan    : {all_data[pilihan][6]}
    Agama            : {all_data[pilihan][7]}
    Status Perkawinan: {all_data[pilihan][8]}
    Pekerjaan        : {all_data[pilihan][9]}
    Kewarganegaraan  : {all_data[pilihan][10]}
    Berlaku hingga   : {all_data[pilihan][11]}
            """
    print(hasil)

def deleteData():
    exist = os.path.isfile('data.txt')
    if exist == False:
        fileNotFound()
        return 0

    f = open("data.txt", "r")
    count = f.readlines() 
    lines = len(count)
    f.close()
    

    print("Banyak data : ",lines)
    if lines == 0:
        print("Data kosong")
        return 0;


    pilih = 0
    while(pilih == 0 or pilih > lines):
        question = f"Hapus data ke? (1-{lines}) : "
        pilih = int(input(question))
        pilihan = pilih - 1

    del count[pilihan]
    f = open("data.txt", "w+")
    for line in count:
        f.write(line)
    f.close()
    print("Data pada index ke ", pilih , " Berhasil Dihapus")

def fileNotFound():
    print("file tidak ada, silahkan inputkan data dahulu")
