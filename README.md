# Tugas-1
TUGAS 1 – Algoritma dan Pemrograman Dasar
- NIM: 2615323045
- Kelas: 1A
- Prodi: D3 Manajemen Informatika
- Politeknik Negeri Bali

---

SOAL 1 – REKAP NILAI MAHASISWA

A. Hasil Program

Program menghitung nilai akhir dari tugas, UTS, dan UAS dengan bobot masing-masing 30%, 30%, dan 40%.

=== TABEL REKAPITULASI NILAI MAHASISWA ===
Nama       | Nilai Akhir | Nilai Huruf | Keterangan
-------------------------------------------------------
Andi       | 81.00       | B           | Lulus
Bunga      | 87.70       | A           | Lulus
Citra      | 51.50       | D           | Tidak Lulus
Dimas      | 72.50       | B           | Lulus
Eka        | 35.00       | E           | Tidak Lulus
-------------------------------------------------------
Rata-rata nilai akhir kelas : 65.54
Banyaknya mahasiswa yang lulus : 3

B. Desain Fungsi

|      Fungsi       |      Parameter        |   Jenis    |          Kegunaan          |
|  "hitung_nilai()" |    tugas, uts, uas    |  Non-void  |   Menghitung nilai akhir   |
|  "nilai_huruf()"  |        nilai          |  Non-void  |   Menentukan nilai huruf   |
|   "kelulusan()"   |        huruf          |  Non-void  | Menentukan status kelulusan|
|"tampilkan_nilai()"| nama, tugas, uts, uas |    Void    |   Menampilkan hasil nilai  |

C. Perhitungan Manual

Andi:

(80 × 0,3) + (70 × 0,3) + (90 × 0,4) = 81

Hasil: B (Lulus).

Dimas:

(75 × 0,3) + (80 × 0,3) + (65 × 0,4) = 72,5

Hasil: B (Lulus).

Hasil perhitungan manual sama dengan hasil program.

D. Pengembangan Program

Untuk mencari mahasiswa dengan nilai tertinggi, dapat ditambahkan fungsi "nilai_tertinggi()". Fungsi tersebut nantinya dipanggil melalui "main()", sedangkan fungsi lainnya tidak perlu diubah.

---

SOAL 2 – STRUK PENGIRIMAN

A. Hasil Program

Program menghitung ongkir berdasarkan berat, jarak, dan status anggota. Pelanggan yang menjadi anggota mendapatkan diskon 10%.

=== STRUK PENGIRIMAN TOKO DARING ===
-----------------------------------
Pelanggan    : Rina
Biaya Berat  : Rp10,000
Biaya Jarak  : Rp0
Potongan     : Rp0
Ongkir Akhir : Rp10,000
-----------------------------------
Pelanggan    : Sari
Biaya Berat  : Rp22,000
Biaya Jarak  : Rp5,000
Potongan     : Rp0
Ongkir Akhir : Rp27,000
-----------------------------------
Pelanggan    : Tono
Biaya Berat  : Rp22,000
Biaya Jarak  : Rp5,000
Potongan     : Rp2,700
Ongkir Akhir : Rp24,300
-----------------------------------
Pelanggan    : Umar
Biaya Berat  : Rp10,000
Biaya Jarak  : Rp5,000
Potongan     : Rp1,500
Ongkir Akhir : Rp13,500
-----------------------------------
Pelanggan    : Vina
Biaya Berat  : Rp34,000
Biaya Jarak  : Rp0
Potongan     : Rp0
Ongkir Akhir : Rp34,000
-----------------------------------
TOTAL PENDAPATAN ONGKOS KIRIM HARI INI: Rp108,800

B. Desain Fungsi

Fungsi             |          Parameter         |  Jenis  | Kegunaan
"tampilkan_judul()"|              -             |   Void  | Menampilkan judul
"biaya_berat()"    |            berat           | Non-void| Menghitung biaya berat
"biaya_jarak()"    |            jarak           | Non-void| Menghitung biaya jarak
"diskon()"         |        ongkir, anggota     | Non-void| Menghitung diskon
"tampilkan_struk()"| nama, berat, jarak, anggota| Non-void| Menampilkan struk dan mengembalikan total

C. Perhitungan Manual

Sari:

Rp10.000 + (3 × Rp4.000) + Rp5.000 = Rp27.000

Tono:

Rp27.000 - (10% × Rp27.000) = Rp24.300

Umar:

Rp15.000 - (10% × Rp15.000) = Rp13.500

Hasil perhitungan manual sesuai dengan hasil program.

D. Perubahan Aturan

Jika batas jarak gratis menjadi 15 km dan biaya tambahan menjadi Rp7.000, fungsi "biaya_jarak()" cukup diubah menjadi:

def biaya_jarak(jarak):
    """Menghitung biaya berdasarkan jarak."""
    if jarak <= 15:
        return 0
    else:
        return 7000

Fungsi lainnya tidak perlu diubah karena perhitungan jarak sudah memiliki fungsi tersendiri.

---

KESIMPULAN

Dari kedua soal ini, saya belajar menggunakan fungsi untuk membagi program berdasarkan tugasnya. Penggunaan "if-else", "return", dan "for loop" juga membantu proses perhitungan menjadi lebih teratur dan mudah dipahami.
