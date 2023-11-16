#Third party imports
from selenium.webdriver.common.by import By

#Proyect imports
from utilities.baseClass import baseClass


class MainPage(baseClass):

    btn_consultas = (By.ID, "domMenu_vertical[1]")
    cuentas_corrientes = (By.XPATH, "//table[@id='cuentas']/tbody/tr") # Corregir
    btn_salir = (By.XPATH, "img[alt='Salir']")
    btn_saldos_movimientos = (By.ID, "domMenu_vertical[1][2]")
    element_saldos = (By.XPATH, "//table[@id='cuentas']/tbody/tr/td/div//div")
    element_cuentas = (By.XPATH, "//table[@id='cuentas']/tbody/tr/td//a")

    def __init__(self, driver):
        self.driver = driver

    def wait_main_page_load(self):
        self.wait_element_presence(MainPage.btn_consultas, 240)

    def get_btn_consultas(self):
        return self.driver.find_element(*MainPage.btn_consultas)

    def get_cuentas_corrientes(self):
        return self.driver.find_elements(*MainPage.cuentas_corrientes)

    def salir(self):
        self.driver.find_element(*MainPage.btn_salir).click()

    def click_saldos_movimientos(self):
        self.wait_to_click(MainPage.btn_saldos_movimientos, 60)

    def get_saldos_elements(self):
        return self.driver.find_elements(*MainPage.element_saldos)

    def get_cuentas_elements(self):
        return self.driver.find_elements(*MainPage.element_cuentas)
