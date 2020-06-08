import urllib.request
import time
import xlsxwriter

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


print("\n\n\n\n            ######## BUEN DÍA ESTIMADO/A! ######## \n                ### ESTO ES MISERISCRAPING ### \n\n\nEl usuario ingresa calle de Argentina y las alturas mínima y máxima para obtener los números telefónicos de cada vivienda en paginasblancas.com.ar. Exporta a excel automáticamente; el archivo se encontrará en la misma carpeta donde esté este programa. Enjoy it.-\n")

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

while (calle.find('ü') != -1):
	pos = calle.find('ü')
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

lados = input("\n\n-----> Se van a rastrillar " +str(cantidad) +" direcciones. ENTER para continuar o\n1 y enter para buscar solo pares\n2 y enter para buscar solo impares\n")

if lados == "1":
	print("Se buscarán solo pares\n")
elif lados == "2":
	print("Se buscarán solo impares\n")
else:
	lados == 0
	print("Se buscarán pares e impares\n")

aceptar = input("ENTER para buscar en Ciudad de Buenos Aires\n3 y enter para cambiar de jurisdicción\n0 y enter para salir\n")

if (aceptar == '0'):
	quit()

jurisdiccion = "caba"
if (aceptar == '3'):
	jurisdiccion = input("\nProvincia o localidad (ir probando): ").lower().strip()

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
		

filtrar = input("\nFiltrar también por código postal? Introdúzcalo y enter, o solo ENTER: ")

try:
	filtrar = int(filtrar)
	filtrar = str(filtrar)
except:
	filtrar = "no"

if filtrar == "no":
	print("\n\nCOMENZANDO ... calle " + calle + " alturas " +min + "-" +max + " en " +jurisdiccion)
else:
	print("\n\nCOMENZANDO ... calle " + calle + " alturas " +min + "-" +max + " en " +jurisdiccion + " CP " +filtrar)

time.sleep(2)

##################################################################################################

ws.write(0, 0, "DIRECCIONES")
ws.set_column('A:A', 30)
ws.write(0, 1, "TELÉFONOS")
ws.set_column('B:B', 16)
ws.write(0, 2, "JURISDICCIÓN: " +jurisdiccion.upper())
ws.set_column('C:C', 25)
ws.set_column('E:E', 14)

q = 2

for i in range(0, cantidad):

	numero = str(minInt + i)

	if lados == "0":
		pass
	elif lados == "1" and int(numero)%2 == 0:
		pass
	elif lados == "2" and int(numero)%2 == 1:
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
					if filtrar != "no":
						try:
							cp4 = int(cp4)
							filtrar = int(filtrar)
							if filtrar == cp4:
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

print("\n\n\n#####################            Exportado a archivo Excel con éxito! \n\n\nSolo para fines educativos. Dudas y problemas a ghp.2120@gmail.com\n\n\n")



