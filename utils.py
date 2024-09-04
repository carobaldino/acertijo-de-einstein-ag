
import random
from modelo import colores, nacionalidades, bebidas, cigarrillos, mascotas, posicion

# Estuve usando este métdo como inicializador pero, tiene poca diversidad de genes. Para usarlo al algoritmo se hace lo siguiente:
#1. Se deja sin usar:
# toolbox.register("attr_int", random.randint, a = 0, b = 4)
#2. Inicializamos directo al individuo:
# toolbox.register("individual", tools.initRepeat, creator.Individual, inicializar_cromosoma)

def inicializar_cromosoma():
  base = [0, 1, 2, 3, 4]
  
  # Inicializo las listas para cada grupo de características
  ind_colores = random.sample(base, len(base))
  ind_nacionalidades = random.sample(base, len(base))
  ind_bebidas = random.sample(base, len(base))
  ind_cigarrillos = random.sample(base, len(base))
  ind_mascotas = random.sample(base, len(base))
  ind_posiciones = random.sample(base, len(base))

  # Combino todas las listas en un cromosoma
  cromosoma = []
  for i in range(5):
    cromosoma.append(ind_colores[i])
    cromosoma.append(ind_nacionalidades[i])
    cromosoma.append(ind_bebidas[i])
    cromosoma.append(ind_cigarrillos[i])
    cromosoma.append(ind_mascotas[i])
    cromosoma.append(ind_posiciones[i])
  
  return cromosoma

# Para pruebas:
def imprimir_cromosoma(cromosoma):
  #cromosoma = inicializar_cromosoma()
  print("Cromosoma: ", cromosoma)
  divisor = 6

  colores_individuo = []
  nacionalidades_individuo = []
  bebidas_individuo = []
  cigarrillos_individuo = []
  mascotas_individuo = []
  posicion_individuo = []

  # Parseo al individo, le doy sentido a las características
  for i in range(len(cromosoma)):
    posicion_persona = i % divisor

    if posicion_persona == 0:
      colores_individuo.append(colores[cromosoma[i]])
    if posicion_persona == 1:
      nacionalidades_individuo.append(nacionalidades[cromosoma[i]])
    if posicion_persona == 2:
      bebidas_individuo.append(bebidas[cromosoma[i]])
    if posicion_persona == 3:
      cigarrillos_individuo.append(cigarrillos[cromosoma[i]])
    if posicion_persona == 4:
      mascotas_individuo.append(mascotas[cromosoma[i]])
    if posicion_persona == 5:
      posicion_individuo.append(posicion[cromosoma[i]])

  for i in range (5):
    print("Color:\t\t", colores_individuo[i])
    print("Nacionalidad:\t", nacionalidades_individuo[i])
    print("Bebida:\t\t", bebidas_individuo[i])
    print("Cigarrillo:\t", cigarrillos_individuo[i])
    print("Mascota:\t", mascotas_individuo[i])
    print("Posicion:\t", posicion_individuo[i])
    print("\n")
