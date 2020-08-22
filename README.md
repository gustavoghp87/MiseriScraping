# MiseriScraping
App de terminal en Python para hacer web scraping sobre el sitio de Páginas Blancas de Argentina y poder descargar gran cantidad de números telefónicos y sus respectivas direcciones, exportando automáticamente a archivo Excel (.xlsx). Se introduce la calle, la altura mínima de barrido y la altura máxima, opcionalmente se cambia de ciudad (CABA por default). Luego se esperan los resultados.

Barre cerca de 100 direcciones por minuto.

Respecto a las jurisdicciones, partidos y localidades, se depende de la base de datos de Páginas Blancas y hay que ir probando diferentes maneras. Por ejemplo, en la base de datos no figura "san isidro" sino "buenos aires" pero sí toma "tandil". El programa exporta los códigos postales para evitar problemas.

Lo mismo decimos para el nombre específico de las calles. Por ejemplo, Páginas Blancas toma "j m moreno" y no "jose maria moreno". Hay que ir probando.

Librerías: requiere beautifulsoup y xlsxwriter

<video src="https://www.youtube.com/embed/AJW4_3rtcoE" width="320" height="200" controls preload></video>
<iframe width="560" height="315" src="https://www.youtube.com/embed/AJW4_3rtcoE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

############################################################################################################################################

MiseriScraping is a web scraping app wroten in Python to seek and download telephone numbers with addresses.

Require:
pip3 install bs4
pip3 install XlsxWriter


############################################################################################################################################

Instrucciones para Windows:
1) Descargar python 3 desde https://www.python.org/downloads/release/python-383/
   Es el archivo Windows x86-64 executable installer
   Opcionalmente ver si hay alguna versión superior
2) En la ventana de diálogo de instalación del programa tildar la opción "Agregar Python al Path / Add Python 3.8 to Path"
3) Instalar
4) Buscar y abrir "cmd" en la lupa de Windows
   Opción 2: click derecho en el logo de windows y abrir Windows PowerShell
   Opción 3: abrir C://Windows/system32/cmd
5) Tipear: python -m pip install -U pip    y dar enter
   Tiper:  pip install bs4                 y dar enter
   Tiper:  pip install xlsxwriter          y dar enter
   Si ninguna de estas cosas funciona, reiniciar pc y volver a intentar
6) Poner miseriscraping.py en una carpeta exclusiva
7) Presionando Shift hacer click derecho en alguna parte vacía de la carpeta y seleccionar "Abrir la ventana de PowerShell aquí"
   Esto es solo para Windows 10. Para versiones anteriores, hay que abrir "cmd" como en el punto 4) y navegar hasta MiseriScraping
8) Tipear: python3 .\miseriscraping.py     y dar enter
9) El programa puede ser interrumpido en cualquier momento con control+c


