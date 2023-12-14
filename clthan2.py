def cetak_sila_pancasila(n):
  pancasila = {
      1: "Ketuhanan Yang Maha Esa",
      2: "Kemanusiaan yang Adil dan Beradab",
      3: "Persatuan Indonesia",
      4: "Kerakyatan yang Dipimpin oleh Hikmat Kebijaksanaan dalam Permusyawaratan/Perwakilan",
      5: "Keadilan Sosial bagi Seluruh Rakyat Indonesia"
  }

  if n in pancasila:
      print(f"Sila {n}: {pancasila[n]}")
  else:
      print("Input tidak valid. Masukkan angka antara 1 hingga 5.")

cetak_sila_pancasila(4)
