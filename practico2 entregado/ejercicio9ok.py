#9.	Crear una función que retorne la suma de todos los presupuestos de las personas (budget).
#●	get_budgets([
#  { "name": "John", "age": 21, "budget": 23000 },
#  { "name": "Steve",  "age": 32, "budget": 40000 },
#  { "name": "Martin",  "age": 16, "budget": 2700 }
#]) ➞ 65700

#●	get_budgets([
#  { "name": "John",  "age": 21, "budget": 29000 },
#  { "name": "Steve",  "age": 32, "budget": 32000 },
#  { "name": "Martin",  "age": 16, "budget": 1600 }

def get_budgets(lista):

    registro0=[]
    registro1=[]
    registro2=[]
    total=0

    #print(lista[0])
    #print(lista[1])
    #print(lista[2])
    registro0=list(lista[0].items())
    registro1=list(lista[1].items())
    registro2=list(lista[2].items())
    total=registro0[2][1]+registro1[2][1]+registro2[2][1]
    #print(total)
    return(total)

print(get_budgets([{ "name": "John", "age": 21, "budget": 23000 },{ "name": "Steve",  "age": 32, "budget": 40000 },{ "name": "Martin",  "age": 16, "budget": 2700 }]))
print(get_budgets([{ "name": "John",  "age": 21, "budget": 29000 },{ "name": "Steve",  "age": 32, "budget": 32000 },{ "name": "Martin",  "age": 16, "budget": 1600 }]))