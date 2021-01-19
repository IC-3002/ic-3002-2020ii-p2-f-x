from dominio_ag import DominioAG
from dominio_tsp import DominioTSP

class DominioAGTSP(DominioAG, DominioTSP):
    """
    Representa el objeto de dominio que conoce los detalles de implementación y modelamiento
    del problema del vendedor viajero para ser resuelto con algoritmos genéticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar(n)
        Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

    cruzar(sol_a, sol_b)
        Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

    mutar(sol)
        Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero para ser resuelto
        con algoritmos genéticos.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioAGTSP correctamente inicializada.
        """
        
        #usa los atributos de dominio_tsp
        DominioTSP.__init__(self, ciudades_rutacsv, ciudad_inicio) 

    def generar_n(self, n):
        """Construye aleatoriamente una lista de listas que representa n 
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (list) Lista que contiene n listas, cada una representando
        una posible solución al problema modelado por el objeto de dominio.
        """
        
        #implementa las funcion que ya existe de generar en dominio_tsp para calcular las soluciones
  
        
        posibles_soluciones = []

        while n > 0:
            posibles_soluciones += [DominioTSP.generar(self)]
            n -= 1

        return posibles_soluciones

    def cruzar(self, sol_a, sol_b):
        """Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

        Entradas:
        sol_a (estructura de datos)
            Estructura de datos que modela la solución antecesora A que será cruzada con la B

        sol_b (estructura de datos)
            Estructura de datos que modela la solución antecesora B que será cruzada con la A

        Salidas:
        (estructura de datos) Una nueva solución producto del cruzamiento entre las soluciones A y B
        """

        #Se parte la mitad de la solución a, y despues se le agregan a esa solución los que falten que estén en la solución b
        half = len(sol_a)//2
        solve = sol_a[:mitad]
        
        for ciudad in sol_b:
            if ciudad not in solve:
                solve.append(ciudad)
                if len(solve) == len(sol_a):
                    break
            
            
        return solve

    def mutar(self, sol):
        """Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.

        Entradas:
        sol (estructura de datos)
            La solución a mutar.
        
        Salidas:
        (estructura de datos) Una nueva solución que refleja un ligero cambio con respecto 
        a la solución dada por parámetro
        """

        #Se cambia una posicion de la primeraq mitad de la lista por una de la segunda mitad
        len_half = len(sol) // 2  
        temp1 = random.randint(0,mitad_largo-1) 
        temp2 = random.randint(mitad_largo,len(sol)-1)
        new_solve = sol[:]
        new_solve[temp1],new_solve[temp2] = new_solve[temp2],new_solve[temp1]

        return new_solve
