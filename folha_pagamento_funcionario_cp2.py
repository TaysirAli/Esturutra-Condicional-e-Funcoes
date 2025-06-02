nome = input("Digite seu nome:\t")
cargo = int(input("\nInforme seu cargo.\n1-Gerente\t\t2-Analista\n3-Assistente\t4-Estagiário\nCargo:\t"))

while cargo <= 0 or cargo > 4:
    print("\n1-Gerente\t\t2-Analista\n3-Assistente\t4-Estagiário")
    cargo = int(input("\nFavor digitar uma das opções acima...\nCargo:\t"))

salario_b = float(input("\nDigite seu salário base:\t"))
horas_e = int(input("\nDigite o total das horas extras trabalhadas:\t"))
faltas_m = int(input("\nDigite o total de faltas neste mês:\t"))
bonus = input("\nRecebeu bônus de desempenho esse mês?\nResponda com Sim ou Não:\t")

def calcular_horas_extras():
    valor_h_e = salario_b * 0.015
    return valor_h_e * horas_e

total_h_e = calcular_horas_extras()

def calcular_descontos_faltas():
    valor_f = salario_b * 0.02
    return valor_f * faltas_m

total_f = calcular_descontos_faltas()

def calcular_bonus():
    bonus_t = 0
    if bonus.lower() == "sim" and cargo == 1:
        bonus_t = 1000
    elif bonus.lower() == "sim" and cargo == 2:
        bonus_t = 500
    elif bonus.lower() == "sim" and cargo == 3:
        bonus_t = 300
    elif bonus.lower() == "sim" and cargo == 4:
        bonus_t = 100
    else:
        print()
    return  bonus_t

bonusFinal = calcular_bonus()
salario_t = salario_b + total_h_e + bonusFinal - total_f

print(
    f"\nSalário Bruto: {salario_b}\n"
    f"Total de acréscimos: {total_h_e + bonusFinal}\n"
    f"Total de descontos: {total_f}\n"
    f"Salário Final: {salario_t}"
)