# Standard library imports
from datetime import date
import sys

# Third party imports
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # borrar desp de rehacer POM con seleccion fecha
from selenium.common.exceptions import TimeoutException, SessionNotCreatedException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pywinauto.keyboard import send_keys

# Proyect imports
from utilities.baseClass import baseClass
from page_objects.credicoop.log_in_page import LogInPage
from page_objects.credicoop.main_page import MainPage
from page_objects.credicoop.saldos_page import SaldosPage
from page_objects.credicoop.movimientos_page import MovimientosPage
from menu.menu import (msg_file_not_downloaded,
                       msg_minimizar_manualmente,
                       msg_actualizar_driver)



class TestsCredicoop(baseClass):

    def __init__(self, datos_empresa, mes, year):
        self.adherente = datos_empresa["adherente"]
        self.doc = datos_empresa["doc"]
        self.empresa = datos_empresa["empresa"]
        self.clave = datos_empresa["clave"]
        self.periodo = mes[0] + ' ' + year
        self.month = int(mes[2])
        try:
            if self.driver.session_id != None:
                # Si no existe el driver salta excepción y en la excepción lo crea. Esto es para usar solo un mismo driver para todos los tests. Una vez inicializado el driver con el objeto creado en la baseClass, ya no se crea mas.
                pass
        except AttributeError:
            try:
                self.creacion_driver()
            except SessionNotCreatedException:
                msg_actualizar_driver()
                sys.exit(1)

    def test_log_in(self):
        # El get() para abrir la pagina lo hacemos acá y no en el conftest porque la sesión caduca. Entonces si lo ponemos en el setup() del conftest te la abre una vez sola
        log_in_page = LogInPage(self.driver)
        self.driver.execute_script("window.open('https://bancainternet.bancocredicoop.coop/bcclbe/');")
        self.rsleep2()
        self.rsleep2()
        self.rsleep2()
        self.rsleep2()
        send_keys("{ESC}")
        self.rsleep2()
        self.driver.get("https://bancainternet.bancocredicoop.coop/bcclbe/")  # Con el ".get()" al driver le estas diciendo que ingrese a esa url
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        # LOG IN
        log_in_page.desplegable_adherente()
        self.rsleep1()
        log_in_page.select_adherente()
        self.rsleep1()
        log_in_page.enter_adherente(self.adherente)
        self.rsleep1()
        log_in_page.enter_doc(self.doc)
        self.rsleep1()
        log_in_page.click_input_clave()
        self.rsleep1()
        log_in_page.enter_clave(self.clave)
        self.rsleep1()
        log_in_page.click_ingresar()
        # time.sleep(10)

    def test_download_movimientos(self, report):
        # LOG IN
        if report:
            self.saldos = {}
        self.test_log_in()

        main_page = MainPage(self.driver)
        # ACCES TO SALDOS
        main_page.wait_main_page_load()
        # VERIFICAMOS SI HAY ALGUNA VENTANA EMERGENTE. SI LA HAY, LA CERRAMOS. COMO ES ALGO QUE SIEMPRE HAY QUE HACER AL IGUAL QUE EL LOGIN, LO METEMOS DENTRO DEL LOGIN
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
        if report:
            # Tomo saldos bancarios para reporte
            saldos_elements = main_page.get_saldos_elements()
            cuentas_elements = main_page.get_cuentas_elements()
            for saldo, cuenta in zip(saldos_elements, cuentas_elements):
                self.saldos[cuenta.text] = saldo.text
        btn_consultas = main_page.get_btn_consultas()
        self.rsleep2()
        ActionChains(self.driver).move_to_element(btn_consultas).perform()
        main_page.click_saldos_movimientos()
        # self.driver.execute_script("document.elementFromPoint(200, 100).click()")
        saldos_page = SaldosPage(self.driver)
        saldos_page.wait_saldos_load()
        self.rsleep2()
        inputs_cc = saldos_page.get_inputs()
        self.rsleep2()
        # No se puede iterar estos objetos haciendo "for input_cc in inputs_cc:" y hacer todo para cada elemento asi de manera ideal porque cuando se vuelve a la saldos page salta error: "selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document". Entonces lo que hay que hacer es volver a obtener los elementos para aplicarles las acciones, por esto en cada iteracion se lee de nuveo los WebElements.
        # Entonces antes del for se lee la cantidad de cuentas corrientes para saber cuantas son. Con esto se crea el for y en base a esa cantidad con el metodo range(len()) se  arma el for que se recorrera tantas veces como cuentas corrientes haya, y se accede a cada cuenta corriente a traves del numero de iteracion en la que se esta. Es rustico pero hay que releer siempre los elementos porque sino no se encuentran
        # MOVIMIENTOS
        movimientos_page = MovimientosPage(self.driver)
        self.rsleep2() # AGREGADO PARCHE***
        for item in range(len(inputs_cc)):
            self.rsleep2()
            inputs_cc = saldos_page.get_inputs()
            self.rsleep2()
            inputs_cc[item].click()
            if not report:
                # Si se trata de conciliacion bancaria, que seleccione las fechas. Si se trata de los saldos, no es necesario porque por default te trae ultimos 10 dias y necesitamos ultimos 3.
                saldos_page.start_date_menu()
                self.rsleep2()
                self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles)-1]) #Cambiamos a la última pestaña que se haya abierto
                self.test_select_date(saldos_page, 'start')
                # time.sleep(0.5)
                self.driver.switch_to.window(self.driver.window_handles[0]) #Cambiamos a la ventana inicial
                self.rsleep2()
                # Selección último día si no estamos en el mismo mes
                if self.month != date.today().month:
                    saldos_page.last_date_menu()
                    self.rsleep2()
                    self.driver.switch_to.window(self.driver.window_handles[len(self.driver.window_handles)-1]) #Cambiamos a la última pestaña que se haya abierto
                    # time.sleep(0.5)
                    self.test_select_date(saldos_page, 'last')
                self.rsleep1()
            saldos_page.go_to_movimientos()
            try:
            # Si no hay movimientos (para saberlo busca elemento con texto: 'No existen movimientos entre las fechas seleccionadas')
                movimientos_page.check_movimientos_presence()
                msg_file_not_downloaded(self.empresa)
            except:
            # Si hay movimientos (no encontró texto) se sigue con la descarga del resumen
                movimientos_page.desplegable_export_format()
                self.rsleep2()
                movimientos_page.select_excel_format()
                self.rsleep2()
                movimientos_page.export_movimientos()
            if inputs_cc[item] != inputs_cc[len(inputs_cc)-1]:
                # Si estoy con el último input vuelvo a la saldos_page
                self.rsleep2() # AGREGADO PARCHE***
                movimientos_page.back_to_saldos_page()
                saldos_page.wait_saldos_load()
            else:
                if report:
                    movimientos_page.log_out()
                    self.rsleep1()
                    movimientos_page.wait_logout_text()
                    if self.empresa == "MI ESQUINA SA":
                    # Minimizo con la úlima empresa
                        try:
                            self.driver.minimize_window()
                        except WebDriverException:
                            msg_minimizar_manualmente()
                else:
                    # Si no hay que hacer lo de cheques a debitarse que minimice.
                    # Ver para minimizar cuando hace la ultima descarga de cheques a debitarse
                    try:
                        self.driver.minimize_window()
                    except WebDriverException:
                        msg_minimizar_manualmente()

    def test_select_date(self, object, mode):
        saldos_page = object
        bankPeriod = saldos_page.get_period()
        # Selecciono periodo
        while bankPeriod != self.periodo:
            self.rsleep2()
            saldos_page.previous_month_select()
            bankPeriod = saldos_page.get_period()
            # time.sleep(0.25)
        days = saldos_page.get_days()
        days_count = len(days)
        if mode == 'start':
            index = 0
        elif mode == 'last':
            # Usa '0' indentation, entonces hay que restarle 1 a la cuenta
            index = days_count - 1
        self.rsleep1()
        days[index].click()
        # time.sleep(0.5)
        self.driver.switch_to.window(self.driver.window_handles[0]) #Cambiamos a la ventana inicial
        # time.sleep(0.5)
