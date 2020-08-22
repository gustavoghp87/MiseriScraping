import urllib.request
import time
import xlsxwriter

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

import tkinter as tk
from tkinter import ttk
import pymongo
import threading

print("\n\n\n\n            ######## BUEN DÍA ESTIMADO/A! ######## \n                ### ESTO ES MISERISCRAPING ### \n\nEl usuario ingresa calle de Argentina y las alturas mínima y máxima para obtener los números telefónicos registrados de cada vivienda. Exporta a excel automáticamente; el archivo se encontrará en la misma carpeta donde esté este programa. Enjoy it.-\n\n")



#calle = input("\nCalle: ").lower().strip()

def scrapear(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1):

	pares2 = pares1
	impares2 = impares1
	
	cp2 = cp1
	cp3 = False
	try:
		cp2 = int(cp2)
		cp3 = True
	except:
		cp3 = False
	

	print("Comenzando:", calle1, min1 + "-" + max1, jurisdicción1, cp1, ", pares", pares1, "impares", impares1)
	calle = calle1.lower().strip()

	print("Calle: " + calle)
	while (calle.find('ñ') != -1):
		pos = calle.find('ñ')
		calle = calle[0:pos] + 'n' + calle[pos+1:]

	while (calle.find(' ') != -1):
		pos = calle.find(' ')
		calle = calle[0:pos] + '-' + calle[pos+1:]

	while (calle.find('á') != -1):
		pos = calle.find('á')
		calle = calle[0:pos] + 'a' + calle[pos+1:]

	while (calle.find('é') != -1):
		pos = calle.find('é')
		calle = calle[0:pos] + 'e' + calle[pos+1:]

	while (calle.find('í') != -1):
		pos = calle.find('í')
		calle = calle[0:pos] + 'i' + calle[pos+1:]

	while (calle.find('ó') != -1):
		pos = calle.find('ó')
		calle = calle[0:pos] + 'o' + calle[pos+1:]

	while (calle.find('ú') != -1):
		pos = calle.find('ú')
		calle = calle[0:pos] + 'u' + calle[pos+1:]

	while (calle.find('ü') != -1):
		pos = calle.find('ü')
		calle = calle[0:pos] + 'u' + calle[pos+1:]


	min = int(min1)
	max = int(max1)

	if (max < min):
		print("Invirtiendo extremos...")
		auxiliar = min
		min = max
		max = auxiliar

	
	jurisdiccion = jurisdicción1.lower().strip()

	while (jurisdiccion.find('ñ') != -1):
		pos = jurisdiccion.find('ñ')
		jurisdiccion = jurisdiccion[0:pos] + 'n' + jurisdiccion[pos+1:]

	while (jurisdiccion.find(' ') != -1):
		pos = jurisdiccion.find(' ')
		jurisdiccion = jurisdiccion[0:pos] + '-' + jurisdiccion[pos+1:]

	while (jurisdiccion.find('á') != -1):
		pos = jurisdiccion.find('á')
		jurisdiccion = jurisdiccion[0:pos] + 'a' + jurisdiccion[pos+1:]

	while (jurisdiccion.find('é') != -1):
		pos = jurisdiccion.find('é')
		jurisdiccion = jurisdiccion[0:pos] + 'e' + jurisdiccion[pos+1:]

	while (jurisdiccion.find('í') != -1):
		pos = jurisdiccion.find('í')
		jurisdiccion = jurisdiccion[0:pos] + 'i' + jurisdiccion[pos+1:]

	while (jurisdiccion.find('ó') != -1):
		pos = jurisdiccion.find('ó')
		jurisdiccion = jurisdiccion[0:pos] + 'o' + jurisdiccion[pos+1:]

	while (jurisdiccion.find('ú') != -1):
		pos = jurisdiccion.find('ú')
		jurisdiccion = jurisdiccion[0:pos] + 'u' + jurisdiccion[pos+1:]
		
	while (jurisdiccion.find('ü') != -1):
		pos = jurisdiccion.find('ü')
		jurisdiccion = jurisdiccion[0:pos] + 'u' + jurisdiccion[pos+1:]


	#print("\n-----> Se van a rastrillar " +str(cantidad) + " direcciones en " + jurisdiccion)

	dia = int(time.time())
	archivo = calle +"_" + str(dia) + ".xlsx"
	wb = xlsxwriter.Workbook(archivo)
	ws = wb.add_worksheet()
	ws.write(0, 0, "DIRECCIONES")
	ws.set_column('A:A', 30)
	ws.write(0, 1, "TELÉFONOS")
	ws.set_column('B:B', 16)
	ws.write(0, 2, "JURISDICCIÓN: " +jurisdiccion.upper())
	ws.set_column('C:C', 25)
	ws.set_column('E:E', 14)

	scrapear2(calle, min, max, pares2, impares2, jurisdiccion, cp2, cp3, wb, ws)
	monging(calle, min, max, pares2, impares2, jurisdiccion, cp2, dia)

	##################################################################################################

def monging(calle, min, max, pares2, impares2, jurisdiccion, cp2, dia):
	json = {
		'calle': calle,
		'min': min,
		'max': max,
		'pares': pares2,
		'impares': impares2,
		'jurisdiccion': jurisdiccion,
		'cp': cp2,
		'timestamp': dia
	}

	try:
		myclient = pymongo.MongoClient("mongodb://ms:0123456789Mise20200123456789Mise@3.22.60.96:46016/miseriscraping")
		mydb = myclient["miseriscraping"]
		mydb.busquedas.insert_one(json)
	except:
		print(".")

def scrapear2(calle, min, max, pares2, impares2, jurisdiccion, cp2, cp3, wb, ws):

	cantidad = max - min + 1
	q = 2

	for i in range(0, cantidad):
		
		numero = str(min + i)

		if pares2 == True and int(numero)%2 == 0:
			pass
		elif impares2 == True and int(numero)%2 == 1:
			pass
		else:
			continue

		unoMas = "si"
		contador1 = 0

		for j in range(1, 50):

			if unoMas == "si":
				pass
			else:
				continue

			direccion = 'http://www.paginasblancas.com.ar/direccion/s/' +calle +'-' +numero +'/' +jurisdiccion + "/p-" + str(j)

			try:
				datos = urllib.request.urlopen(direccion).read().decode()
			except HTTPError as e:
				print(e)
			except URLError:
				print("Servidor caído o problemas de red... Intente de nuevo")

			soup =  BeautifulSoup(datos, "html.parser")
			
			print("\nCalle " +calle +" " +numero +": \n")


			# RASTRILLAJE
			supertags = soup.findAll("div", {"class": "m-results-business-section info"})
			for supertag in supertags:

				# CÓDIGO POSTAL
				taks = supertag('span')
				for tak in taks:
					takStr = str(tak.getText())
					if (takStr.startswith("(CP:")):
						posDosP = takStr.find(':')
						cp4 = takStr[posDosP+1:posDosP+5]
						if cp3 == True:
							try:
								cp4 = int(cp4)
								if cp2 == cp4:
									print('\n\n#######################################################################\n')
									print(takStr)
									q += 1
									contador1 += 1
									#print("Contador:", contador1)
									excC = "C" + str(q)
									ws.write(excC, takStr)

									# DIRECCIONES
									tajs = supertag.findAll("span", {"itemprop": "streetAddress"})
									for taj in tajs:
										tajStr = str(taj.getText().strip())
										sinEspacios = " ".join(tajStr.split())
										print(sinEspacios)
										exc = "A" + str(q)
										ws.write(exc, sinEspacios)

									# TELEFONOS
									tags = supertag('input')
									for tag in tags:
										try:
											tagInt = int(tag.get('value'))
											if (tagInt > 100000):               #evitar otros datos
												tagStr = str(tagInt)
												tagStrG = tagStr[:2] +"-" +tagStr[2:4] +"-" +tagStr[4:8] +"-" + tagStr[8:]
												print(tagStrG)
												excB = "B" + str(q)
												ws.write(excB, tagStrG)
												
												excE = "E" + str(q)
												ws.write(excE, tagStr)
										except:
											aux = i   #esto no hace nada
							except:
								z = 1

						else:
							print('\n\n#######################################################################\n')
							print(takStr)
							q += 1
							contador1 += 1
							excC = "C" + str(q)
							ws.write(excC, takStr)
							#print("Contador:", contador1)

							# DIRECCIONES
							tajs = supertag.findAll("span", {"itemprop": "streetAddress"})
							for taj in tajs:
								tajStr = str(taj.getText().strip())
								sinEspacios = " ".join(tajStr.split())
								print(sinEspacios)
								exc = "A" + str(q)
								ws.write(exc, sinEspacios)

							# TELEFONOS
							tags = supertag('input')
							for tag in tags:
								try:
									tagInt = int(tag.get('value'))
									if (tagInt > 100000):               #evitar otros datos
										tagStr = str(tagInt)
										tagStrG = tagStr[:2] +"-" +tagStr[2:4] +"-" +tagStr[4:8] +"-" + tagStr[8:]
										print(tagStrG)
										excB = "B" + str(q)
										ws.write(excB, tagStrG)
										
										excE = "E" + str(q)
										ws.write(excE, tagStr)
								except:
									aux = i   #esto no hace nada
			
			if contador1/15 == j:
				unoMas = "si"
			else:
				unoMas = "no"
			#print("Contador1:", contador1, "Uno más abajo: " + unoMas)

	##################################################################################################

	wb.close()

	print("\n\n\n#####################            Exportado a archivo Excel con éxito! \n\nSolo para fines educativos. Dudas y problemas a ghp.2120@gmail.com\n\n\n")



root = tk.Tk()
root.config(width=380, height=145)
root.title("MiseriScraping (Argentina)")
frame = tk.Frame(root)
frame.place(x=15, y=15, width=370, height=150)

def verificarLado(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1):
	if pares1 == False and impares1 == False:
		print("Marcar pares o impares o ambos...")
	else:
		scrapear(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1)

def verificarCp(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1):
	if cp1 != "":
		try:
			int(cp1)
			verificarLado(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1)
		except:
			print("Ingrese solo números en CP...")
	else:
		verificarLado(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1)

def verificarMax(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1):
	try:
		int(max1)
		verificarCp(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1)
	except:
		print("Ingrese solo números en MAX...")

def verificarMin(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1):
	try:
		int(min1)
		verificarMax(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1)
	except:
		print("Ingrese solo números en MIN...")

def start():
	calle1        = calleEntry.get()
	min1          = minEntry.get()
	max1          = maxEntry.get()
	jurisdicción1 = jurisdiccionEntry.get()
	cp1           = cpEntry.get()
	pares1        = i.get()
	impares1      = j.get()
	print(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1)
	if calle1 != "" and jurisdicción1 != "" and min1 != "" and max1 != "":
		verificarMin(calle1, min1, max1, jurisdicción1, cp1, pares1, impares1)
	else:
		print("Faltan datos")

calleLabel = tk.Label(frame, text="Calle: ").grid(row=4, column=1)
calleLabel = tk.Label(frame, text="Altura mínima: ").grid(row=5, column=1)
calleLabel = tk.Label(frame, text="Altura máxima: ").grid(row=6, column=1)
calleLabel = tk.Label(frame, text="Jurisdicción ").grid(row=8, column=1)
calleLabel = tk.Label(frame, text="CP (opcional): ").grid(row=10, column=1)

calleEntry = tk.Entry(frame)
calleEntry.grid(row=4, column=2)
minEntry   = tk.Entry(frame)
minEntry.grid(row=5, column=2)
maxEntry   = tk.Entry(frame)
maxEntry.grid(row=6, column=2)

jurisdiccionEntry = tk.Entry(frame)
jurisdiccionEntry.insert(0, "CABA")
jurisdiccionEntry.grid(row=8, column=2)

cpEntry = tk.Entry(frame)
cpEntry.grid(row=10, column=2)

i = tk.BooleanVar()
i.set(True)
paresCh = ttk.Checkbutton(frame, text="pares  ", variable=i, offvalue=False, onvalue=True)
paresCh.place(x=240, y=9)

j = tk.BooleanVar()
j.set(True)
imparesCh = ttk.Checkbutton(frame, text="impares", variable=j, offvalue=False, onvalue=True)
imparesCh.place(x=240, y=32)

button = tk.Button(frame, text="Scrapear!", padx=30, pady=8, command=lambda:start())
button.place(x=230, y=65)

root.mainloop()

