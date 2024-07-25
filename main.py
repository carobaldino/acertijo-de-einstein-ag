import array
import numpy as np
from deap import base, creator, tools, algorithms
from individuo import crear_individuo, colores, nacionalidades, bebidas, cigarrillos, mascotas
import random


# Creación de la clase fitness y del individuo
creator.create("FitnessMax", base.Fitness, weights=(1.0,)) #problema de maximización
creator.create("Individual", list, fitness=creator.FitnessMax)


# Toolbox: registro atributos, individuo y pobración
toolbox = base.Toolbox()
toolbox.register("atributos", crear_individuo)
toolbox.register("individuo", tools.initRepeat, creator.Individual, toolbox.atributos, 5)
toolbox.register("poblacion", tools.initRepeat, list, toolbox.individuo)


# Evaluar: f: cromosoma/individuo -> R. Aplico las reglas del enunciado.
def evaluar_individuo(poblacion):
  puntaje = 0

  for i, individuo in enumerate(poblacion):
    #El británico vive en una casa roja
    if individuo["nacionalidad"] == "britanico" and individuo["color"] == "rojo":
      puntaje += 1
    
    #El sueco tiene un perro
    if individuo["nacionalidad"] == "sueco" and individuo["mascota"] == "perro":
      puntaje += 1

    #El danes toma te
    if individuo["nacionalidad"] == "danes" and individuo["bebida"] == "te":
      puntaje += 1

    #La casa verde esta a la izquierda de la casa blanca
    if individuo["color"] == "verde" and i < len(poblacion) - 1 and poblacion[i+1]["color"] == "blanco":
      puntaje += 1

    #El dueño de la casa verde toma cafe
    if individuo["color"] == "verde" and individuo["bebida"] == "cafe":
      puntaje += 1

    #La persona que fuma PallMall tiene un pájaro
    if individuo["cigarrillo"] == "pallmall" and individuo["mascota"] == "pajaro":
      puntaje += 1

    #El dueño de la casa amarilla fuma Dunhill
    if individuo["color"] == "amarilla" and individuo["cigarrillo"] == "dunhill":
      puntaje += 1

    #El que vive en la casa del centro toma leche
    if i == 2 and individuo["bebida"] == "leche":
      puntaje += 1

    #El noruego vive en la primera casa
    if i == 0 and individuo["nacionalidad"] == "noruego":
      puntaje += 1

    #La persona que fuma Brends vive junto a la que tiene un gato
    if individuo["cigarrillo"] == "brends" and 0 < i < len(poblacion) - 1 and (poblacion[i - 1]["mascota"] == "gato" or poblacion[i + 1]["mascota"] == "gato"):
      puntaje += 1

    #La persona que tiene un caballo vive junto a la que fuma Dunhill
    if individuo["mascota"] == "caballo" and 0 < i < len(poblacion) - 1 and (poblacion[i - 1]["cigarrillo"] == "dunhill" or poblacion[i + 1]["cigarrillo"] == "dunhill"):
      puntaje += 1

    #El que fuma Bluemasters bebe cerveza
    if individuo["cigarrillo"] == "bluemaster" and individuo["bebida"] == "cerveza":
      puntaje += 1

    #El alemán fuma Prince
    if individuo["nacionalidad"] == "aleman" and individuo["cigarrillo"] == "prince":
      puntaje += 1

    #El noruego vive junto a la casa azul
    if individuo["nacionalidad"] == "noruego" and 0 < i < len(poblacion) - 1 and (poblacion[i - 1]["color"] == "azul" or poblacion[i + 1]["color"] == "azul"):
      puntaje += 1

    #El que fuma Brends tiene un vecino que toma agua   
    if individuo["cigarrillo"] == "brends" and 0 < i < len(poblacion) - 1 and (poblacion[i - 1]["bebida"] == "agua" or poblacion[i + 1]["bebida"] == "agua"):
      puntaje += 1

  return puntaje,

toolbox.register("evaluate", evaluar_individuo)
toolbox.register("mate", tools.cxTwoPoint)

def mutar_individuo(individuo):
  atributos = {
    "color": colores,
    "nacionalidad": nacionalidades,
    "bebida": bebidas,
    "cigarrillo": cigarrillos,
    "mascota": mascotas
  }
  # Seleccionar un índice aleatorio en la lista de diccionarios
  idx = random.randint(0, len(individuo) - 1)
  # Seleccionar un atributo aleatorio para mutar
  atributo_a_mutar = random.choice(list(atributos.keys()))
  # Mutar el atributo seleccionado
  individuo[idx][atributo_a_mutar] = random.choice(atributos[atributo_a_mutar])
  return individuo,



toolbox.register("mutate", mutar_individuo) #(the independent probability of each attribute to be mutated indpb)
toolbox.register("select", tools.selTournament, tournsize=3)


def main():  
  # print("Hello world!")
  # print("\nPoblación")
  # population = toolbox.poblacion(n=300)
  # for i, ind in enumerate(population):
  #   print(f"\tSolucion {i+1}: {ind}")
  # Parámetros del algoritmo
  population = toolbox.poblacion(n=500)
  ngen = 500
  cxpb = 0.7
  mutpb = 0.2

  # Ejecución del algoritmo
  algorithms.eaSimple(population, toolbox, cxpb, mutpb, ngen, verbose=True)

  # Verificar la mejor solución encontrada
  best_individual = tools.selBest(population, 1)[0]
  print(f"Mejor Individuo: {best_individual}")
  print(f"Evaluación: {evaluar_individuo(best_individual)}")



if __name__ == "__main__":
  main()