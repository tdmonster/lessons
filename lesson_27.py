# def bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f"Talaba {ism.title()}ning bahosini kiriting:")
#         baholar[ism]=baho
#     return baholar

# talabalar=["Izzatbek","Tohirbek","Husanboy"]
# baholar=bahola(talabalar)
# print(baholar)


# def katta_harf(ismlar):
#     return [ism.title() for ism in ismlar]


# ismlar=[" izzatbek","tohirbek","husanboy"]
# yangi_ismlar=katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)



# def summa(*sonlar):
#     return sum(sonlar)
   

# print(summa(100,2,3,4,5,6))



# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)

# print(summa(2,3))


# **kwargs

def avto_info(kompaniya,model,**malumotlar):
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar


avto1=avto_info("GM","Malibu",rang="qora",yili=2025)
avto2=avto_info("GM","BD",rang="oq",yili=2020)

print(avto1)
print()
print(avto2)
