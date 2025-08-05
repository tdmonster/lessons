# menyu=["osh","kabob","sho'rvo","qozonkabob","somsa"]
# ovqat=input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() in menyu:
#     print("Buyurtma qbul qilindi")
# else:
#     print("Afsuski bizda bu ovqat yo'q!")
# menyu=["osh","somsa","kabob","monti","sho'rvo","hotdog","cola","sharbat","spagetti","tandir", "jo'ja"]
# buyurtmam=["shashlik","tandir, "jo'ja","sharbat"]

# for taom in buyurtmam:
#     if taom in menyu:
#         print(f"Buyurtma: {taom} qabul qilindi!")
#     else:
#         print(f"Afsuski bizda {taom} yo'q!")
# menyu=["osh","somsa","shashlik","norin","tandir"]
# ovqat=input("Nima ovcqat yeysiz?>>")
# if ovqat.lower() not in menyu:
#     print("Afsuski bizda bu ovqat yo'q")
# else:
#     print("Buyurtma qabul qilindi")
# son=int(input("istalgan son kiriting?"))
# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} soniga qoldiqsiz bo'linadi!")
users=["asrorbek","izzatbek","ozodbek","tohirbek"]
login=input("Yangi login tanlang!")

if login.lower() in users:
    print("Bu user name band ,boshqa user name tanglang!")
else:
    print("Xush kelibsiz", login.title())