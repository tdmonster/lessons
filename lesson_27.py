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

# def avto_info(kompaniya,model,**malumotlar):
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar


# avto11=avto_info("GM","Malibu",rang="qora",yili=2025)
# avto2=avto_info("GM","BD",rang="oq",yili=2020)

# print(avto11)
# print()
# print(avto2)

    
    
    
    
def avto_info(kompaniya,model,rangi,karobka,yili,narhi=None):
    avto={"kompaniya":kompaniya,
         "model":model,
         "rang":rangi,
         "karobka":karobka,
         "yil":yili,
         "narh":narhi
         }
    return avto

def avto_kirit():
    avtolar=[]
    while True:
        print("\n Quyidagi malumotlarni kiriting :",end="")
        kompaniya=input("Ishlab chiqaruvchi:")
        model=input("Modeli:")
        rangi=input("Rangi")
        karobka=input("Karobka")
        yili=input("yili:")
        narhi=input("narhi:")
        
        avtolar.append(avto_info(kompaniya,model,rangi,karobka,yili,narhi))
        javob=input("Yana avto qo'shishni hohlaysizmi")
        if javob=="no":
            break
        
    return avtolar
        
        
        
def info_print(avto_info):
    print(f"{avto_info["rang"].title()} {avto_info["kompaniya"].upper()}"
          f"{avto_info["model"].upper},{avto_info["karobka"]} karobka,"
          f"{avto_info["yil"]}-yil,{avto_info["narh"]}$")
    
    