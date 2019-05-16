from threading import Thread
import time

listTot=[0.0,0.0,0.0,0.0]

def fibonacci(x):
    if x<2:
        return x
    else:
       return  (fibonacci(x-1) + fibonacci(x-2))

def printfibVal(z, list, indice):
    time1=time.time()
    resul=(fibonacci(z))
    time2=time.time()
    timet= time2 - time1
    listTot[indice]=timet
    print   ("Para : %s : fibonacci : %s tiempo : %s" % (z,resul, timet) )
    
    


#if __name__ == "__main__":
   
thread1 = Thread(target = printfibVal, args = (34,listTot,0 ))
thread1.start()
thread2 = Thread(target = printfibVal, args = (37,listTot,1 ))
thread2.start()
thread3 = Thread(target = printfibVal, args = (35,listTot,2 ))
thread3.start()
thread4 = Thread(target = printfibVal, args = (36,listTot,3 ))
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
print ("thread finished...exiting")

suma =0
for i in listTot:
    suma = suma + i
print ("Promedio : %s" %(suma/4))
