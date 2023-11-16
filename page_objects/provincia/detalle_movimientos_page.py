#Standard library imports

#Third party imports
from selenium.webdriver.common.by import By

#Proyect imports
from utilities.baseClass import baseClass


class DetalleMovimientosPage(baseClass):
    selector = (By.ID, "cuenta")
    opciones = (By.XPATH, "//select[@id='cuenta']//option")
    boton_buscar = (By.ID, "rightAlignButton")
    boton_excel = (By.XPATH, '//*[@id="table_1"]/thead/tr[1]/td/table/tbody/tr/td[2]/a/img')
    fecha_desde = (By.ID, "fechaDesde")
    fecha_hasta = (By.ID, "fechaHasta")
    boton_volver = (By.CLASS_NAME, "botonSubmitVolver")

    def __init__(self, driver):
        self.driver = driver

    def elegir_cuenta(self):
        self.driver.find_element(*DetalleMovimientosPage.selector).click()

    def click_buscar(self):
        self.driver.find_element(*DetalleMovimientosPage.boton_buscar).click()

    def get_cuentas_elements(self):
        return self.driver.find_elements(*DetalleMovimientosPage.opciones)

    def opcion_select(self, opcion):
        opcion.click()

    def click_excel(self):
        self.driver.find_element(*DetalleMovimientosPage.boton_excel).click()

    def set_fecha_inicial(self, fecha_inicio):
        self.driver.execute_script("document.getElementById('fechaDesde').value = arguments[0];", fecha_inicio)

    def set_fecha_final(self,fecha_final):
        self.driver.execute_script("document.getElementById('fechaHasta').value = arguments[0];", fecha_final)

    def volver(self):
        self.driver.find_element(*DetalleMovimientosPage.boton_volver).click()
