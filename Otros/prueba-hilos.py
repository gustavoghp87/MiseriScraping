#!/usr/bin/python

import threading
import time


def hilo(i):
	print("[+] En hilo %d\n" % i)
	time.sleep(3)
	print("[-] hilo %d finalizado\n" % i)

# Creacion y Ejecucion de 1 hilo paralelo a hilo 2

simplethread=threading.Thread(target=hilo, args=[1])
simplethread.start()

# Esto se ejecuta como proceso principal

hilo(2)

# Esperamos a que acabe el hilo paralelo 1
simplethread.join()