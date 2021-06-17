import modul_crud
import os

def menu():
    pilihan = 0
    while(pilihan == 0 or pilihan > 4) :
        print(20*"=", "M E N U   A W A L", 20*"=")
        print("1. Input data")
        print("2. Lihat Data")
        print("3. Delete Data")
        print("4. Exit\n")
        pilihan = int(input("Pilihan (1-4): "))

    if pilihan == 1:
       modul_crud.inputData() 
       menu()
    elif pilihan == 2:
        modul_crud.lihatData()
        menu()
    elif pilihan == 3:
        modul_crud.deleteData()
        menu()
    elif pilihan == 4:
        exit()

menu()
