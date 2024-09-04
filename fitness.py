from modelo import colores, nacionalidades, bebidas, cigarrillos, mascotas, posicion
#Solución
#cromosoma = [3, 3, 4, 1, 2, 0, 4, 2, 0, 4, 3, 1, 0, 0, 2, 0, 1, 2, 1, 4, 1, 3, 4, 3, 2, 1, 3, 2, 0, 4]

def fitness_deap(cromosoma):
  puntaje = 0

  colores_individuo = []
  nacionalidades_individuo = []
  bebidas_individuo = []
  cigarrillos_individuo = []
  mascotas_individuo = []
  posicion_individuo = []

  divisor = 6 #cada 6 elementos es el punto de corte

  # Parseo al individo, le doy sentido a las características
  for i in range(len(cromosoma)):
    if i % divisor == 0:
      colores_individuo.append(colores[cromosoma[i]])
    if i % divisor == 1:
      nacionalidades_individuo.append(nacionalidades[cromosoma[i]])
    if i % divisor == 2:
      bebidas_individuo.append(bebidas[cromosoma[i]])
    if i % divisor == 3:
      cigarrillos_individuo.append(cigarrillos[cromosoma[i]])
    if i % divisor == 4:
      mascotas_individuo.append(mascotas[cromosoma[i]])
    if i % divisor == 5:
      posicion_individuo.append(posicion[cromosoma[i]])
    

  # Penalizo a el individuo que tenga alguna caraterística repetida
  if len(set(colores_individuo)) != len(colores):
    puntaje += 0 
  else:
    puntaje += 10

  if len(set(nacionalidades_individuo)) != len(nacionalidades):
    puntaje += 0
  else:
    puntaje += 10

  if len(set(bebidas_individuo)) != len(bebidas):
    puntaje += 0
  else:
    puntaje += 10

  if len(set(cigarrillos_individuo)) != len(cigarrillos):
    puntaje += 0
  else:
    puntaje += 10

  if len(set(mascotas_individuo)) != len(mascotas):
    puntaje += 0
  else:
    puntaje += 10

  if len(set(posicion_individuo)) != len(posicion):
    puntaje += 0
  else:
    puntaje += 10


  # Premio a aquellos individuos que cumplan las reglas
  for i in range(5): #es 5 porque son 5 casas/personas
    #1. El británico vive en una casa roja
    if nacionalidades_individuo[i] == "britanico" and colores_individuo[i] == "rojo":
      puntaje += 1
    
    #2. El sueco tiene un perro
    if nacionalidades_individuo[i] == "sueco" and mascotas_individuo[i] == "perro":
      puntaje += 1

    #3. El danes toma te
    if nacionalidades_individuo[i] == "danes" and bebidas_individuo[i] == "te":
      puntaje += 1

    #4. El dueño de la casa verde toma cafe
    if colores_individuo[i] == "verde" and bebidas_individuo[i] == "cafe":
      puntaje += 1

    #5. La persona que fuma PallMall tiene un pájaro
    if cigarrillos_individuo[i] == "pallmall" and mascotas_individuo[i] == "pajaro":
      puntaje += 1

    #6. El dueño de la casa amarilla fuma Dunhill
    if colores_individuo[i] == "amarillo" and cigarrillos_individuo[i] == "dunhill":
      puntaje += 1

    #7. El que vive en la casa del centro toma leche
    if posicion_individuo[i] == 3 and bebidas_individuo[i] == "leche":
      puntaje += 1
    
    #8. El noruego vive en la primera casa
    if posicion_individuo[i] == 1 and nacionalidades_individuo[i] == "noruego":
      puntaje += 1

    #9. El que fuma Bluemasters bebe cerveza
    if cigarrillos_individuo[i] == "bluemaster" and bebidas_individuo[i] == "cerveza":
      puntaje += 1

    #10. El alemán fuma Prince
    if nacionalidades_individuo[i] == "aleman" and cigarrillos_individuo[i] == "prince":
      puntaje += 1

    #11. La casa verde esta a la izquierda de la casa blanca
    if i > 0 and colores_individuo[i] == "blanco" and colores_individuo[i-1] == "verde":
      puntaje += 1
      
    #12. La persona que fuma Brends vive junto a la que tiene un gato
    if cigarrillos_individuo[i] == "brends":
      if (i > 0 and i < 4 and (mascotas_individuo[i-1] == "gato" or mascotas_individuo[i+1] == "gato")) or (i==0 and mascotas_individuo[i+1] == "gato") or (i==4 and mascotas_individuo[i-1] == "gato"):
        puntaje += 10

    #13. La persona que tiene un caballo vive junto a la que fuma Dunhill
    if mascotas_individuo[i] == "caballo":
      if (i > 0 and i < 4 and (cigarrillos_individuo[i-1] == "dunhill" or cigarrillos_individuo[i+1] == "dunhill")) or (i==0 and cigarrillos_individuo[i+1] == "dunhill") or (i==4 and cigarrillos_individuo[i-1] == "dunhill"):
        puntaje += 10

    #14. El noruego vive junto a la casa azul
    if nacionalidades_individuo[i] == "noruego":
      if (i > 0 and i < 4 and (colores_individuo[i-1] == "azul" or colores_individuo[i+1] == "azul")) or (i==0 and colores_individuo[i+1] == "azul") or (i==4 and colores_individuo[i-1] == "azul"):
        puntaje += 10

    #15. El que fuma Brends tiene un vecino que toma agua
    if cigarrillos_individuo[i] == "brends":
      if (i > 0 and i < 4 and (bebidas_individuo[i-1] == "agua" or bebidas_individuo[i+1] == "agua")) or (i==0 and bebidas_individuo[i+1] == "agua") or (i==4 and bebidas_individuo[i-1] == "agua"):
        puntaje += 10
  
  #el máximo puntaje es 111
  return puntaje,
