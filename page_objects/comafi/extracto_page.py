# Standard imports
import time
#Third party imports
from selenium.webdriver.common.by import By
#Proyect imports
from utilities.baseClass import baseClass

class ExtractoPage(baseClass):

    input_start_date = (By.NAME, "fechaDesde")
    input_last_date = (By.NAME, "fechaHasta")
    frame_header = (By.NAME,"header")
    frame_body = (By.NAME,"body")
    frame_main = (By.NAME, "mainLayout")
    frame_main_2 = (By.NAME, "mainLayoutBody")
    btn_ir = (By.CSS_SELECTOR, "td[class='texto_Gris10 aliniacionCriterioBoton1']")
    text_no_movimientos = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[2]/td[contains(text(), 'No hay movimientos a visualizar')]")
    btn_exportar = (By.CSS_SELECTOR, "img[src='/ebank2/jsp/resources/img/botExportar.gif']")
    btn_salir = (By.CSS_SELECTOR, "img[src='/ebank2/jsp/resources/img/btnSalir.gif']")

    def __init__(self, driver):
        self.driver = driver
    def select_start_date(self, start_date):
        # self.wait_to_click(ExtractoPage.input_last_date, 10)
        # self.wait_frame_presence(ExtractoPage.frame_body, 20) # No es necesario porque vamos al parent frame en la función "go to extracto"
        self.wait_frame_presence(ExtractoPage.frame_main, 240)
        self.wait_frame_presence(ExtractoPage.frame_main_2, 60)
        # Ya en el frame correspondiente, procedemos a asignarle el valor al input
        # Para esto modificamos el valor del atributo "value"
        self.wait_element_presence(ExtractoPage.input_start_date, 240)
        element_input_start_date = self.driver.find_element(*ExtractoPage.input_start_date)
        self.driver.execute_script(f"arguments[0].setAttribute('value','{start_date}')", element_input_start_date)
    def select_last_date(self, last_date):
        # self.wait_to_click(ExtractoPage.input_last_date, 10)
        # Ya en el frame correspondiente, procedemos a asignarle el valor al input
        # Para esto modificamos el valor del atributo "value"
        element_input_last_date = self.driver.find_element(*ExtractoPage.input_last_date)
        self.driver.execute_script(f"arguments[0].setAttribute('value','{last_date}')", element_input_last_date)
    def click_ir(self):
        self.driver.find_element(*ExtractoPage.btn_ir).click()
    def check_movimientos_presence(self):
        # Por algun motivo tengo que "reiniciar" la referencia a los iframes. Aunque
        # entiendo que deberia seguir en el frame_main_2 despues de la funcion "select_last_date"
        # pero por algun motivo si no hago lo de abajo para volver ubicarme en ese no puede
        # encontrar al boton
        self.driver.switch_to.default_content()
        self.wait_frame_presence(ExtractoPage.frame_body, 240)
        self.wait_frame_presence(ExtractoPage.frame_main, 20)
        self.wait_frame_presence(ExtractoPage.frame_main_2, 20)
        self.wait_element_presence(ExtractoPage.text_no_movimientos, 5)
        self.driver.switch_to.default_content()

    def click_exportar(self):
        self.wait_to_click(ExtractoPage.btn_exportar, 240)
        self.driver.switch_to.default_content()

    def click_salir(self):
        self.driver.switch_to.default_content()
        self.wait_frame_presence(ExtractoPage.frame_header, 20)
        self.driver.find_element(*ExtractoPage.btn_salir).click()

