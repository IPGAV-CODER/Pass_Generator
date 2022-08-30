import random
import string

LS  = int(input("Length of string: "))
LNK = str(input("For the APP: "))

print("Criando senhas para ",LNK)

digits = random.choices(string.digits, k=LS)
letters = random.choices(string.ascii_uppercase,k=LS)
PASS_TEMP = random.sample(digits + letters, LS)
PASS = LNK + "".join(PASS_TEMP)

print(f"Password made for {LNK} is {PASS}")
