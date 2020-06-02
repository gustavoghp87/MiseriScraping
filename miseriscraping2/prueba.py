lado = "par"
min = 10
max = 20
print(5%2, 6%2)

for i in range(min, max+1):

	numero = i
	if ((lado == "par") and (numero%2 == 0)):
		pass
	elif (lado == "impar") and (numero%2 == 1):
		pass
	else:
		continue

	numero = str(i)
	print(numero)