import os
import xlsxwriter
import pandas as pd

################################################################################################################################

data = pd.read_excel("te.xlsx", encoding='UTF8')

wb = xlsxwriter.Workbook("nuevo.xlsx")
ws = wb.add_worksheet()
ws.write(0, 0, "inner_id")
ws.write(0, 1, "calle_id")
ws.write(0, 2, "territorio")
ws.write(0, 3, "manzana")
ws.write(0, 4, "dirección")
ws.write(0, 5, "calle")
ws.write(0, 6, "altura")
ws.write(0, 7, "piso/depto")
ws.write(0, 8, "depto")
ws.write(0, 9, "depto+")
ws.write(0, 13, "teléfono")
ws.write(0, 14, "estado")

for i in data.index:
	inner_id = data['inner_id'][i]
	cuadra_id    = data['cuadra_id'][i]
	territorio  = data['territorio'][i]
	manzana  = data['manzana'][i]
	direccion  = data['dirección'][i]
	telefono = data['teléfono'][i]
	estado = data['estado'][i]

	excA = "A" + str(i+2)
	ws.write(excA, inner_id)
	excB = "B" + str(i+2)
	ws.write(excB, cuadra_id)
	excC = "C" + str(i+2)
	ws.write(excC, territorio)
	excD = "D" + str(i+2)
	ws.write(excD, manzana)
	excE = "E" + str(i+2)
	ws.write(excE, direccion)

	excF = "F" + str(i+2)
	excG = "G" + str(i+2)
	excH = "H" + str(i+2)
	excI = "I" + str(i+2)
	excJ = "J" + str(i+2)

	lista = direccion.split(' ')
	if (lista[1].isdigit()):
		ws.write(excF, lista[0])
		ws.write(excG, lista[1])
		try:
			ws.write(excH, lista[2])
		except:
			z = 1
		try:
			ws.write(excI, lista[3])
		except:
			z = 1
		try:
			ws.write(excF, lista[4])
		except:
			z = 1
	elif (lista[2].isdigit()):
		calle = lista[0] + " " + lista[1]
		ws.write(excF, calle)
		ws.write(excG, lista[2])
		try:
			ws.write(excH, lista[3])
		except:
			z = 1
		try:
			ws.write(excI, lista[4])
		except:
			z = 1
		try:
			ws.write(excF, lista[5])
		except:
			z = 1
	elif (lista[3].isdigit()):
		calle = lista[0] + " " + lista[1] + " " + lista[2]
		ws.write(excF, calle)
		ws.write(excG, lista[3])
		try:
			ws.write(excH, lista[4])
		except:
			z = 1
		try:
			ws.write(excI, lista[5])
		except:
			z = 1
		try:
			ws.write(excF, lista[6])
		except:
			z = 1
	elif (lista[4].isdigit()):
		calle = lista[0] + " " + lista[1] + " " + lista[2] + " " + lista[3]
		ws.write(excF, calle)
		ws.write(excG, lista[4])
		try:
			ws.write(excH, lista[5])
		except:
			z = 1
		try:
			ws.write(excI, lista[6])
		except:
			z = 1
		try:
			ws.write(excF, lista[7])
		except:
			z = 1

	excN = "N" + str(i+2)
	ws.write(excN, telefono)
	excO = "O" + str(i+2)
	ws.write(excO, estado)



wb.close()

print("\n\n\n#####################        Terminado con éxito! \n\n\n")
