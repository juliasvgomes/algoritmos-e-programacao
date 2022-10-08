# https://www.beecrowd.com.br/judge/pt/problems/view/1019

N = int(input())

hora = N // 60**2
N = N - hora * 60**2

minutos = N // 60
N = N - minutos * 60

segundos = N

print("%i:%i:%i" %(hora, minutos, segundos))