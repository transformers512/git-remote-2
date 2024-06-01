def pangkat(n):
  return lambda angka:angka**n

hasil_pangkat = pangkat(3)
print(f"hasil dari 6 pangkat 3 adalah: {hasil_pangkat(6)}")