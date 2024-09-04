import random

# Mi cromosoma tiene que ser un array de 30 elemenos porque tiene que incluir al fixture completo (6 genes * 5 casas/personas). La base: del 0 al 5
# [4, 3, 3, 1, 1, 2, 0, 2, 1, 4, 4, 2, 1, 0, 0, 0, 1, 3, 4, 2, 2, 3, 1, 3, 0, 2, 2, 1, 1, 3]
# |1, 1, 1, 1, 1, 1| 2, 2, 2, 2, 2, 2| 3, 3, 3, 3, 3, 3| 4, 4, 4, 4, 4, 4| 5, 5, 5, 5, 5, 5|
# |  persona 1.    |   persona 2.    |  persona 3.     |  persona 5.     |   persona 5.    |
# |0              5|6              11|12             17|18             23|24             29|
import random

# Genes/Características
#                    0            1           2             3         4
colores        = ["rojo",      "verde",   "blanco",     "amarillo", "azul"  ]      # 1        
nacionalidades = ["britanico", "sueco",   "danes",      "noruego",  "aleman"]      # 2
bebidas        = ["te",        "cafe",    "leche",      "cerveza",  "agua"  ]      # 3
cigarrillos    = ["pallmall",  "dunhill", "bluemaster", "prince",   "brends"]      # 4
mascotas       = ["perro",     "pajaro",  "gato",       "caballo",  "pez"   ]      # 5
posicion       = [1,           2,          3,           4,          5       ]      # 6
