riwayat_sekolah = [
  {
      "nama_sekolah": "SDN 3 Pringga Jurang",
      "alamat_sekolah": "Pringga Jurang",
      "tahun_lulus": 2016
  },
  {
      "nama_sekolah": "MTS NW Talun",
      "alamat_sekolah": "Pringga Jurang",
      "tahun_lulus": 2019
  },
  {
      "nama_sekolah": "SMA N 1 Sikur",
      "alamat_sekolah": "Sikur",
      "tahun_lulus": 2022
  }
]

for riwayat in riwayat_sekolah:
  print(f"Nama Sekolah:", riwayat["nama_sekolah"])
  print(f"Alamat Sekolah:", riwayat["alamat_sekolah"])
  print(f"Tahun Lulus:", riwayat["tahun_lulus"])
  print()