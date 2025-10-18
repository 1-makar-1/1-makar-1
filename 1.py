import random
marks = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOP1QRSTUVWXYZ12345678901"
podaj_dłudość = int(input("podaj długość hasła:"))

password = ""

for i in range(podaj_dłudość):
    password += random.choice(marks)

print(password)
