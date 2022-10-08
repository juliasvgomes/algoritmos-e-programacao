# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

total = 0

preco = 1
while preco > 0:
    preco = float(input())
    total += preco


print("Total da compra: R$%2.2f " %(total))
dinheiro = float(input())
print("Valor pago: R$%2.2f"%(dinheiro))
print("Troco: R$%2.2f"%(dinheiro - total))