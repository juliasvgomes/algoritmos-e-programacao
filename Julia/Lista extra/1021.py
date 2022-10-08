# https://www.beecrowd.com.br/judge/pt/problems/view/1021

n = float(input())

n100 = n // 100
n = n - n100*100

n50 = n // 50
n = n - n50*50

n20 = n // 20
n = n - n20*20

n10 = n // 10
n = n - n10*10

n5 = n // 5
n = n - n5*5

n2 = n // 2
n = n - n2*2

n1 = n // 1
n = n - n1*1
n1=float('%.2f'% n1)
n=float('%.2f'% n)

m50 = n // 0.5
n = n - m50*0.5
m50=float('%.2f'% m50)
n=float('%.2f'% n)

m25 = n // 0.25
n = n - m25*0.25
m25=float('%.2f'% m25)
n=float('%.2f'% n)

m10 = n // 0.10
n = n - m10*0.10
m10=float('%.2f'% m10)
n=float('%.2f'% n)

m5 = n // 0.05
n = n - m5*0.05
m5=float('%.2f'% m5)
n=float('%.2f'% n)

m1 = n * 100
m1=float('%.2f'% m1)
n=float('%.2f'% n)

print('NOTAS:')
print('%i nota(s) de R$ 100.00' %n100)
print('%i nota(s) de R$ 50.00' %n50)
print('%i nota(s) de R$ 20.00' %n20)
print('%i nota(s) de R$ 10.00' %n10)
print('%i nota(s) de R$ 5.00' %n5)
print('%i nota(s) de R$ 2.00' %n2)
print('MOEDAS:')
print('%i moeda(s) de R$ 1.00' %n1)
print('%i moeda(s) de R$ 0.50' %m50)
print('%i moeda(s) de R$ 0.25' %m25)
print('%i moeda(s) de R$ 0.10' %m10)
print('%i moeda(s) de R$ 0.05' %m5)
print('%i moeda(s) de R$ 0.01' %m1)