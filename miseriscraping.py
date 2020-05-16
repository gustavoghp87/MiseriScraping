
import urllib.request
import time
import xlsxwriter

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


print("######## BUEN DÍA ESTIMADO/A ######## \n ### ESTO ES MISERISCRAPING ### \n\nEl usuario ingresa calle de la ciudad de Buenos Aires y las alturas mínima y máxima para obtener los números telefónicos de cada vivienda en paginasblancas.com.ar. Exporta a excel automáticamente; el archivo se encontrará en la misma carpeta donde esté este programa. Enjoy it.-\n")

calle = input("Calle sin acentos: ").lower().strip()

while (calle.find('ñ') != -1):
	pos = calle.find('ñ')
	calle = calle[0:pos] + 'n' + calle[pos+1:]

while (calle.find(' ') != -1):
	pos = calle.find(' ')
	calle = calle[0:pos] + '-' + calle[pos+1:]


dia = int(time.time())
archivo = calle +"_" + str(dia) + ".xlsx"
wb = xlsxwriter.Workbook(archivo)
ws = wb.add_worksheet()


while True:
	min = input("Altura MINIMA de esa calle: ")
	try:
		minInt = int(min)
		print("Primer número OK")
		break;
	except:
		print("Ingrese un número...")

while True:
	max = input("Altura MAXIMA de esa calle: ")
	try:
		maxInt = int(max)
		print("Segundo número OK")
		break;
	except:
		print("Ingrese un número...")

if (maxInt < minInt):
	print("Invirtiendo extremos...")
	auxiliar = minInt
	minInt = maxInt
	maxInt = auxiliar

cantidad = maxInt - minInt + 1

aceptar = input("\nSe van a rastrillar " +str(cantidad) +" direcciones.\n3 y enter para cambiar de ciudad,\n0 y enter para cancelar,\nENTER PARA CONTINUAR: \n")

if (aceptar == '0'):
	quit()

ciudad = "caba"
if (aceptar == '3'):
	ciudad = input("Ciudad sin acentos: ").lower().strip()
	while (ciudad.find(' ') != -1):
		pos = ciudad.find(' ')
		ciudad = ciudad[0:pos] + '-' + ciudad[pos+1:]


##################################################################################################

q = 2

for i in range(0, cantidad):

	numero = str(minInt + i)

	direccion = 'http://www.paginasblancas.com.ar/direccion/s/' +calle +'-' +numero +'/' +ciudad

	try:
		datos = urllib.request.urlopen(direccion).read().decode()
	except HTTPError as e:
		print(e)
	except URLError:
		print("Servidor caído o problemas de red... Intente de nuevo")

	soup =  BeautifulSoup(datos, "html.parser")
	
	print("\nCalle " +calle +" " +numero +": \n")


	ws.write(0, 0, "DIRECCIONES")
	ws.write(0, 1, "TELÉFONOS")
	ws.write(0, 2, "CIUDAD: " +ciudad.upper())

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
			q += 1
			exc = "A" + str(q)
			ws.write(exc, sinEspacios)

		# TELEFONOS
		tags = supertag('input')
		for tag in tags:
			try:
				tagInt = int(tag.get('value'))
				if (tagInt > 100000):               #evitar otros datos
					tagStr = str(tagInt)
					tagStr = tagStr[:4] +"-" +tagStr[4:8] +"-" + tagStr[8:]
					print(tagStr)
					excB = "B" + str(q)
					ws.write(excB, tagStr)
					
			except:
				aux = i   #esto no hace nada


##################################################################################################


wb.close()

print("#####################    Exportado a archivo Excel con éxito! ")



