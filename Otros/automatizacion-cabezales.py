import os
import xlsxwriter
import pandas as pd

################################################################################################################################

for i in range(1, 57):
	if i < 10:
		i = str(i)
		archivo = "territorio-0" + i + ".xlsx"
		data = pd.read_excel(archivo, encoding='UTF8')
	else:
		i = str(i)
		archivo = "territorio-" + i + ".xlsx"
		data = pd.read_excel(archivo, encoding='UTF8')

	wb = xlsxwriter.Workbook(archivo)
	ws = wb.add_worksheet()
	ws.write(0, 0, "territorio")
	ws.write(0, 1, "manzana")
	ws.write(0, 2, "dirección")
	ws.write(0, 3, "teléfono")
	ws.write(0, 4, "no abonado en serv")
	ws.write(0, 5, "contesta")
	ws.write(0, 6, "no contesta")
	ws.write(0, 7, "revisita")
	ws.write(0, 8, "cartas")
	ws.write(0, 9, "observaciones")


	for i in data.index:
		territorio = data['territorio'][i]
		manzana    = data['manzana'][i]
		dirección  = data['dirección'][i]
		teléfono  = data['teléfono-'][i]

		excA = "A" + str(i+2)
		ws.write(excA, territorio)
		excB = "B" + str(i+2)
		ws.write(excB, manzana)
		excC = "C" + str(i+2)
		ws.write(excC, dirección)
		excD = "D" + str(i+2)
		ws.write(excD, teléfono)

	wb.close()

print("\n\n\n#####################        Terminado con éxito! \n\n\n")
