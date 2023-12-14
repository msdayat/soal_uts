def boleh_memilih(usia, status_perkawinan):
  if usia >= 17 or status_perkawinan:
    return True
  elif status_perkawinan:
    return True
  else: 
    return False

print(boleh_memilih(18, True)) 
