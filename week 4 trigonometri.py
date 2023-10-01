import math as mtk
lat1 = float(input("Input the first lattitude : "))
lat2 = float(input("Input the second lattitude : "))
long1 = float(input("input the first longtitude : "))
long2 = float(input("Input the seccond longtitude : "))

latTotal = (lat2 * (mtk.pi / 180)) - (lat1 * (mtk.pi / 180))
longTotal = (long2 * (mtk.pi / 180)) - (long1 * (mtk.pi / 180))
a = (mtk.sin(latTotal / 2) ** 2) + ((mtk.cos(lat1)) * (mtk.cos(lat2)) * (mtk.sin(longTotal / 2) ** 2))
c = 2 * mtk.atan2(mtk.sqrt(a), mtk.sqrt(1-a))
d = 6371 * c
print("jarak antar kedua titik adalah sebesar {}".format(d))