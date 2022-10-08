# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

preçoCompra = float(input())

if preçoCompra < 20.00:
    valor = (preçoCompra * (0.45))
    lucro = (preçoCompra + valor)
    
else:
    valor = (preçoCompra * (0.30))
    lucro = (preçoCompra + valor)
    
print ("Valor de venda: R$%.2f" %lucro)