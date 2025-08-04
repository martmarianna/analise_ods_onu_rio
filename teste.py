estoque = {'banana':50, 'maçã':4, 'abacaxi':10}
total = 0
for valor in estoque.values():
    total += valor

print("Temos %d frutas no estoque."%(total))