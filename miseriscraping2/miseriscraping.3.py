import os
import urllib.request
import time
import xlsxwriter

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

import pymongo
import pandas as pd

################################################################################################################################

data = pd.read_excel('Territorios.xlsx', encoding='UTF8')


print("\n\n\n\n            ######## BUEN DÍA ESTIMADO/A! ######## \n               ### ESTO ES MISERISCRAPING 2 ### \n\n\nEl usuario ingresa número de territorio (Argentina) para obtener los números telefónicos de cada vivienda en paginasblancas.com.ar. Exporta a excel automáticamente; el archivo se encontrará en la misma carpeta donde esté este programa. Enjoy it.-\n")

jurisdiccion = "caba"
fila = 1
fila2 = 1


#######################################################################################################################

def depurar_calle(calle):
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

	return calle


########################################################################################################


#########################################################################################################################################


############ CARGA DE DATOS DE TERRITORIOS.XLSX

for r in range(10, 57):


	terri_elegido = str(r)
	try:
		terri_elegido = int(terri_elegido)
	except:
		print("Sólo números...")
		quit()

	if terri_elegido < 10:
		terri_elegido = str(terri_elegido)
		archivo = "territorio-0" + terri_elegido + ".xlsx"
	else:
		terri_elegido = str(terri_elegido)
		archivo = "territorio-" + terri_elegido + ".xlsx"
	wb = xlsxwriter.Workbook(archivo)
	ws = wb.add_worksheet()
	ws.write(0, 0, "territorio")
	ws.write(0, 1, "manzana")
	ws.write(0, 2, "dirección")
	ws.write(0, 3, "teléfono-")
	ws.write(0, 4, "telefono")
	ws.write(0, 5, "cp")
	ws.write(0, 6, "observaciones")
	ws.write(0, 10, "buscados")
	ws.write(0, 11, "control")

	print("fila al iniciar: " +str(fila))
	for i in data.index:
		id_calle   = str(data['id_calle'][i])
		territorio = str(data['territorio'][i])
		manzana    = str(data['manzana'][i])
		calle      = str(data['calle'][i])
		min        = str(data['min'][i])
		max        = str(data['max'][i])
		lado       = str(data['lado'][i])


		print("id_calle: " +id_calle + "\nterritorio: " + territorio + "\nmanzana: " +manzana + "\ncalle: " +calle + "\nmin: " +min + "\nmax: " + max + "\nlado: " + lado )

		print("fila al iniciar fila de territorio afirmativa: " +str(fila))
		if territorio == terri_elegido:
			calle = calle.lower().strip()
			calle = depurar_calle(calle)
			print(calle)

			fila2 += 1
			print("\nTerritorio: " +territorio + ", manzana: " + manzana + ", calle.dep: " + calle + ", min: " +min + ", max: " + max)
			excK = "K" + str(fila2)
			ws.write(excK, "Territorio: " +territorio + ", manzana: " + manzana + ", calle.dep: " + calle + ", min: " +min + ", max: " + max)

			min = int(float(min))
			max = int(float(max))

			print("fila al iniciar scraping: " +str(fila))

			for i in range(min, max+1):
				numero = i
				if ((lado == "par") and (numero%2 == 0)):
					pass
				elif (lado == "impar") and (numero%2 == 1):
					pass
				else:
					continue
				numero = str(i)
				print("fila al iniciar número: " +str(fila))

				direccion = 'http://www.paginasblancas.com.ar/direccion/s/' +calle +'-' +numero +'/' +jurisdiccion
				print("Dirección: " +direccion)

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

					print('\n\n#######################################################################\n')

					# DIRECCIONES
					tajs = supertag.findAll("span", {"itemprop": "streetAddress"})
					for taj in tajs:
						tajStr = str(taj.getText().strip())
						sinEspacios = " ".join(tajStr.split())
						print(sinEspacios)
						fila += 1
						print("fila al sumar 1: " +str(fila))
						excC = "C" + str(fila)
						ws.write(excC, sinEspacios)
						mensaje = "encontré al menos un teléfono en esta cuadra"
						excL = "L" + str(fila2)
						ws.write(excL, mensaje)

					# CÓDIGO POSTAL
					taks = supertag('span')
					for tak in taks:
						takStr = str(tak.getText())
						if (takStr.startswith("(CP:")):
							print(takStr)
							excF = "F" + str(fila)
							ws.write(excF, takStr)


					# TELEFONOS
					tags = supertag('input')
					for tag in tags:
						try:
							tagInt = int(tag.get('value'))
							if (tagInt > 100000):               #evitar otros datos
								tagStr = str(tagInt)
								tagStrG = tagStr[:2] +"-" +tagStr[2:4] +"-" +tagStr[4:8] +"-" + tagStr[8:]
								print(tagStrG)
								excD = "D" + str(fila)
								ws.write(excD, tagStrG)
					
								excE = "E" + str(fila)
								ws.write(excE, tagStr)
								excA = "A" + str(fila)
								ws.write(excA, territorio)
								excB = "B" + str(fila)
								ws.write(excB, manzana)

					
						except:
							aux = i   #esto no hace nada
			print("fila al terminar número afirmativo: " +str(fila))




##################################################################################################


#########################################################################################################################################


	# YENDO A GOOGLE
#	print("Yendo a Google")
#	google = "https://www.google.com/search?q=" + calle + "-" + numero + "-" + jurisdiccion
#	print(google)
#	try:
#		datos2 = urllib.request.urlopen(google).read().decode()
#	except HTTPError as e:
#		print(e, "no encontrado")
#	except URLError:
#		print("Servidor caído o problemas de red... Intente de nuevo")

#	soup2 =  BeautifulSoup(datos2, "html.parser")
	
#	print("\nGoogle | Calle " +calle +" " +numero +": \n")

#	ws.write(0, 7, "LATITUD")
#	ws.write(0, 8, "LONGITUD")

#	superts = soup.findAll("a")
#	for supert in superts:
#		href = supert('href')
#		print("\nhref=" + href)

# href="/maps




##################################################################################################


	wb.close()

	territorio = str(territorio)
	print("\n\n\n#####################        Territorio " + terri_elegido +  " exportado a archivo Excel con éxito! \n\n\n")



