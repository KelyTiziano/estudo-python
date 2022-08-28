nota_1=int(input("primeira nota"))
nota_2=int(input("segunda nota"))
nota_3=int(input("terceira nota"))
nota_4=int(input("quarta nota"))
media_final=(nota_1+nota_2+nota_3+nota_4)/4
print(f"a media final ficou em {media_final}")
if media_final  >=  7:
    print(f"passou")
else:
    print(f"aluno reprovado")
