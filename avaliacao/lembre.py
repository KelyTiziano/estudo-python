n1=float(input("digite a nota 1" ))
n2=float(input("digite a nota 2" ))
media=(n1+n2)/2

if media >=7.5:
    print("aluno aprovado")
elif media <7.5 and media >=5:
    print("recuperação")
else:
    print("reprovou")
