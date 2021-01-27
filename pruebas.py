import time
from simulated_annealing import optimizar as optimizar_sa
from algoritmo_genetico import optimizar as optimizar_ag
from dominio_tsp import DominioTSP
from dominio_ag_tsp import DominioAGTSP

def simulated_annealing():
    
    temperatura = 1e41
    tasa_enfriamiento = 0.999888
    
    archivo = open('resultados.txt', 'a')
    archivo.write("\n\n"+"Parámetros combinados 3 simulated annealing(temperatura = "+str(temperatura)+", tasa_enfriamiento = "+str(tasa_enfriamiento)+")")
    archivo.close()

    inicio_total = time.perf_counter()
    
    for i in range(0,20):
        inicio = time.perf_counter()
        dominio = DominioTSP('datos/ciudades_cr.csv', 'Liberia')
        sol = optimizar_sa(dominio, temperatura, tasa_enfriamiento)
        final = time.perf_counter()
        tiempo = final-inicio
        print(tiempo)
        print("Iteración:",i,"Recorrido:", DominioTSP.texto(dominio, sol), "Costo:", DominioTSP.fcosto(dominio, sol))

        archivo = open('resultados.txt', 'a')
        archivo.write("\n"+"Iteración: "+str(i)+" Tiempo: "+str(tiempo)+" Costo:"+str(DominioTSP.fcosto(dominio, sol))+" Recorrido: "+ str(DominioTSP.texto(dominio, sol)))
        archivo.close()

    final_total = time.perf_counter()
    duracion_total = final_total-inicio_total
    
    print(duracion_total)

    return 0

def algoritmo_genetico():

    tam_pobl = 1000
    porc_elite = 0.5
    prob_mut = 0.9
    reps = 10000
    
    archivo = open('resultados.txt', 'a')
    archivo.write("\n\n"+"Parámetros combinados 3 algoritmo genético(tam_pobl = "+str(tam_pobl)+", porc_elite = "+str(porc_elite)+", prob_mut = "+str(prob_mut)+", reps = "+str(reps)+")")
    archivo.close()

    inicio_total = time.perf_counter()

    for i in range(0,20):
        inicio = time.perf_counter()
        dominio = DominioAGTSP('datos/ciudades_cr.csv', 'Liberia')
        sol = optimizar_ag(dominio, tam_pobl, porc_elite, prob_mut, reps)
        final = time.perf_counter()
        tiempo = final-inicio
        print(tiempo)
        print("Iteración:",i,"Recorrido:", DominioAGTSP.texto(dominio, sol), "Costo:", DominioAGTSP.fcosto(dominio, sol))

        archivo = open('resultados.txt', 'a')
        archivo.write("\n"+"Iteración: "+str(i)+" Tiempo: "+str(tiempo)+" Costo:"+str(DominioAGTSP.fcosto(dominio, sol))+" Recorrido: "+ str(DominioAGTSP.texto(dominio, sol)))
        archivo.close()

    
    final_total = time.perf_counter()
    duracion_total = final_total-inicio_total

    print(duracion_total)
    return 0

print(simulated_annealing())
print(algoritmo_genetico())

