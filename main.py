import random

elemento = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

size = int( input("De cuantos caracteres quieres tu contraseña?") )

password = ""

for i in range(size):
    password += random.choice(elemento)

print(password)
