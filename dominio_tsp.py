from dominio import Dominio
import csv
import random

class DominioTSP(Dominio):
    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolución
    con algoritmos probabilísticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar()
        Construye aleatoriamente una lista que representa una posible solución al problema.

    fcosto(sol)
        Calcula el costo asociado con una solución dada.

    vecino(sol)
        Calcula una solución vecina a partir de una solución dada.

    validar(sol)
        Valida que la solución dada cumple con los requisitos del problema.

    texto(sol)
        Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.
    """

    def __init__(self, ciudades_rutacsv, ciudad_inicio):
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
        """

        self.matriz = []
        self.costos = []

        with open(ciudades_rutacsv) as f:
            lectura = csv.reader(f, delimiter = ',')

            for row in lectura:
                self.matriz.append(row[1:])
        
        self.ciudades = self.matriz[0]
        self.pos_ciudad_inicio = self.ciudades.index(ciudad_inicio)
        self.cantidad_ciudades = len(self.ciudades)
        self.recorrido = self.matriz[self.pos_ciudad_inicio+1]
        self.costos = self.matriz[1:]

    def validar(self, sol):
        """Valida que la solución dada cumple con los requisitos del problema.

        Si n es el número de ciudades en el grafo, la solución debe:
        - Tener tamaño (n-1)
        - Contener sólo números enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (list)
            La solución a validar.

        Salidas:
        (bool) True si la solución es válida, False en cualquier otro caso
        """
        tamano = len(sol)

        if tamano == (self.cantidad_ciudades-1):
            
            for i in sol:

                if i == self.pos_ciudad_inicio:
                    
                    return False
                
                elif type(i) != int:

                    return False
                
                elif i > (self.cantidad_ciudades-1) or i < 0:

                    return False

            repetidos = []
            for j in sol:

                if j not in repetidos:

                    repetidos.append(j)

                else:

                    return False
            
        
            return True

        else:

            return False

    def texto(self, sol):
        
        """Construye una representacion en hilera legible por humanos de la solucion
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (list)
            Solucion a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """

        ciudades = []
        ciudades.append(self.ciudades[self.pos_ciudad_inicio])

        for i in sol:
            ciudades.append(self.ciudades[i])

        ciudades.append(self.ciudades[self.pos_ciudad_inicio])

        return " -> ".join(ciudades)

    def generar(self):
        """Construye aleatoriamente una lista que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        (list) Una lista que representa una solución válida para esta instancia del vendedor viajero
        """

        lista = [i for i in range(0, self.cantidad_ciudades)]       
        lista.remove(self.pos_ciudad_inicio)                           
        random.shuffle(lista)                                   
        return lista

    def fcosto(self, sol):
        """Calcula el costo asociado con una solución dada.

        Entradas:
        sol (list)
            Solución cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solución
        """
        costo = 0
        ciudad = self.pos_ciudad_inicio
        
        for i in range(0, len(sol)):
          costo += float(self.costos[ciudad][sol[i]])
          ciudad = sol[i]
        
        costo += float(self.costos[ciudad][self.pos_ciudad_inicio])
        return costo
        
    def vecino(self, sol):
        """Calcula una solución vecina a partir de una solución dada.

        Una solución vecina comparte la mayor parte de su estructura con 
        la solución que la origina, aunque no son exactamente iguales. El 
        método transforma aleatoriamente algún aspecto de la solución
        original.

        Entradas:
        sol (list)
            Solución a partir de la cual se originará una nueva solución vecina

        Salidas:
        (list) Solución vecina
        """

        vecino = sol[:]
        mitad_sol = len(sol) // 2
        temp1 = random.randint(0,mitad_sol-1) 
        temp2 = random.randint(mitad_sol,len(sol)-1)
        vecino[temp1],vecino[temp2] = vecino[temp2],vecino[temp1]

        return vecino
      
