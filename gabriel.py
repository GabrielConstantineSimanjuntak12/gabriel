def hitung_nilai_akhir(tugas, uts, uas):
    """Menghitung nilai akhir berdasarkan bobot tugas (30%), UTS (30%), dan UAS (40%)."""
    return (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

def tentukan_nilai_huruf(nilai_akhir):
    """Menentukan huruf mutu berdasarkan rentang nilai akhir."""
    if nilai_akhir >= 85:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 55:
        return 'C'
    elif nilai_akhir >= 40:
        return 'D'
    else:
        return 'E'

def tentukan_status_lulus(nilai_huruf):
    """Menentukan status kelulusan mahasiswa dengan syarat minimal nilai huruf C."""
    return "Lulus" if nilai_huruf in ['A', 'B', 'C'] else "Tidak Lulus"

def tampilkan_tabel_rekap(data_mahasiswa):
    """Menampilkan tabel rekapitulasi nilai mahasiswa secara terformat (fungsi void)."""
    print(f"{'Nama':<10} | {'Nilai Akhir':<11} | {'Nilai Huruf':<11} | {'Keterangan'}")
    print("-" * 55)
    for mhs in data_mahasiswa:
        nama = mhs['nama']
        na = hitung_nilai_akhir(mhs['tugas'], mhs['uts'], mhs['uas'])
        nh = tentukan_nilai_huruf(na)
        ket = tentukan_status_lulus(nh)
        print(f"{nama:<10} | {na:<11.2f} | {nh:<11} | {ket}")

def hitung_statistik_kelas(data_mahasiswa):
    """Menghitung rata-rata nilai akhir kelas dan jumlah total mahasiswa yang lulus."""
    total_na = 0
    jumlah_lulus = 0
    jumlah_mhs = len(data_mahasiswa)
    
    for mhs in data_mahasiswa:
        na = hitung_nilai_akhir(mhs['tugas'], mhs['uts'], mhs['uas'])
        total_na += na
        if tentukan_status_lulus(tentukan_nilai_huruf(na)) == "Lulus":
            jumlah_lulus += 1
            
    rata_rata = total_na / jumlah_mhs if jumlah_mhs > 0 else 0
    return rata_rata, jumlah_lulus

def main():
    """Alur utama program rekapitulasi nilai mata kuliah."""
    data_mahasiswa = [
        {"nama": "Andi", "tugas": 80, "uts": 70, "uas": 90},
        {"nama": "Bunga", "tugas": 90, "uts": 85, "uas": 88},
        {"nama": "Citra", "tugas": 60, "uts": 45, "uas": 50},
        {"nama": "Dimas", "tugas": 75, "uts": 80, "uas": 65},
        {"nama": "Eka", "tugas": 30, "uts": 40, "uas": 35}
    ]
    
    print("=== TABEL REKAPITULASI NILAI MAHASISWA ===")
    tampilkan_tabel_rekap(data_mahasiswa)
    
    rata_rata, jumlah_lulus = hitung_statistik_kelas(data_mahasiswa)
    print("-" * 55)
    print(f"Rata-rata nilai akhir kelas : {rata_rata:.2f}")
    print(f"Banyaknya mahasiswa yang lulus : {jumlah_lulus}")

if __name__ == "__main__":
    main()