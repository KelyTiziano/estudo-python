n1=int(input("digite um numero "))
n2=int(input("digite o seu segundo numero "))
n3=int(input("digite o seu terceiro numero "))

if (n1 > n2 and n1>n3 ):
    print(f"o maior numero é {n1}")
if (n2 > n1 and n2>n3 ):
    print(f"o maior numero é {n2}")
if (n3>n1 and n3>n2):
    print(f" o maior numero é {n3}")

if (n1<n2 and n1<n3):
    print(f"o menor numero é {n1}")
if (n2<n1 and n2<n3):
    print(f"omenor numero é {n2}")
if (n3<n1 and n3<n2):
    print(f"o menor numero é {n3}")
