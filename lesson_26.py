
#         'narx':narx
#         }
#     return avto


# print("Sayitimizdagi avtolar ro'yxatini shakllantiramiz")
# avtolar=[]
# while True:
#     print("\nQuyidagi malumotlarni kiriting \n",end="")
#     kompaniya=input("Ishlab chiqaruvchi: ")       
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     karobkasi=input("Karobka turi: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narx=input("narxi: ")
    
#     avtolar.append(avto_info(kompaniya,model,rangi,yili,karobkasi,narx))
#     javob=input("Yana avto qo'shamizmi? (yes/no):")
#     if javob.lower()!='yes':
#         break
    
    
# print("Avtomobil tafsiloti: ")
# for a in avtolar:
#     print(f"Modeli: {a['model']}, rangi: {a['rangi']}, yili:{a['yili']}, karobkasi:{a['karobkasi']}, narx:{a['narx']} ")


def user_info(ismi,familiyasi,t_yili,t_joy,email=None,telefon=None):

    user={'ismi':ismi,
        'familiyasi':familiyasi,
        't_yili':t_yili,
        't_joy':t_joy,
        'email':email,
        'telefon':telefon
        }
    return user

print("Foydalanuvchi ro'yxzatini shakklkantiramiz.")
users=[]
while True:
    print("\nQuyidagi malumotlarni kiriting\n",end="")
    ismi=input("Foydalanuvchi ismi:")
    familiyasi=input("Foydalnuvchi familiyasi:")
    t_yili=input("Tug'ulgan yili:")
    t_joy=input("Tug'ulgan joyi:")
    email=input("Foydalnuvchi emaili:")
    telefon=input("Foydalnuvchi telefoni:")
    
    
    users.append(user_info(ismi,familiyasi,t_yili,t_joy,email,telefon))
    javob=input("Yana foydalanuvchi qo'shamizmi? (yes/no):")
    if javob.lower()!='yes':
        break
    
    print("\n ro'yxatdagi foydalanuvchilasr : ")
for a in users:
    print(f"Foydalanuvchi ismi: {a['ismi']}\nFoydalanuvchi familiyasi: {a['familiyasi']}\nFoydalanuvchi tug'ulgan yili:{a['t_yili']}\nFoydalanuvchi tug'ulgan joyi:{a['t_joy']}\nFoydalanuvchi emaili:{a['email']}\nFoydalanuvchi telefoni{a['telefon']} ")