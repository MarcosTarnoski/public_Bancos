#Standard library imports

#Third party imports
from selenium.webdriver.common.by import By

#Proyect imports
from utilities.baseClass import baseClass


class MovimientosPage(baseClass):
    boton_movimientos = (By.XPATH, '//*[@id="table_1_row1"]/td[7]/a/img')
    text_saldo = (By.CLASS_NAME, "textImporte")
    boton_salir = (By.XPATH, "/html/body/div[5]/div[1]/div[1]/div[1]/div[2]/div[3]/a[1]")

    def __init__(self, driver):
        self.driver = driver

    def click_movimientos(self):
        self.driver.find_element(*MovimientosPage.boton_movimientos).click()

    def get_saldo(self):
        return self.driver.find_elements(*MovimientosPage.text_saldo)

    def salir(self):
        self.driver.find_element(*MovimientosPage.boton_salir).click()
