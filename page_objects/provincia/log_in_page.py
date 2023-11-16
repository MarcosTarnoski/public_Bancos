#Standard library imports

#Third party imports
from selenium.webdriver.common.by import By

#Proyect imports
from utilities.baseClass import baseClass


class LogInPage(baseClass):

    username = (By.ID, "username")
    boton_user = (By.ID, "imageSubmit")
    password = (By.ID, "password")
    boton_pass = (By.ID, "imageSubmitPass")
    boton_nuevo = (By.XPATH, "//*[@id='loginForm']/div[4]/button[2]")

    def __init__(self, driver):
        self.driver = driver

    def enter_usuario(self, usuario):
        self.driver.find_element(*LogInPage.username).send_keys(usuario)

    def click_usuario(self):
        self.wait_to_click(LogInPage.boton_user, 15)

    def enter_clave(self, clave):
        self.driver.find_element(*LogInPage.password).send_keys(clave)

    def version_vieja(self):
        self.driver.find_element(*LogInPage.boton_nuevo).click()

    def click_input_clave(self):
        self.driver.find_element(*LogInPage.boton_pass).click()
    #
    # def click_ingresar(self):
    #     self.driver.find_element(*LogInPage.boton_ingresar).click()
