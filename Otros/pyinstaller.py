
CREAR EJECUTABLES PARA WINDOWS
administrador:   pip install pyinstaller
Agregar la carpeta Scripts al PATH de windows:
	C:\Users\ghp21\AppData\Local\Programs\Python\Python38-32\Scripts
reiniciar


pyinstaller app.py
pyinstaller --onefile app.py
pyinstaller --onefile -w app.py    ocultar la consola
