# # def ozim_haqimda (Ism,Familiya,Yashash_joy,Tugulgan_yil,yosh):
# #     """Salom beruvchi funksiya
# #     """
# #     print(f"Assalomu Alaykum,Hurmatli {Ism.title()}!,Mening familiyam {Familiya.title()},Men {Yashash_joy.title()}da yashayman,men {Tugulgan_yil} yilda tugulganman,Men {yosh} yosh daman")
# # ozim_haqimda("Izzatbek","Azamov","Oltiariq",2011,14)
# # ozim_haqimda("Muhammad ziyo","Azamov","Oltiariq",2023,2)

# def yosh_hisobla(Ism,yil):
#     print(f"Assalomu alaykum hurmatli {Ism.title()} ,siz {2025-yil} yoshdasiz.")
    
# yosh_hisobla(yil=2011,Ism="Izzatbek"
#              )
    
    
# def son_darajasi():
#     son=int(input("Son kiriting:"))
    
#     kvadrat=son**2
#     kub=son**3
#     print(f"{son}ning kvadrati {kvadrat},kubi esa {kub} ga teng")
    
# son_darajasi()

# def son_turi():
#     son=int(input("Son kiriting!"))
    
#     if son%2==1:
#         print(f"{son} soni toq son")
#     else:
#         print(f"{son} soni juft son")
    
# son_turi()






# def kattasi():
#     son1=int(input("Son kiriting1:"))
#     son2=int(input("Son kiriting2:"))
    
#     if son1 >son2:
#         print(f"{son1} soni katta son.")
    
#     elif son1==son2:
#         print("Bu sonlar o'zaro teng.")
        
#     else:
#         print(f"{son2} soni katta son.")
    
    
# kattasi()

def darajasi():
   """x sonini y darajasini hisoblaydigan funksiya"""
   x=int(input("X sonini kiriting:"))
   y=int(input("Y sonini kiriting:"))
   return x**y
print(darajasi())