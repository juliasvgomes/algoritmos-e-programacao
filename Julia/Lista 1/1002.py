# https://www.beecrowd.com.br/judge/pt/problems/view/1002

raio = float(input())
area = round(3.14159*raio**2, 4)
area = '{:6.4f}'.format(area)
print(f"A={area}\n")