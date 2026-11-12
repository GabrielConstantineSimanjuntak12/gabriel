def hitung_biaya_berat(berat):
  """Menghitung biaya berat paket (Rp10.000 untuk <=2kg, selebihnya +Rp4.000/kg)."""
  if berat <= 2:
    return 10000
  else:
    return 10000 + (berat - 2) * 4000


def hitung_biaya_jarak(jarak):
  """Menghitung biaya jarak pengiriman (Rp0 jika <=20km, Rp5.000 jika >20km)."""
  if jarak <= 20:
    return 0
  else:
    return 5000


def hitung_potongan(total_biaya, status_anggota):
  """Menghitung potongan 10% jika status pelanggan adalah anggota ('Ya')."""
  if status_anggota.lower() == "ya":
    return total_biaya * 0.10
  else:
    return 0.0


def cetak_struk_pesanan(pesanan):
  """Mencetak struk untuk satu pesanan dan mengembalikan ongkos kirim akhir (Non-void)."""
  nama = pesanan["nama"]
  berat = pesanan["berat"]
  jarak = pesanan["jarak"]
  status = pesanan["anggota"]

  biaya_b = hitung_biaya_berat(berat)
  biaya_j = hitung_biaya_jarak(jarak)
  total_sebelum_diskon = biaya_b + biaya_j
  potongan = hitung_potongan(total_sebelum_diskon, status)
  ongkir_akhir = total_sebelum_diskon - potongan

  print(f"Pelanggan    : {nama}")
  print(f"Biaya Berat  : Rp{biaya_b:,.0f}")
  print(f"Biaya Jarak  : Rp{biaya_j:,.0f}")
  print(f"Potongan     : Rp{potongan:,.0f}")
  print(f"Ongkir Akhir : Rp{ongkir_akhir:,.0f}")
  print("-" * 35)

  return ongkir_akhir


def main():
  """Fungsi utama untuk memproses seluruh pesanan dan menampilkan total pendapatan."""
  daftar_pesanan = [
      {"nama": "Rina", "berat": 1, "jarak": 10, "anggota": "Bukan"},
      {"nama": "Sari", "berat": 5, "jarak": 25, "anggota": "Bukan"},
      {"nama": "Tono", "berat": 5, "jarak": 25, "anggota": "Ya"},
      {"nama": "Umar", "berat": 2, "jarak": 30, "anggota": "Ya"},
      {"nama": "Vina", "berat": 8, "jarak": 15, "anggota": "Bukan"},
  ]

  print("=== STRUK PENGIRIMAN TOKO DARING ===")
  print("-" * 35)

  total_pendapatan = 0
  for pesanan in daftar_pesanan:
    ongkir = cetak_struk_pesanan(pesanan)
    total_pendapatan += ongkir

  print(f"TOTAL PENDAPATAN ONGKOS KIRIM HARI INI: Rp{total_pendapatan:,.0f}")


if __name__ == "__main__":
  main()