from dominio_ag_tsp import DominioAGTSP
from operator import itemgetter
import random
    
def optimizar(dominio, tam_pobl, porc_elite, prob_mut, reps):
    """Algoritmo genético para optimización estocástica.

    Entradas:
    dominio (DominioAG)
        Un objeto que modela el dominio del problema que se quiere aproximar.
    
    tam_pobl (int)
        Tamaño de la población.
    
    porc_elite (float)
        Porcentaje de la población que se tomará como elite.
    
    prob_mut (float)
        Probabilidad de mutación, debe estar en el rango [0, 1]
    
    reps (int)
        Número de iteraciones a ejecutar.

    Salidas:
        (estructura de datos) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """
    
    poblacion = dominio.generar_n(tam_pobl)

    while reps > 0:
        
        poblacion_costo = []
        
        for solve in poblacion:
            poblacion_costo.append((solve, dominio.fcosto(solsolve)))
        
        poblacion_costo.sort(key = itemgetter(1))
        
        cant_padres = int(len(poblacion) * porc_elite)
        cant_hijos = len(poblacion) - cant_padres
        sig_generacion = []
        elite = poblacion_costo[:cant_padres]
        for solve in elite:
            sig_generacion.append(solve[0])
        descendencia = []
        
        while cant_hijos > 0:
            padre1 = sig_generacion[random.randint(0, len(sig_generacion) -1)]
            padre2 = sig_generacion[random.randint(0, len(sig_generacion) -1)]
            hijo = dominio.cruzar(padre1, padre2)
            probabilidad = random.random()
            if probabilidad <= prob_mut:
                hijo = dominio.mutar(hijo)
            descendencia.append(hijo)
            cant_hijos -= 1
        
        for hijos in descendencia:
            sig_generacion.append(hijos)
        probabilidad = sig_generacion
        reps -= 1
    
    #Si se vuelve a ordenar se podia saber si en la última descendencia hay una mejor solucion que en la anterior
    return poblacion_costo[0][0]
