from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #(el "as" es para guardar esto en una variable EC, para poder llamarlo mas facil)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
chromeOptions.add_experimental_option("prefs", {"download.default_directory" : "C:\\Users\\Marcos\\Desktop\\python\\Automation\\Proyecto 3 - Bancos"}) #Aca decimos la ruta en la que queremos que guarde archivos que se descarguen
chromeOptions.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe", options=chromeOptions) #Hacemos referencia al
# driver de chrome que vamos a usar en todo el programa.Con la letra "r" estas indicando que lo que sigue es una dirección, sino la
#barra invertida '\' marcaría ERROR. Ademas se agrega la opcion de que no muestre el cartel "software de prueba automatizado"

driver.get("https://bancainternet.bancocredicoop.coop/bcclbe/") #Con el ".get()" al driver le estas diciendo que ingrese a esa url

# LOG IN
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.NAME, "adherent"))).click()
time.sleep(1.5)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/table/tbody/tr/td[1]/table/tbody/tr[2]/td/form/table/tbody/tr[1]/td[2]/select/option[2]"))).click()
time.sleep(1)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.NAME, "adherentText"))).send_keys("277242")
# time.sleep(1)
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.NAME, "nroDoc"))).send_keys("12214379")

# VERIFICAMOS SI HAY ALGUNA VENTANA EMERGENTE. SI LA HAY, LA CERRAMOS
time.sleep(12)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

#ACCES SALDOS Y MOVIMIENTOS
elemento = driver.find_element_by_id("domMenu_vertical[1]")
ActionChains(driver).move_to_element(elemento).perform()
# No funciona el click siempre acá, porque pueden salir ventanas que lo obstruyen. Entonces mejor lo hacemos con javascript.
# ActionChains(driver).move_by_offset(200, 100).perform()
# time.sleep(2)
# ActionChains(driver).click().perform()
driver.execute_script("document.elementFromPoint(200, 100).click()")



# SALDOS
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cuentas']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]/a/img"))).click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[len(driver.window_handles)-1]) #Cambiamos a la última pestaña que se haya abierto
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/center/a[2]"))).click() #Flechita para ir a marzo
time.sleep(2)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/font/table/tbody/tr[2]/td[2]/font/a"))).click() #1ro de Marzo
time.sleep(2)
driver.switch_to.window(driver.window_handles[0]) #Cambiamos a la ventana inicial
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cuentas']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td[3]/a/img"))).click()
driver.switch_to.window(driver.window_handles[len(driver.window_handles)-1]) #Cambiamos a la última pestaña que se haya abierto
time.sleep(2)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/center/a[2]"))).click() #Flechita para ir a marzo
time.sleep(2)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/font/table/tbody/tr[6]/td[4]/font/a"))).click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0]) #Cambiamos a la ventana inicial
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cuentas']/table/tbody/tr/td/table/tbody/tr[3]/td/input[1]"))).click()
time.sleep(1.5)


# MOVIMIENTOS
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tabla']/table[3]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td[1]/select"))).click()
time.sleep(1.5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tabla']/table[3]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td[1]/select/option[2]"))).click()
time.sleep(1.5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tabla']/table[3]/tbody/tr/td/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td[4]/input"))).click()
