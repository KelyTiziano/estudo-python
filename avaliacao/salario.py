horas_mes=int(input("Quantas horas você trabalha por mes? "))
valor_hora=int(input("Quan você ganha por hora trabalhada?"))
bruto=(valor_hora*horas_mes)

ir=(5*bruto/100)
sindicato=(3*bruto/100)
liquido=(bruto-ir-sindicato)
print(f"seu salario bruto é {bruto} reais, com os descontos de 5% {ir} do IR e 3% {sindicato} do sindicato, seu salário liquido fica em {liquido} reais")

