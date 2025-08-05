# yosh=int(input("Yoshingiz nechchida?"))

# if yosh<=4:
#     print("Yo'l haqqi siz uchun  bepul")
    
# elif yosh<=12:
#     print("Yo'l haqqi siz uchun 5 ming so'm")
# elif yosh>=100:
#     print("Yo'l haqqi siz uchun bepul")
      
# else:
#     print("Yo'l haqqi siz uchun 10 ming so'm")

yosh=int(input("Yoshingiz nechchida?>>>"))

if yosh<=4:
    narx=0
    
elif yosh<=12:
    narx=5000
    
elif yosh<65:
    narx=10000
    
else:
    narx=8000
    
print(f"Siz uchun kirish {narx}so'm")
