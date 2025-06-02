import re

# input dos valores
estado = int(input("Qual é o estado de origem dessa carga? (de 1 a 5)\n\t"))
t_carga = int(input("\nQual é o peso da carga? (em toneladas)\n\t"))
cod_carga = int(input("\nQual é o código da carga? (entre 10 e 40)\n\t"))

kg_carga = t_carga * 1000

#definindo o preço por kg
if cod_carga >= 10 and cod_carga <= 20:
    preco_kg = 100
elif cod_carga >= 21 and cod_carga <= 30:
    preco_kg = 250
elif cod_carga >= 31 and cod_carga <= 40:
    preco_kg = 340
else:
    print("arruma o preco_kg")
    preco_kg = 0

#definindo o imposto
if estado == 1:
    imposto = 0.35
elif estado == 2:
    imposto = 0.25
elif estado == 3:
    imposto = 0.15
elif estado == 4:
    imposto = 0.05
elif estado == 5:
    imposto = 0
else:
    print("arruma o impósto")
    imposto = 0

#fazendo as operações necessárias para ter os valores corretos
preco_carga = kg_carga * preco_kg

imposto_t = preco_carga * imposto

preco_t = preco_carga + imposto_t

#função para deixar o valor no esquema de valor em real
def formatar_valor_br(valor_str):
    """Essa função usa regex para deixar a entrega(output) dos valores melhores,
    com melhor vizualização"""
    valor_str = re.sub(",", "#", valor_str)
    valor_str = re.sub(r"\.", ",", valor_str)
    valor_str = re.sub("#", ".", valor_str)
    return valor_str

#formatação dos valores
preco_kg_formatado = f"{preco_kg:,.2f}"
preco_carga_formatado = f"{preco_carga:,.2f}"
imposto_formatado = f"{imposto_t:,.2f}"
preco_t_formatado = f"{preco_t:,.2f}"

#chamada da função
preco_kg_formatado = formatar_valor_br(preco_kg_formatado)
preco_carga_formatado = formatar_valor_br(preco_carga_formatado)
imposto_formatado = formatar_valor_br(imposto_formatado)
preco_t_formatado = formatar_valor_br(preco_t_formatado)

#outputs
print(
    f"\nPeso da carga em quilos:\tR$ {preco_kg_formatado} kg\n"
    f"Preço da carga:\t\t\t\tR$ {preco_carga_formatado}\n"
    f"Imposto total:\t\t\t\tR$ {imposto_formatado}\n"
    f"Valor Final:\t\t\t\tR${preco_t_formatado}"
)