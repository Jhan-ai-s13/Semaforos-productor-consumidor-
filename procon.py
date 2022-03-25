import threading
n = 10 # de elementos creados que aun no se han agregado al buffer

producir = threading.Semaphore(10) #sueteres por producir
disponibles = threading.Semaphore(0) #sueteres disponibles para el consumo
bodega = threading.Semaphore(1) #buffer en uso?
buffer = list()

def productor():
    while (1):
        elemento = "sueter"
        producir.acquire() 
        bodega.acquire()
        print("Poniendo sueter a la bodega en el espacio", len(buffer))
        print("[faltan %d sueteres por producir]"%producir._value,bodega._value)
        buffer.append(elemento)
        bodega.release()
        disponibles.release()
        
def consumidor():
    while(1):
        disponibles.acquire()
        bodega.acquire()
        print("Adquiriendo sueter de la bodega en el espacio", len(buffer)-1)
        print("[sueter %d obtenido]" %producir._value,bodega._value)
        buffer.pop()
        bodega.release()
        producir.release()

def main():
    hilo1 = threading.Thread(target=productor)
    hilo2 = threading.Thread(target=consumidor)
    hilo1.start()
    hilo2.start()
    
main()