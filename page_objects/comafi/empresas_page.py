#Third party imports
from selenium.webdriver.common.by import By

#Proyect imports
from utilities.baseClass import baseClass


class EmpresasPage(baseClass):

    frame_body = (By.NAME,"body")
    frame_main = (By.NAME, "mainLayout")
    frame_main_2 = (By.NAME, "mainLayoutBody")
    frame_cuentas_menu = (By.ID,"frame10")
    frame_header = (By.NAME,"header")
    btn_cambiar_empresa = (By.CSS_SELECTOR, "a[href='/ebank2/cambioEmpresaActual.do?accion=executeObtenerListadoHeader']")
    table_empresas = (By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr")
    btn_aceptar = (By.CSS_SELECTOR, "img[src='/ebank2/jsp/resources/img/admc/botAceptar.gif']")
    current_empresa = (By.CSS_SELECTOR, "td.texto_Gris9 b")

    def __init__(self, driver):
        self.driver = driver

    def click_cambiar_empresa(self):
        self.wait_frame_presence(EmpresasPage.frame_header, 240)
        self.wait_to_click(EmpresasPage.btn_cambiar_empresa, 240)
        self.driver.switch_to.default_content()

    def get_table_empresas(self):
        self.wait_frame_presence(EmpresasPage.frame_body, 240)
        self.wait_frame_presence(EmpresasPage.frame_main, 20)
        self.wait_frame_presence(EmpresasPage.frame_main_2, 20)
        return self.driver.find_elements(*EmpresasPage.table_empresas)

    def get_empresa(self, row_empresa):
        xpath_name_empresa = f"/html/body/table/tbody/tr/td/table/tbody/tr[{row_empresa}]/td[2]"
        name_empresa = (By.XPATH, xpath_name_empresa)
        # self.wait_frame_presence(EmpresasPage.frame_body, 240)
        # self.wait_frame_presence(EmpresasPage.frame_main, 20)
        # self.wait_frame_presence(EmpresasPage.frame_main_2, 20)
        return self.driver.find_element(*name_empresa)

    def click_empresa(self, row_empresa):
        xpath_input_empresa = f"/html/body/table/tbody/tr/td/table/tbody/tr[{row_empresa}]//input"
        input_empresa = (By.XPATH, xpath_input_empresa)
        self.driver.find_element(*input_empresa).click()

    def click_aceptar(self):
        self.driver.find_element(*EmpresasPage.btn_aceptar).click()
        # time.sleep(5) # Damos un tiempo xq sino saca el resumen sin hacer
        # el cambio de empresa
        self.driver.switch_to.default_content()
        self.wait_frame_presence(EmpresasPage.frame_header, 240) #240 # Hacemos
                                                                # aca el cambio de
                                                                # frame, no en
                                                                # get_current_empresa
    def get_current_empresa(self):
        return self.driver.find_element(*EmpresasPage.current_empresa)
