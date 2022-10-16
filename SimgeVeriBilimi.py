#iki tane dizinin tanımlaması
A= [3,5,7,9,2,10,1,23,5,19,5,4,8,1,6,4,35,2,7,8,5,3,1,1,1]
B = [12,64,7,9,1,2,6,45,7,3,3,3,3,17,6,50,6,8,7,1,1,3,2,43,10]

#ortalamayı bulma
def ortalamayiBul(dizi):
    elemanSayisi = len(dizi)
    if elemanSayisi <= 1:
        return dizi
    else:
        return sum(dizi) / elemanSayisi
#medyanı bulma
def medyaniBul(dizi):
    dizi = sorted(dizi)
    elemanSayisi = len(dizi)
    if elemanSayisi % 2 == 1:
        return dizi[elemanSayisi // 2]
    else:
        i = elemanSayisi // 2
        return (dizi[i - 1] + dizi[i]) / 2

#standart sapmayı bulma
def standartSapmayiBul(dizi):
    sd = 0.0 # standart sapma
    elemanSayisi = len(dizi)
    if elemanSayisi <= 1:
        return 0.0
    else:
        for _ in dizi:
            sd += (float(_) - ortalamayiBul(dizi)) ** 2
        sd = (sd / float(elemanSayisi)) ** 0.5
        return sd
#varyansı bulma
def varyansBul(dizi):
    return standartSapmayiBul(dizi) ** 2
#modu bulma
def moduBul(dizi):
    sayac = {}
    for i in dizi:
        if i in sayac:
            sayac[i]+=1
        else:
            sayac[i] = 1
    mod = sorted(sayac, key=sayac.get, reverse=True)[:1][0]
    sayiAdedi = sayac[mod]
    return mod, sayiAdedi
#normalize etme
def NormalizeEtme(dizi):
    sonuc = 0
    for eleman in dizi:
        sonuc += (eleman)**2
    sonuc = sonuc**0.5#karekoku alnıyor.
    yeni_dizi=[]
    for eleman in dizi:
        yeni_dizi.append(eleman/sonuc)
    return(yeni_dizi)
#yapılan işlemleri ekrana yazdırma

print(f"A dizisinin ortalaması: {ortalamayiBul(A)}\n"
      f"B dizisinin ortalaması: {ortalamayiBul(B)}")

print(f"A dizisinin  medyanı: {medyaniBul(A)}\n"
      f"B dizisinin medyanı: {medyaniBul(B)}")

print(f"A dizisinin standart sapması: {standartSapmayiBul(A)}\n"
      f"B dizisinin standart sapması: {standartSapmayiBul(B)}")

print(f"A dizsinin varyansı: {varyansBul(A)}\n"
      f"B dizisinin varyansı: {varyansBul(B)}")

print(f"A dizisinin modu: {moduBul(A)}\n"
      f"B dizisinin modu: {moduBul(B)}")

print(f"A dizisinin normalize edilmiş hali: {NormalizeEtme(A)}\n"
      f"B dizisinin normalize edilmiş hali: {NormalizeEtme(B)}")