# Standard library imports

#Third party imports
from selenium.webdriver.common.by import By

#Proyect imports
from utilities.baseClass import baseClass

class MovimientosPage(baseClass):

    desp_format = (By.NAME, "output")
    select_format = (By.CSS_SELECTOR, "option[value='xls']")
    btn_export = (By.CSS_SELECTOR, "input[value='Exportar']")
    btn_log_out = (By.CSS_SELECTOR, "img[alt='Salir']")
    text_log_out = (By.XPATH, "/html/body/table/tbody/tr[2]/td[1]/table/tbody/tr[3]/td/table/tbody/tr[1]/td")
    text_no_movements = (By.XPATH, "//*[@id='tabla']/table[1]/tbody/tr/td/span")
    btn_volver = (By.CSS_SELECTOR, "input[value='Volver']")

    def __init__(self, driver):
        self.driver = driver

    def desplegable_export_format(self):
        self.wait_to_click(MovimientosPage.desp_format, 20)

    def select_excel_format(self):
        self.wait_to_click(MovimientosPage.select_format, 20)

    def export_movimientos(self):
        self.driver.find_element(*MovimientosPage.btn_export).click()

    def log_out(self):
        self.driver.find_element(*MovimientosPage.btn_log_out).click()

    def wait_logout_text(self):
        self.wait_element_presence(MovimientosPage.text_log_out, 10)

    def check_movimientos_presence(self):
        self.wait_element_presence(MovimientosPage.text_no_movements, 5)

    def back_to_saldos_page(self):
        self.driver.find_element(*MovimientosPage.btn_volver).click()
