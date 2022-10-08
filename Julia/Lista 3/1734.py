# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

numero = int(input())

fatorial = 1
contar = 1

while contar <= numero:
    fatorial = fatorial * contar
    contar = contar + 1
    
print("%i!" %(numero), "= %i" %(fatorial))