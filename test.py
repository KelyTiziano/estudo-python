km_cilindro_completo=150
preco_cilindro_completo=66
km_por_m3=km_cilindro_completo/16
print(f"meu carro faz {km_por_m3} por m3")

km_total_dia=1000
qtd_tanque_completo=km_total_dia/km_cilindro_completo
print(f"eu enchi o tanque {qtd_tanque_completo} vezes")

total_gasto_dia=qtd_tanque_completo*preco_cilindro_completo
print(f"eu gasto{total_gasto_dia}para rodar{km_total_dia}")




