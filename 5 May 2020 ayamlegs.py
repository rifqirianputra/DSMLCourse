ayamlegs = 2
kambinglegs = 4
totallivestock = 13
totallegs = 32

kambing = abs((ayamlegs * totallivestock - totallegs)/(kambinglegs-ayamlegs))
ayam = abs(totallivestock - kambing)

print (f"jumlah kambing adalah {kambing}, dan jumlah ayam adalah {ayam}")
