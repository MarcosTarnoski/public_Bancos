#Standard library imports

#Third party imports
from selenium.webdriver.common.by import By

#Proyect imports
from utilities.baseClass import baseClass


class PerfilPage(baseClass):

    opcion = (By.XPATH, '//input[@name="tipoPerfil" and @value="2"]')
    boton_aceptar = (By.ID, "rightAlignButton")

    def __init__(self, driver):
        self.driver = driver

    def elegir_perfil(self):
        self.driver.find_element(*PerfilPage.opcion).click()

    def click_aceptar(self):
        self.driver.find_element(*PerfilPage.boton_aceptar).click()
