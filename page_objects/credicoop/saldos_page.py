# Standard library imports

#Third party imports
from selenium.webdriver.common.by import By

#Proyect imports
from utilities.baseClass import baseClass

class SaldosPage(baseClass):

    # btn_init_date_menu = (By.CSS_SELECTOR, "a[href='javascript:show_calendar('consultasForm.desde');'] img")  # Tardan mucho estos selectores
    # btn_last_date_menu = (By.CSS_SELECTOR, "a[hre='javascript:show_calendar('consultasForm.hasta');'] img")

    btn_init_date_menu = (By.XPATH, "//*[@id='cuentas']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]/a/img")
    btn_last_date_menu = (By.XPATH, "//*[@id='cuentas']/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td[3]/a/img")
    btn_previous_month = (By.XPATH, "//a[text()='<']")
    period = (By.XPATH, "//center/font/b")
    days = (By.XPATH, "/html/body/font/table/tbody/tr/td/font/a")
    btn_consultar = (By.CSS_SELECTOR, "input[value='Consultar']")
    input_cc = (By.CSS_SELECTOR, "input[name='cuenta']")
    table_cc = (By.CSS_SELECTOR, "table.credi")

    def __init__(self, driver):
        self.driver = driver

    def wait_saldos_load(self):
        self.wait_element_presence(SaldosPage.table_cc, 10)

    def get_inputs(self):
        return self.driver.find_elements(*SaldosPage.input_cc)

    def start_date_menu(self):
        self.wait_to_click(SaldosPage.btn_init_date_menu, 20)

    def previous_month_select(self):
        self.wait_to_click(SaldosPage.btn_previous_month, 20)

    def last_date_menu(self):
        self.wait_to_click(SaldosPage.btn_last_date_menu, 20)

    def go_to_movimientos(self):
        self.driver.find_element(*SaldosPage.btn_consultar).click()

    def get_period(self):
        return self.driver.find_element(*SaldosPage.period).text

    def get_days(self):
        return self.driver.find_elements(*SaldosPage.days)
