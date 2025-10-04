import random
marks = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
podaj_dłudość = int(input("podaj długość hasła:"))

password = ""

for i in range(podaj_dłudość):
    password += random.choice(marks)

print(password)
