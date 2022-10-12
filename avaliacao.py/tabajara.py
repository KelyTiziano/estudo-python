salario=int(input("Qual é o seu salario?"))
por20=(20*salario/100)
por15=(15*salario/100)
por10=(10*salario/100)
por5=(5*salario/100)

if salario <280:
    print(f"com aumento de 20% ({por20} reais) seu salario deixou de ser {salario} e passa a ser {(por20+salario)}")

if salario >280<700:
     print(f"com aumento de 15% ({por15} reais) seu salario deixou de ser {salario} e passa a ser {(por15+salario)}")

if salario >700<1500:
     print(f"com aumento de 10% ({por10} reais) seu salario deixou de ser {salario} e passa a ser {(por10+salario)}")

if salario >1500:
     print(f"com aumento de 5% ({por5} reais) seu salario deixou de ser {salario} e passa a ser {(por5+salario)}")



