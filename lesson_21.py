# cars = {'name':'BMW','color':'blue','year':2025,'price':45000}
# nom = cars['name']
# rang = cars['color']
# yili = cars['year']
# narx =cars['price']
# print(f"Mening mashinam nomi {nom} ,rangi {rang} ,yili {yili} ,narx {narx} do'llor")


# ism = men_haqimda_malumot['name']
# familiya = men_haqimda_malumot['lastname']
# yosh = men_haqimda_malumot['age']
# maktab = men_haqimda_malumot['school']
# fargona = men_haqimda_malumot['address']

# print(f"Mening ismim {ism}, familiyam {familiya}, yoshim {yosh}, maktabda {maktab} o'qiyman yshayman {fargona}da hechqayerda ishlamman")
# print(men_haqimda_malumot.items())

# for kalit, qiymat in men_haqimda_malumot.items():
#   print(f"Kalit: {kalit}")   
#   print(f"Qiymat: {qiymat}")
# men_haqimda_malumot = {'name':'Izzatbek','lastname':'Azamov','age':14,'school':'7-school','address':'fergana'}
 
# # print(men_haqimda_malumot.keys())
# bozorlik = ["banan","non","qaymoq","sut","tarvuz","tuxum","guruch","go'sht"]
# mahsulotlar = {"non":5000,"qaymoq":50000,"tuxum":2000,"guruch":50000,"go'sht":10000,"sut":2000,"tarvuz":3000}

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#       print(f"Iltimos, do'koningizga {buyum} ham olib keling")

# print(mahsulotlar.keys())
# print(mahsulotlar.values())

# for narx in mahsulotlar.values():
#     print(f"mahsulot narxlari: {narx}")
davlatlar = {"Uzbekiston":"Toshkent","Angliya":"London","Italiya":"Rim","Rossiya":"Maskova","Amerika":"Vashington"}
for davlat, poytaxt in davlatlar.items():

    print(f"{davlat} davlatning poytaxti {poytaxt} shahri")
    