# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

c = 0
s = 0
qtd = 0

while c <= 3:
  Idade = int(input())
  Peso = float(input())
  c = c + 1
  s = s + Idade
  if Peso > 90:
    qtd = qtd + 1
print("Qtd pessoas > 90Kg: %i" %(qtd))
  
Media = s / 4
print("Idade média: %.2f" %(Media))