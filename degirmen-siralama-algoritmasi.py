sayilar = [81, 81, 99, 0, -1, 5, 3, 81, 0, 9, 10, 0, -5, 4, 2, 1, 91]
siralanmis_sayilar = [None] * len(sayilar)
kullanimlar = {}  
for j in sayilar:
    if j in kullanimlar:
        kullanimlar[j] += 1
    else:
        kullanimlar[j] = 1
for j in sayilar:
    kucukluk = 0
    esitlik = 0
    for i in sayilar:
        if j < i:
            kucukluk += 1
        elif j == i:
            esitlik += 1
    siralanmis_sayilar[len(siralanmis_sayilar) - kucukluk - esitlik + kullanimlar[j] - 1] = j
    kullanimlar[j] -= 1
print(siralanmis_sayilar)