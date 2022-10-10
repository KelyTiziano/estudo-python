p=float(input("quanto voce ganha por hora?"))
p1=int(input("quantas horas voce trabalha por mes?"))
bruto=(p1*p)
print(f"Salário bruto {bruto}")

liquido=bruto-(bruto*24/100)
print(f"com os descontos o salario é {liquido} reais ")
descontos=(bruto-liquido)
print(f"voce teve um total de {descontos} reais em descontos")

desc_inss=bruto-(bruto*8/100)
inss=(bruto-desc_inss)
print(f"você pagou ao inss {inss} reais")

desc_ir=bruto-(bruto*11/100)
ir=(bruto-desc_ir)
print(f" voce pagou ao IR {ir} reais")

desc_sindicato=bruto-(bruto*5/100)
sindicato=(bruto-desc_sindicato)
print(f"voce pagou ao sindicato {sindicato} reais ")


