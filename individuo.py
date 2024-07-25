import random
import itertools
from deap import base, creator, tools, algorithms

###############################
# Atributos y posibles valores
###############################
colores        = ["rojo", "verde", "blanco", "amarillo", "azul"]
nacionalidades = ["britanico", "sueco", "danes", "noruego", "aleman"]
bebidas        = ["te", "cafe", "leche", "cerveza", "agua"]
cigarrillos    = ["pallmall", "dunhill", "bluemaster", "prince", "brends"]
mascotas       = ["perro", "pajaro", "gato", "caballo", "pez"]


########################
# Funciones principales
########################
def evaluarIndividuo(individuo):
  puntaje = 0

  #Recorro y aplico reglas
  for i, persona in enumerate(individuo):
    #El británico vive en una casa roja
    if persona["nacionalidad"] == "britanico" and persona["color"] == "rojo":
      puntaje += 1
    
    #El sueco tiene un perro
    if persona["nacionalidad"] == "sueco" and persona["mascota"] == "perro":
      puntaje += 1

    #El danes toma te
    if persona["nacionalidad"] == "danes" and persona["bebida"] == "te":
      puntaje += 1

    #El dueño de la casa verde toma cafe
    if persona["color"] == "verde" and persona["bebida"] == "cafe":
      puntaje += 1

    #La persona que fuma PallMall tiene un pájaro
    if persona["cigarrillo"] == "pallmall" and persona["mascota"] == "pajaro":
      puntaje += 1

    #El dueño de la casa amarilla fuma Dunhill
    if persona["color"] == "amarilla" and persona["cigarrillo"] == "dunhill":
      puntaje += 1
    
    #El que vive en la casa del centro toma leche
    if i == 2 and persona["bebida"] == "leche":
      puntaje += 100

    #El noruego vive en la primera casa
    if i == 0 and persona["nacionalidad"] == "noruego":
      puntaje += 100

    #El que fuma Bluemasters bebe cerveza
    if persona["cigarrillo"] == "bluemaster" and persona["bebida"] == "cerveza":
      puntaje += 1

    #El alemán fuma Prince
    if persona["nacionalidad"] == "aleman" and persona["cigarrillo"] == "prince":
      puntaje += 1

  for i, persona in enumerate(individuo):
    #La casa verde esta a la izquierda de la casa blanca
    if i > 1:
      if individuo[i]["color"] == "blanco" and individuo[i-1]["color"] == "verde":
        puntaje += 1
    
  #La persona que fuma Brends vive junto a la que tiene un gato
  puntaje += viveJunto(individuo, "cigarrillo", "brends", "mascota", "gato")

  #La persona que tiene un caballo vive junto a la que fuma Dunhill
  puntaje += viveJunto(individuo, "mascota", "caballo", "cigarrillo", "dunhill")

  #El noruego vive junto a la casa azul
  puntaje += viveJunto(individuo, "nacionalidad", "noruego", "color", "azul")

  #El que fuma Brends tiene un vecino que toma agua
  puntaje += viveJunto(individuo, "cigarrillo", "brends", "bebida", "agua")


  return puntaje,


def generarIndividuo():
  individuo = []

  chosenColors = set()
  chosenNacionality = set()
  chosenDrink = set()
  chosenCigarret = set()
  chosenPet = set()

  agregarAtributos(chosenColors, colores)
  agregarAtributos(chosenNacionality, nacionalidades)
  agregarAtributos(chosenDrink, bebidas)
  agregarAtributos(chosenCigarret, cigarrillos)
  agregarAtributos(chosenPet, mascotas)

  actualizarIndividuo(individuo, chosenColors, chosenNacionality, chosenDrink, chosenCigarret, chosenPet)
  
  return individuo


def cruzar(ind1, ind2):
  # Realiza el cruce de dos puntos definidos
  hijo1 = ind1[:2] + ind2[2:4] + ind1[4:5]
  hijo2 = ind2[:2] + ind1[2:4] + ind2[4:5]

  hijo1Revisado = controlarAtributosRepetidos(hijo1)
  hijo2Revisado = controlarAtributosRepetidos(hijo2)

  return creator.Individual(hijo1Revisado), creator.Individual(hijo2Revisado)


def mutarIndividuo(individuo, indpb):
  if random.random() < indpb:
      ind2 = generarIndividuo()
      individuoMutado, _ = cruzar(individuo, ind2)
      return creator.Individual(individuoMutado),
  return individuo,





#######################
# Funciones auxiliares
#######################
def viveJunto(individuo, clavePivot, valorPivot, claveVecino, valorVecino):
  puntos = 0
  for i, persona in enumerate(individuo):
    if i > 1 and i < 4:
      if individuo[i][clavePivot] == valorPivot and (individuo[i-1][claveVecino] == valorVecino or individuo[i+1][claveVecino] == valorVecino):
        puntos += 1
    elif i==1:
      if individuo[i][clavePivot] == valorPivot and individuo[i+1][claveVecino] == valorVecino:
        puntos += 1
    elif i==4:
      if individuo[i][clavePivot] == valorPivot and individuo[i-1][claveVecino] == valorVecino:
        puntos += 1
  
  return puntos

def controlarAtributosRepetidos(individuo):
  coloresExistentes = set()
  nacionalidadesExistentes = set()
  bebidasExistentes = set()
  cigarrillosExistentes = set()
  mascotasExistentes = set()
  
  for gen in individuo:
    coloresExistentes.add(gen["color"])
    nacionalidadesExistentes.add(gen["nacionalidad"])
    bebidasExistentes.add(gen["bebida"])
    cigarrillosExistentes.add(gen["cigarrillo"])
    mascotasExistentes.add(gen["mascota"])
  
  agregarAtributos(coloresExistentes, colores)
  agregarAtributos(nacionalidadesExistentes, nacionalidades)
  agregarAtributos(bebidasExistentes, bebidas)
  agregarAtributos(cigarrillosExistentes, cigarrillos)
  agregarAtributos(mascotasExistentes, mascotas)

  actualizarIndividuo(individuo, coloresExistentes, nacionalidadesExistentes, bebidasExistentes, cigarrillosExistentes, mascotasExistentes)

  return individuo

def agregarAtributos(atributosExistentes, atributos):
  while len(atributosExistentes) < len(atributos): 
    atributosExistentes.add(random.choice(atributos))
    
def actualizarIndividuo(individuo, nuevosColores, nuevasNacionalidades, nuevasBebidas, nuevosCigarrillos, nuevasMascotas):
    for i in range(len(nuevosColores)):
        if i < len(individuo):
            # Si el individuo ya tiene elementos, actualizamos sus atributos
            individuo[i]["color"] = list(nuevosColores)[i]
            individuo[i]["nacionalidad"] = list(nuevasNacionalidades)[i]
            individuo[i]["bebida"] = list(nuevasBebidas)[i]
            individuo[i]["cigarrillo"] = list(nuevosCigarrillos)[i]
            individuo[i]["mascota"] = list(nuevasMascotas)[i]
        else:
            # Si el individuo tiene menos de 5 elementos, agregamos nuevos
            gen = {
                "color": list(nuevosColores)[i],
                "nacionalidad": list(nuevasNacionalidades)[i],
                "bebida": list(nuevasBebidas)[i],
                "cigarrillo": list(nuevosCigarrillos)[i],
                "mascota": list(nuevasMascotas)[i]
            }
            individuo.append(gen)

def modificarUnAtributo(individuo):
  atributos = ["color", "nacionalidad", "bebida", "cigarillo", "mascota"]
  atributoAModificar = random.choice(atributos)
  valorAModificar = random.choice(atributoAModificar)

  for i, atr in enumerate(atributosAModificar):
    individuo[i][atr] = random.choice(atr)




[{'color': 'blanco', 'nacionalidad': 'danes', 'bebida': 'te', 'cigarrillo': 'prince', 'mascota': 'gato'}, 
 {'color': 'amarillo', 'nacionalidad': 'sueco', 'bebida': 'cerveza', 'cigarrillo': 'pallmall', 'mascota': 'pajaro'}, 
 {'color': 'rojo', 'nacionalidad': 'britanico', 'bebida': 'leche', 'cigarrillo': 'bluemaster', 'mascota': 'caballo'}, 
 {'color': 'azul', 'nacionalidad': 'aleman', 'bebida': 'cafe', 'cigarrillo': 'brends', 'mascota': 'perro'}, 
 {'color': 'verde', 'nacionalidad': 'noruego', 'bebida': 'agua', 'cigarrillo': 'dunhill', 'mascota': 'pez'}]