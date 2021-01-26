import time
from simulated_annealing import optimizar
from dominio_tsp import DominioTSP

def simulated_annealing():
    
    temperatura = 1e6
    tasa_enfriamiento = 0.999

    for i in range(0,500):
        dominio = DominioTSP('datos/ciudades_cr.csv', 'Liberia')
        sol = optimizar(dominio, temperatura, tasa_enfriamiento)

        print("Recorrido:", DominioTSP.texto(dominio, sol), "Costo:", DominioTSP.fcosto(dominio, sol))

    return 0

print(simulated_annealing())
