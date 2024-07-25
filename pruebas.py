import random

# Atributos y posibles valores
colores        = ["rojo", "verde", "blanco", "amarillo", "azul"]
nacionalidades = ["britanico", "sueco", "danes", "noruego", "aleman"]
bebidas        = ["te", "cafe", "leche", "cerveza", "agua"]
cigarrillos    = ["pallmall", "dunhill", "bluemaster", "prince", "brends"]
mascotas       = ["perro", "pajaro", "gato", "caballo", "pez"]

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

  for i, gen in enumerate(individuo):
    gen["color"] =  list(coloresExistentes)[i]
    gen["nacionalidad"] = list(nacionalidadesExistentes)[i]
    gen["bebida"] = list(bebidasExistentes)[i]
    gen["cigarrillo"] = list(cigarrillosExistentes)[i]
    gen["mascota"] = list(mascotasExistentes)[i]

  return individuo

def agregarAtributos(atributosExistentes, atributos):
  while len(atributosExistentes) < len(atributos): 
    atributosExistentes.add(random.choice(atributos))
    

ind1 = [
  {'color': 'amarillo', 'nacionalidad': 'sueco', 'bebida': 'cerveza', 'cigarrillo': 'bluemaster', 'mascota': 'gato'}, 
  {'color': 'rojo', 'nacionalidad': 'britanico', 'bebida': 'agua', 'cigarrillo': 'pallmall', 'mascota': 'pajaro'}, 
  {'color': 'azul', 'nacionalidad': 'danes', 'bebida': 'leche', 'cigarrillo': 'brends', 'mascota': 'perro'}, 
  {'color': 'verde', 'nacionalidad': 'noruego', 'bebida': 'cafe', 'cigarrillo': 'prince', 'mascota': 'caballo'}, 
  {'color': 'blanco', 'nacionalidad': 'aleman', 'bebida': 'te', 'cigarrillo': 'dunhill', 'mascota': 'pez'}
]

ind2 = [
  {'color': 'rojo', 'nacionalidad': 'britanico', 'bebida': 'te', 'cigarrillo': 'pallmall', 'mascota': 'pajaro'}, 
  {'color': 'blanco', 'nacionalidad': 'aleman', 'bebida': 'agua', 'cigarrillo': 'dunhill', 'mascota': 'pez'}, 
  {'color': 'verde', 'nacionalidad': 'noruego', 'bebida': 'cafe', 'cigarrillo': 'brends', 'mascota': 'caballo'}, 
  {'color': 'amarillo', 'nacionalidad': 'sueco', 'bebida': 'cerveza', 'cigarrillo': 'bluemaster', 'mascota': 'perro'}, 
  {'color': 'azul', 'nacionalidad': 'danes', 'bebida': 'leche', 'cigarrillo': 'prince', 'mascota': 'gato'}
]


# hijo = [
#   {'color': 'amarillo', 'nacionalidad': 'sueco', 'bebida': 'cerveza', 'cigarrillo': 'bluemaster', 'mascota': 'gato'},  x
#   {'color': 'rojo', 'nacionalidad': 'britanico', 'bebida': 'agua', 'cigarrillo': 'pallmall', 'mascota': 'pajaro'},     x
#   {'color': 'verde', 'nacionalidad': 'noruego', 'bebida': 'cafe', 'cigarrillo': 'brends', 'mascota': 'caballo'},       y
#   {'color': 'amarillo', 'nacionalidad': 'sueco', 'bebida': 'cerveza', 'cigarrillo': 'bluemaster', 'mascota': 'perro'}, y
#   {'color': 'blanco', 'nacionalidad': 'aleman', 'bebida': 'te', 'cigarrillo': 'dunhill', 'mascota': 'pez'}             x
# ]
## Se repite: 
# color amarillo; 
# nacionalidad sueco; 
# bebida cerveza; 
# cigarrillo bluemaster


# Resultado
# [
#   {'color': 'azul', 'nacionalidad': 'danes', 'bebida': 'cafe', 'cigarrillo': 'brends', 'mascota': 'gato'}, 
#   {'color': 'amarillo', 'nacionalidad': 'aleman', 'bebida': 'agua', 'cigarrillo': 'dunhill', 'mascota': 'pajaro'}, 
#   {'color': 'rojo', 'nacionalidad': 'sueco', 'bebida': 'leche', 'cigarrillo': 'pallmall', 'mascota': 'pez'}, 
#   {'color': 'blanco', 'nacionalidad': 'britanico', 'bebida': 'te', 'cigarrillo': 'bluemaster', 'mascota': 'caballo'}, 
#   {'color': 'verde', 'nacionalidad': 'noruego', 'bebida': 'cerveza', 'cigarrillo': 'prince', 'mascota': 'perro'}
#   ]

def cruzar(ind1, ind2):
  # Realiza el cruce de dos puntos definidos
  hijo = ind1[:2] + ind2[2:4] + ind1[4:5]

  hijoRevisado = controlarAtributosRepetidos(hijo)

  return hijoRevisado,

print(cruzar(ind1, ind2))



