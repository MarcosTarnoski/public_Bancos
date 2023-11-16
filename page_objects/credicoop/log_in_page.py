#Standard library imports

#Third party imports
from selenium.webdriver.common.by import By

#Proyect imports
from utilities.baseClass import baseClass


class LogInPage(baseClass):

    desp_adherente = (By.NAME, "adherent")
    opt_adherente = (By.CSS_SELECTOR, "option[value='0']")
    input_adherente = (By.NAME, "adherentText")
    input_doc = (By.NAME, "nroDoc")
    input_clave = (By.ID, "passwordText")
    boton_ingresar = (By.CLASS_NAME, "button")

    def __init__(self, driver):
        self.driver = driver

    def desplegable_adherente(self):
        self.wait_to_click(LogInPage.desp_adherente, 15)

    def select_adherente(self):
        self.wait_to_click(LogInPage.opt_adherente, 15)

    def enter_adherente(self, adherente):
        self.driver.find_element(*LogInPage.input_adherente).send_keys(adherente)

    def enter_doc(self, doc):
        self.driver.find_element(*LogInPage.input_doc).send_keys(doc)

    def enter_clave(self, clave):
        self.driver.find_element(*LogInPage.input_clave).send_keys(clave)

    def click_input_clave(self):
        self.driver.find_element(*LogInPage.input_clave).click()

    def click_ingresar(self):
        self.driver.find_element(*LogInPage.boton_ingresar).click()
