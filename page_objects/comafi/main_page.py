#Third party imports
from selenium.webdriver.common.by import By

#Proyect imports
from utilities.baseClass import baseClass


class MainPage(baseClass):

    frame_body = (By.NAME,"body")
    frame_main = (By.NAME, "mainLayout")
    frame_main_2 = (By.NAME, "mainLayoutBody")
    frame_cuentas_menu = (By.ID,"frame10")
    frame_header = (By.NAME,"header")
    btn_consultas = (By.XPATH, "/html/body/table/tbody/tr[1]/td/div/div[1]/table/tbody/tr/td[2]")
    btn_cuentas = (By.ID, "base1Consultas10Cuentas")
    btn_extracto = (By.CSS_SELECTOR, "a[href='/ebank2/extracto.do?accion=executeMenuCuentas&tipoOpeNombreDiv=1Consultas&separadorName=separador1']")
    text_saldo = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]")
    btn_ingresar = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[10]/td[2]/a/img")

    def __init__(self, driver):
        self.driver = driver

    def consultas(self):
        # self.driver.switch_to.frame("body") # No uso esta instrucción porque no llega a cargar el DOM y tira error
        self.driver.switch_to.default_content()
        self.wait_frame_presence(MainPage.frame_body, 240)
        self.wait_to_click(MainPage.btn_consultas, 60)

    def cuentas(self):
        self.wait_to_click(MainPage.btn_cuentas, 60)

    def ingresar(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("body");
        self.driver.switch_to.frame("mainLayout");
        self.driver.switch_to.frame("mainLayoutBody");
        self.wait_to_click(MainPage.btn_ingresar, 60)

    def go_to_extracto(self):
        self.driver.switch_to.default_content()
        # self.driver.switch_to.frame("frame10")
        self.wait_frame_presence(MainPage.frame_body, 240)
        self.wait_frame_presence(MainPage.frame_cuentas_menu, 60)
        self.wait_to_click(MainPage.btn_extracto, 60)
        # self.driver.switch_to.default_content()
        self.driver.switch_to.parent_frame()


    def get_saldo(self):
        self.driver.switch_to.default_content()
        self.wait_frame_presence(MainPage.frame_body, 240)
        self.wait_frame_presence(MainPage.frame_main, 20)
        self.wait_frame_presence(MainPage.frame_main_2, 20)
        return self.driver.find_element(*MainPage.text_saldo)

    def es_seguro(self):
        self.driver.switch_to.default_content()
        self.wait_frame_presence(MainPage.frame_body, 240)
        self.wait_frame_presence(MainPage.frame_main, 20)
        self.wait_frame_presence(MainPage.frame_main_2, 20)
        self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[10]/td[2]/a/img")
        self.driver.switch_to.default_content()
