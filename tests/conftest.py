# Standard library imports

# Third party imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Proyect imports
from data.directory import DIRECTORY

def setup():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    prefs = {"download.default_directory":f"{DIRECTORY}\\paperworks"}
    chromeOptions.add_experimental_option("prefs", prefs) #Aca decimos la ruta en la que queremos que guarde archivos que se descarguen
    chromeOptions.add_argument("--start-maximized")
    # chromeOptions.add_argument("--user-data-dir=chrome-data")
    chromeOptions.add_argument('--disable-gpu') # Para que no salten esos errores raros
    service = Service(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chromeOptions) #Hacemos referencia al
    # driver de chrome que vamos a usar en todo el programa.Con la letra "r" estas indicando que lo que sigue es una dirección, sino la
    # barra invertida '\' marcaría ERROR. Ademas se agrega la opcion de que no muestre el cartel "software de prueba automatizado"
    return driver