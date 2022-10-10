a=int(input("digite um numero "))
b=int(input("digite o segundo numero "))
c=int(input("digite o terceiro numero "))
if (c>b and c>a and b>a):
    print(f"a ordem decrescente é {c},{b},{a}")
if (b>a and b>c and a>c):
    print(f"a ordem decrescente é {b}, {a}, {c}")
if (a>b and a>c and b>c):
    print(f"a ordem decrescente é {a},{b}, {c}")
if (c>a and c>b and a>b):
    print(f"a ordem decrescente é {c}, {a},{b}")
if(b>a and b>c and c>a):
    print(f"a ordem decrescente é {b},{c}, {a}")
if (a>b and a>c and c>b):
    print(f"a ordem decrescente é {a},{c},{b}")
