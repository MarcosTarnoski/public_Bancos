#Standard library imports

#Third party imports
from selenium.webdriver.common.by import By

#Proyect imports
from utilities.baseClass import baseClass


class LogInPage(baseClass):

    input_user = (By.ID, "input-user")
    input_access = (By.ID, "input-clave")
    input_ident = (By.ID, "input-nickname")
    boton_ingresar = (By.XPATH, "/html/body/form/div/div[2]/a[1]")
    def __init__(self, driver):
        self.driver = driver

    def wait_loginpage_load(self):
        self.wait_element_presence(LogInPage.input_user, 240) #240

    def enter_user(self, user):
        self.driver.find_element(*LogInPage.input_user).send_keys(user)

    def click_acces_key(self):
        self.driver.find_element(*LogInPage.input_access).click()

    def enter_acceso(self, acceso):
        self.driver.find_element(*LogInPage.input_access).send_keys(acceso)

    def click_ident_key(self):
        self.driver.find_element(*LogInPage.input_ident).click()

    def enter_ident(self, ident):
        self.driver.find_element(*LogInPage.input_ident).send_keys(ident)

    def click_ingresar(self):
        self.driver.find_element(*LogInPage.boton_ingresar).click()
