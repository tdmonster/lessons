# def kvadrat_funksiya():
#     son=int(input("Son kiriting:"))
#     natija=(f"{son}sonining kvadrati: {son**2}")
#     return natija
# print(kvadrat_funksiya())


# def full_name_func(first_name,last_name,name=''):
#     full_name=f"{first_name}{last_name}"
#     return full_name


# student1=full_name_func("Muhammadyusuf" , "Abdusattorov")
# student2=full_name_func("Husanboy" , "Shermuhammedov")
# student3=full_name_func("Tohirbek" , "Rustamov")
# student4=full_name_func("Izzatbek" , "Azamov")

# print(f"Darsga kech qolgan talabalar: {student2}.\nVaqtida kelgan talabalar: {student1}, {student4}, {student3}")
 
 

# def full_name_func(first_name,last_name,name=''):
#     if name:

#         full_name=f"{first_name} {name} {last_name}"
#     else:
#         full_name=f"{first_name} {last_name}"
        
#     return full_name.title()


# student1=full_name_func("Muhammadyusuf" , "Abdusattorov")
# student2=full_name_func("Husanboy" , "Shermuhammedov")
# student3=full_name_func("Tohirbek" , "Rustamov")
# student4=full_name_func("Izzatbek" , "Azamov")
# student5=full_name_func("palonchi","pistonchiyev","Xojakovich")
# print(student1)
# print(student5)

# def avto_info(model,rangi,yili,karobkasi,narx=None):

#     avto={
#         'model':model,
#         'rangi':rangi,
#         'yili':yili,
#         'karobkasi':karobkasi,
#         'narx':narx
#         }
#     return avto

# avto1=avto_info('Malibu','Qora',2021,'avtomat')
# avto2=avto_info('Gentra','qora',2023,'avtomat',12000)

# print("online savdoda mavjud avtomobillar :")
# for avto in [avto1,avto2]:
#     if avto['narx']:
#         print(f"Modeli: {avto['model']}, Rangi: {avto['rangi']} yili:{avto['yili']},karobkasi:{avto['karobkasi']},narx:{avto['narx']} ")
#     else:
#         print(f"{avto['model']} {avto['rangi']} {avto['yili']},karobkasi:{avto['karobkasi']} ")
def oraliq(min,max,qadam):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        min+= qadam
        
    return sonlar

print(oraliq(1,51,2))
print(oraliq(10,21,3))