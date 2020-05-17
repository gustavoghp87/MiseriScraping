
import urllib.request
import time
import xlsxwriter

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


print("\n\n\n\n            ######## BUEN DÍA ESTIMADO/A! ######## \n                ### ESTO ES MISERISCRAPING ### \n\n\nEl usuario ingresa calle de la ciudad de Buenos Aires -u otras jurisdicciones de Argentina- y las alturas mínima y máxima para obtener los números telefónicos de cada vivienda en paginasblancas.com.ar. Exporta a excel automáticamente; el archivo se encontrará en la misma carpeta donde esté este programa. Enjoy it.-\n")

calle = input("\nCalle: ").lower().strip()

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

aceptar = input("\n-----> Se van a rastrillar " +str(cantidad) +" direcciones.\n\n3 y enter para cambiar de provincia,\n0 y enter para cancelar,\nENTER PARA CONTINUAR: \n")

if (aceptar == '0'):
	quit()

jurisdiccion = "caba"
if (aceptar == '3'):
	jurisdiccion = input("\nProvincia: ").lower().strip()
	while (jurisdiccion.find(' ') != -1):
		pos = jurisdiccion.find(' ')
		jurisdiccion = jurisdiccion[0:pos] + '-' + jurisdiccion[pos+1:]
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


##################################################################################################

q = 2

for i in range(0, cantidad):

	numero = str(minInt + i)

	direccion = 'http://www.paginasblancas.com.ar/direccion/s/' +calle +'-' +numero +'/' +jurisdiccion

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
	ws.write(0, 2, "JURISDICCIÓN: " +jurisdiccion.upper())

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

		# CÓDIGO POSTAL
		taks = supertag('span')
		for tak in taks:
			takStr = str(tak.getText())
			if (takStr.startswith("(CP:")):
				print(takStr)
				excC = "C" + str(q)
				ws.write(excC, takStr)


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



##################################################################################################


wb.close()

print("\n\n\n#####################            Exportado a archivo Excel con éxito! \n\n\n")



