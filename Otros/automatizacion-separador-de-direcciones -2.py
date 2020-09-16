import os
import xlsxwriter
import pandas as pd

################################################################################################################################

data = pd.read_excel("te.xlsx", encoding='UTF8')

wb = xlsxwriter.Workbook("nuevo2.xlsx")
ws = wb.add_worksheet()
ws.write(0, 0, "inner_id")
ws.write(0, 1, "calle_id")
ws.write(0, 2, "territorio")
ws.write(0, 3, "manzana")
ws.write(0, 4, "dirección")
ws.write(0, 5, "dire-alt")
ws.write(0, 6, "piso/depto")
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

	print("DIRECCION: " + direccion)
	lista = direccion.split(' ')
	if (lista[1].isdigit()):
		direccion2 = lista[0] + " " + lista[1]
		ws.write(excF, direccion2)
		try:
			pisodepto = lista[2] + " " + lista[3] + " " + lista[4]
		except:
			try:
				pisodepto = lista[2] + " " + lista[3]
			except:
				try:
					pisodepto = lista[2]
				except:
					pisodepto = ""
		ws.write(excG, pisodepto)
	elif (lista[2].isdigit()):
		direccion2 = lista[0] + " " + lista[1] + " " + lista[2]
		ws.write(excF, direccion2)
		try:
			pisodepto = lista[3] + " " + lista[4] + " " + lista[5]
		except:
			try:
				pisodepto = lista[3] + " " + lista[4]
			except:
				try:
					pisodepto = lista[3]
				except:
					pisodepto = ""
		ws.write(excG, pisodepto)
	elif (lista[3].isdigit()):
		direccion2 = lista[0]  + " " + lista[1] + " " + lista[2] + " " + lista[3]
		ws.write(excF, direccion2)
		try:
			pisodepto = lista[4] + " " + lista[5] + " " + lista[6]
		except:
			try:
				pisodepto = lista[4] + " " + lista[5]
			except:
				try:
					pisodepto = lista[4]
				except:
					pisodepto = ""
		ws.write(excG, pisodepto)
	elif (lista[4].isdigit()):
		direccion2 = lista[0]  + " " + lista[1] + " " + lista[2] + " " + lista[3] + " " + lista[4]
		ws.write(excF, direccion2)
		try:
			pisodepto = lista[5] + " " + lista[6] + " " + lista[7]
		except:
			try:
				pisodepto = lista[5] + " " + lista[6]
			except:
				try:
					pisodepto = lista[5]
				except:
					pisodepto = ""
		ws.write(excG, pisodepto)

	excN = "N" + str(i+2)
	ws.write(excN, telefono)
	excO = "O" + str(i+2)
	ws.write(excO, estado)



wb.close()

print("\n\n\n#####################        Terminado con éxito! \n\n\n")
