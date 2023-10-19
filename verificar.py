
meta = 1000
vendas = [
    ['joao', 1300],
    ['maria', 2000],
    ['fernando', 300],
    ['lucas', 2300],
    ['gabriela', 1250],
    ['pedro', 800],
    ['alex', 950]
]

for item in vendas:
    if item[1] >= meta:
        print(f'vendendores que bateu a meta de 1000 ou mais peças vendidas, foram: {item[0]}, quantidades vendidas: {item[1]}')
    else:
        print(f'vendedores que não bateu a meta: {item[0]}, vendeu: {item[1]}')