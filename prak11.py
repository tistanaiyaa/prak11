# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:33:32 2024

@author: Lenovo
"""

class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan
        Mahasiswa.total_mahasiswa += 1

    def tampilkan_data(self):
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Angkatan: ", self.angkatan)

if __name__ == "__main__":
    nama = input("Masukkan Namamu: ")
    nim = input("Masukkan NIM kamu: ")
    angkatan = input("Masukkan Tahun Angkatanmu: ")

    mahasiswa1 = Mahasiswa(nama, nim, angkatan)

    print("\nData Mahasiswa")
    mahasiswa1.tampilkan_data()

    print("\nTotal Mahasiswa:", Mahasiswa.total_mahasiswa)
