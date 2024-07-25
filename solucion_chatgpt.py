import random
import numpy
from deap import base, creator, tools, algorithms

# Definición de los atributos y posibles valores
colores        = ["rojo", "verde", "blanco", "amarillo", "azul"]
nacionalidades = ["britanico", "sueco", "danes", "noruego", "aleman"]
bebidas        = ["te", "cafe", "leche", "cerveza", "agua"]
cigarrillos    = ["pallmall", "dunhill", "bluemaster", "prince", "brends"]
mascotas       = ["perro", "pajaro", "gato", "caballo", "pez"]
posiciones     = [1, 2, 3, 4, 5]

def generarIndividuo():
    # Generar una permutación de cada atributo
    colores_perm = random.sample(colores, len(colores))
    nacionalidades_perm = random.sample(nacionalidades, len(nacionalidades))
    bebidas_perm = random.sample(bebidas, len(bebidas))
    cigarrillos_perm = random.sample(cigarrillos, len(cigarrillos))
    mascotas_perm = random.sample(mascotas, len(mascotas))
    posiciones_perm = random.sample(posiciones, len(posiciones))

    # Crear el individuo como una lista de tuplas con características únicas
    individuo = list(zip(colores_perm, nacionalidades_perm, bebidas_perm, cigarrillos_perm, mascotas_perm, posiciones_perm))

    return individuo

def evaluarIndividuo(individuo):
    puntaje = 0
    aux_dic = {}
    aux_list = []

    # Convertir la lista de tuplas a una lista de diccionarios
    for tupla in individuo:
        aux_dic = {
            "color": tupla[0],
            "nacionalidad": tupla[1],
            "bebida": tupla[2],
            "cigarrillo": tupla[3],
            "mascota": tupla[4],
            "posicion": tupla[5]
        }
        aux_list.append(aux_dic)

    # Aplicar las reglas para calcular el puntaje
    for i, persona in enumerate(aux_list):
        if persona["nacionalidad"] == "britanico" and persona["color"] == "rojo":
            puntaje += 1
        if persona["nacionalidad"] == "sueco" and persona["mascota"] == "perro":
            puntaje += 1
        if persona["nacionalidad"] == "danes" and persona["bebida"] == "te":
            puntaje += 1
        if persona["color"] == "verde" and (esVecinoDe(aux_list, "color", "blanco", persona["posicion"]-1) or esVecinoDe(aux_list, "color", "blanco", persona["posicion"]+1)):
            puntaje += 1
        if persona["color"] == "verde" and persona["bebida"] == "cafe":
            puntaje += 1
        if persona["cigarrillo"] == "pallmall" and persona["mascota"] == "pajaro":
            puntaje += 1
        if persona["color"] == "amarillo" and persona["cigarrillo"] == "dunhill":
            puntaje += 1
        if i == 2 and persona["bebida"] == "leche":
            puntaje += 1
        if i == 0 and persona["nacionalidad"] == "noruego":
            puntaje += 1
        if persona["cigarrillo"] == "brends" and (esVecinoDe(aux_list, "mascota", "gato", persona["posicion"]+1) or esVecinoDe(aux_list, "mascota", "gato", persona["posicion"]-1)):
            puntaje += 1
        if persona["mascota"] == "caballo" and (esVecinoDe(aux_list, "cigarrillo", "dunhill", persona["posicion"]+1) or esVecinoDe(aux_list, "cigarrillo", "dunhill", persona["posicion"]-1)):
            puntaje += 1
        if persona["cigarrillo"] == "bluemaster" and persona["bebida"] == "cerveza":
            puntaje += 1
        if persona["nacionalidad"] == "aleman" and persona["cigarrillo"] == "prince":
            puntaje += 1
        if persona["nacionalidad"] == "noruego" and (viveJunto(aux_list, persona["posicion"]-1) or viveJunto(aux_list, persona["posicion"]+1)):
            puntaje += 1
        if persona["cigarrillo"] == "brends" and ((esVecinoDe(aux_list, "bebida", "agua", persona["posicion"]+1) or esVecinoDe(aux_list, "bebida", "agua", persona["posicion"]-1))):
            puntaje += 1

    return puntaje,

def esVecinoDe(pueblo, key, value, posicion):
    if posicion < 0 or posicion >= len(pueblo):
        return False
    return pueblo[posicion][key] == value

def viveJunto(pueblo, posicion):
    if posicion < 0 or posicion >= len(pueblo):
        return False
    return True

def mutarIndividuo(individuo, indpb):
    for i in range(len(individuo)):
        if random.random() < indpb:
            atributos = list(range(len(individuo[i])))
            idx = random.choice(atributos)
            nuevo_valor = random.choice(list(set(range(len(atributos))) - {idx}))
            individuo[i] = individuo[i][:idx] + (nuevo_valor,) + individuo[i][idx+1:]
    return individuo,

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("individual", tools.initIterate, creator.Individual, generarIndividuo) # Estructura inicial
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluarIndividuo) # Evaluación del individuo
toolbox.register("mate", tools.cxTwoPoint) # Cruce de dos puntos
toolbox.register("mutate", mutarIndividuo, indpb=0.05) # Mutación
toolbox.register("select", tools.selTournament, tournsize=3) # Selección

# Ejecución del algoritmo evolutivo
if __name__ == "__main__":
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, stats=stats, halloffame=hof, verbose=True)

    best_individual = tools.selBest(pop, 1)[0]
    
    print("======Población========")
    print(pop)
    print("======Log========")
    print(log)
    print("======Mejor Individuo========")
    print(best_individual)
    print("======Evaluación========")
    print(evaluarIndividuo(best_individual))
