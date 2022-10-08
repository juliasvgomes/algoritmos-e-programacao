# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

anoAtual = int (input( ))

salarioBase = 1000
percentual = 0.015

if anoAtual < 2006:
    print("O ano informado deverá ser > 2005!")
    
else:
    salarioFinal = salarioBase + (percentual * salarioBase)
    
    for n in range (2007,anoAtual + 1) :
        percentual = percentual + 0.01
        salarioFinal = salarioFinal + (percentual * salarioFinal)
    
    print ("Salário atual: R$%.2f" %salarioFinal)