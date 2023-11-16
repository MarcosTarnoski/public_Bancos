# Standard imports
import time

#Third party imports
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.common.exceptions import TimeoutException

#Proyect imports
from utilities.baseClass import baseClass



class ExtractoSeguroPage(baseClass):

    input_start_date = (By.ID, "start")
    input_last_date = (By.XPATH, "/html/body/app-root/app-authenticated-root/app-operator-root/div[1]/div[2]/app-accounts-root/app-accounts-movements/html/form/div/div/div[3]/div/div[2]/input")
    btn_no_movimientos = (By.XPATH, "/html/body/ngb-modal-window/div/div/modal-error/div[2]/h3")
    btn_salir = (By.XPATH, "/html/body/ngb-modal-window/div/div/modal-error/div[1]/div/button")
    btn_movimientos = (By.XPATH, "/html/body/app-root/app-authenticated-root/app-operator-root/div[1]/div[2]/app-accounts-root/div/ul/li[2]/a")
    btn_buscar = (By.XPATH, "/html/body/app-root/app-authenticated-root/app-operator-root/div[1]/div[2]/app-accounts-root/app-accounts-movements/html/form/div/div/div[7]/div/a")
    btn_icono_descarga = (By.XPATH, "/html/body/app-root/app-authenticated-root/app-operator-root/div[1]/div[2]/app-accounts-root/app-accounts-movements/html/app-accounts-movements-last/main/div[2]/div/div/table/thead/tr/th[6]/button")
    btn_descargar = (By.XPATH, "/html/body/app-root/app-authenticated-root/app-operator-root/app-download-component/div")
    btn_salir2 = (By.XPATH, "/html/body/app-root/app-authenticated-root/app-operator-root/div[1]/div[2]/nav/div[3]/div/div[2]/div[2]/div[2]/span/a/i")
    btn_error = (By.XPATH, "/html/body/ngb-modal-window/div/div/modal-error/div[1]/div/button")
    btn_volver = (By.XPATH, "/html/body/app-root/app-error403/div/div/div[1]/button")

    def __init__(self, driver):
        self.driver = driver

    def click_movimientos(self):
        try:
            self.wait_element_presence(ExtractoSeguroPage.btn_movimientos, 100)
        except TimeoutException:
            self.driver.find_element(*ExtractoSeguroPage.btn_error).click()
            self.wait_to_click(ExtractoSeguroPage.btn_volver, 10)
           # self.driver.find_element(*ExtractoSeguroPage.btn_volver).click()

        self.wait_element_presence(ExtractoSeguroPage.btn_movimientos, 120)
        self.driver.find_element(*ExtractoSeguroPage.btn_movimientos).click()

    def select_start_date(self, start_date):
        self.wait_element_presence(ExtractoSeguroPage.input_start_date, 120)
        self.driver.find_element(*ExtractoSeguroPage.input_start_date).send_keys(Keys.SHIFT, Keys.ARROW_UP)
        self.driver.find_element(*ExtractoSeguroPage.input_start_date).send_keys(Keys.DELETE)
        self.driver.find_element(*ExtractoSeguroPage.input_start_date).send_keys(start_date)

    def select_last_date(self, last_date):
        self.wait_element_presence(ExtractoSeguroPage.input_last_date, 120)
        self.driver.find_element(*ExtractoSeguroPage.input_last_date).send_keys(Keys.SHIFT, Keys.ARROW_UP)
        self.driver.find_element(*ExtractoSeguroPage.input_last_date).send_keys(Keys.DELETE)
        self.driver.find_element(*ExtractoSeguroPage.input_last_date).send_keys(last_date)

    def click_ir(self):
        self.driver.find_element(*ExtractoSeguroPage.btn_buscar).click()

    def check_movimientos_presence(self):
        self.wait_element_presence(ExtractoSeguroPage.btn_no_movimientos, 80)
        self.driver.find_element(*ExtractoSeguroPage.btn_no_movimientos)

    def click_exportar(self):

        self.wait_element_presence(ExtractoSeguroPage.btn_icono_descarga, 120)
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*ExtractoSeguroPage.btn_icono_descarga))
        self.wait_element_presence(ExtractoSeguroPage.btn_descargar, 240)
        self.driver.find_element(*ExtractoSeguroPage.btn_descargar).click()



    def click_salir(self):
        try:
            self.driver.find_element(*ExtractoSeguroPage.btn_salir).click()
        except:
            self.driver.find_element(*ExtractoSeguroPage.btn_salir2).click()
