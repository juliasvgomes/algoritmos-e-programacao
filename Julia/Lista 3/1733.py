# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = (input())
horasExtras = float(input())

salHoraExtra = (horasExtras * (10))
salBruto = ((3) * 1192.40 + salHoraExtra)

if salBruto > 2000.0:
    inss = (salBruto * (0.12))
    
else:
    inss = (salBruto * (0.5))

if salBruto > 2500.00:
    imposto = (salBruto * (0.20))
    
else:
    imposto = (salBruto * (0.0))

salLiquido = (salBruto - (inss) - (imposto))
    
print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %(salBruto))
print("Salário líquido: R$%.2f" %(salLiquido))