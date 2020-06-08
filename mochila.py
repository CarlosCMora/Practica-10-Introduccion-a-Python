"""
Considere una mochila capaz de cargar un peso M y n elementos. 
Con pesos p1,p2,p3...pn y los beneficios b1,b2,b3...bn 
Tanto M como pi serán enteros. 
Se trata de encontrar la combinación de elementos , representados con mediante la tupla:
x=(x1,x2,x3...xn) con xi pertenece {0,1} Maximiza el beneficio
f(x)= suma(i=1, n) bixi
Sin sobrepasar el peso maximo.
suma(i=1,n) pi xi 
"""

#i es el indice del elemento
#p peso
#b beneficio
#m peso disponible
benefitMax = 0
optima = []
def pesoMochila(backpack):
    weight = 0
    for i in range(len(backpack)):
        weight = weight + backpack[i][1]
    return weight


def benefitMochila(backpack):
    benefit = 0
    for i in range(len(backpack)):
        benefit = benefit + backpack[i][0]
    return benefit


def copyBackpack(backpack):
    newBackpack = []
    for i in range(len(backpack)):
        newBackpack.append(backpack[i][0])
    return newBackpack

def fillBackpack(n,backpack, items, capacity):
    benefit = benefitMochila(backpack)
    weigth = pesoMochila(backpack)

    global benefitMax
    global optima
    if n >= len(items) or weigth >= capacity:
        benefitMax = benefit
        optima.clear()
        optima = copyBackpack(backpack)
    else:
        x = items[n]
        if weigth + x[1] <= capacity:
            backpack.append(x)
            fillBackpack(n+1, backpack, items, capacity)
            backpack.pop()
        fillBackpack(n+1, backpack, items, capacity)

elementos = [(2,1),(10,4),(1,1),(2,2),(6,12)]
mochila = []
fillBackpack(0,mochila,elementos,15)
print("Elementos en la mochila {}, con bemeficio {}, con peso {}", format(optima, benefitMax, pesoMochila(optima)))


