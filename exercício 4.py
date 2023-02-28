print('exercício 4 variáveis e nomes')

carros = 100
lugares_no_carro = 4.0
motoristas = 30
passageiros = 90
carros_não_dirigidos = carros - motoristas
carros_dirigidos = motoristas
capacidade_no_carro = carros_dirigidos * lugares_no_carro
media_de_passageiros_por_carro = passageiros / carros_dirigidos

print('tem', carros, 'carros disponiveis')
print('so tem', motoristas, 'motoristas disponiveis')
print('vão ter', carros_não_dirigidos,'carros vazios')
print('posso tansportar', capacidade_no_carro,'pessoas hoje')
print('temos', passageiros,'para capacidade hoje')
print('precisamos',media_de_passageiros_por_carro,'em cada carro')

