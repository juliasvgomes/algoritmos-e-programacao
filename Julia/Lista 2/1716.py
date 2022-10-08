# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

plano = input("")

salario_atual = float(input(""))

if plano == "A":
    aumento = salario_atual * 0.1

if plano == "B":
    aumento = salario_atual * 0.15
    
elif plano == "C":
    aumento = salario_atual * 0.2
    
novo_salario = salario_atual + aumento

print("Novo salário: R$%.2f" %novo_salario)