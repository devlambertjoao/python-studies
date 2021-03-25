peso_max = 113

class Item:
  def __init__(self, id, peso, valor):
    self.id = id
    self.peso = peso
    self.valor = valor
    self.valorPeso = valor / peso

items = [
    Item(1,3,1), Item(2,8,3), Item(3,12,1), Item(4,2,8), Item(5,8,9), Item(6,4,3), Item(7,4,2), Item(8,5,8), Item(9,1,5), Item(10,1,1), Item(11,8,1), Item(12,6,6), Item(13,4,3), Item(14,3,2), 
    Item(15,3,1), Item(16,5,2), Item(17,3,3), Item(18,24,8), Item(19,5,9), Item(20,7,3), Item(21,4,2), Item(22,5,4), Item(23,7,5), Item(24,2,4), Item(25,3,3), Item(26,8,1), Item(27,4,3), Item(28,3,2),
    Item(29,7,14), Item(30,19,40), Item(31,20,20), Item(32,21,19), Item(33,11,15), Item(34,10,37), Item(35,13,18), Item(36,17,13), Item(37,18,19), Item(38,4,6), Item(39,15,15), Item(40,25,4), Item(41,12,17), Item(42,19,39)
]

def orderByValorPeso(e):
    return e.valorPeso

items.sort(reverse=True, key = orderByValorPeso)
itemsMochila = []
totalPeso = 0

for item in items:
    if totalPeso + item.peso <= peso_max:
        itemsMochila.append(item)
        totalPeso = totalPeso + item.peso

pesoTotalMochila = 0
valorTotalMochila = 0
for itemMochila in itemsMochila:
    print("Objeto: {itemId}".format(itemId=itemMochila.id))
    pesoTotalMochila = pesoTotalMochila + itemMochila.peso
    valorTotalMochila = valorTotalMochila + itemMochila.valor

print("Peso total da mochila: {pesoMochila}".format(pesoMochila=pesoTotalMochila))
print("Valor total da mochila: {valorMochila}".format(valorMochila=valorTotalMochila))