# MiseriScraping

App de terminal y ejecutable para Windows en Python para hacer web scraping sobre el sitio de Páginas Blancas de Argentina.

Descargar gran cantidad de números telefónicos y sus respectivas direcciones, exportando automáticamente a archivo Excel (.xlsx).

Se introduce la calle, la altura mínima de barrido y la altura máxima, opcionalmente se cambia de ciudad (CABA por default) y pares/impares.

Luego se esperan los resultados.

Barre cerca de 100 direcciones por minuto.

Respecto a las jurisdicciones, partidos y localidades, se depende de la base de datos de Páginas Blancas y hay que ir probando diferentes maneras. Por ejemplo, en la base de datos no figura "san isidro" sino "buenos aires" pero sí toma "tandil". El programa exporta los códigos postales para evitar problemas.

Lo mismo decimos para el nombre específico de las calles. Por ejemplo, Páginas Blancas toma "j m moreno" y no "jose maria moreno". Hay que ir probando.

Librerías para versión de terminal: requiere beautifulsoup y xlsxwriter (se puede activar el entorno virtual y listo, "venv\Scripts\activate")

Video: https://www.youtube.com/embed/AJW4_3rtcoE

--------------------------------------------------------------------------------------------------------------------------------

MiseriScraping is a web scraping app wroten in Python to seek and download telephone numbers with addresses.

Require:
pip3 install bs4
pip3 install XlsxWriter


--------------------------------------------------------------------------------------------------------------------------------

