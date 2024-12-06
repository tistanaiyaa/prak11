# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:33:11 2024

@author: Lenovo
"""

class Data:
    def __init__(self):
        self.__nama = None
        self.__nilai = None

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_nilai(self):
        return self.__nilai

    def set_nilai(self, nilai):
        self.__nilai = nilai

    def hapus_data(self):
        self.__nama = None
        self.__nilai = None


def main():
    data = Data()

    while True:
        print("\n===== Program OOP =====")
        print("1. Mendeklarasikan Objek")
        print("2. Menampilkan Objek")
        print("3. Merubah Nilai Objek")
        print("4. Menghapus Objek")
        print("5. Keluar Dari Program")

        pilihan = input("Masukkan Pilihan Berupa Angka (1/2/3/4/5): ")

        if pilihan == "1":
            nama = input("Masukkan Namamu: ")
            nilai = input("Masukkan Nilai: ")
            data.set_nama(nama)
            data.set_nilai(nilai)
            print("Data Berhasil Ditambahkan")

        elif pilihan == "2":
            print("\n===== Menampilkan Objek =====")
            nama = data.get_nama()
            nilai = data.get_nilai()
            print(f"Nama: {nama}")
            print(f"Nilai: {nilai}")

        elif pilihan == "3":
            print("\n===== Merubah Nilai Objek =====")
            atribut = input("Apa yang ingin diubah (Nama/Nilai)? ").strip().lower()
            if atribut == "nama":
                nama_baru = input("Masukkan Nama Baru: ")
                data.set_nama(nama_baru)
                print("Data Nama Berhasil Diubah")
            elif atribut == "nilai":
                nilai_baru = input("Masukkan Nilai Baru: ")
                data.set_nilai(nilai_baru)
                print("Data Nilai Berhasil Diubah")
            else:
                print("Pilihan tidak valid!")

        elif pilihan == "4":
            data.hapus_data()
            print("Data Berhasil Dihapus")

        elif pilihan == "5":
            print("Terima Kasih Sudah Menggunakan Program Saya")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi!")


if __name__ == "__main__":
    main()