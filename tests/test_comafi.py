# Standard library imports
from datetime import date
import sys
import os
import time
from data.directory import DIRECTORY

# Third party imports
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #borrar desp de rehacer POM con seleccion fecha
from selenium.common.exceptions import NoSuchElementException, TimeoutException, SessionNotCreatedException, UnexpectedAlertPresentException

# Proyect imports
from utilities.baseClass import baseClass
from dataprocessing.excelProcessing import (DATE_FORMAT,
                                            TODAY_dt64,
                                            DAYS_AGO_dt64)
from page_objects.comafi.log_in_page import LogInPage
from page_objects.comafi.main_page import MainPage
from page_objects.comafi.extracto_page import ExtractoPage
from page_objects.comafi.extracto_seguro_page import ExtractoSeguroPage
from page_objects.comafi.empresas_page import EmpresasPage
from menu.menu import (msg_file_not_downloaded,
                      msg_minimizar_manualmente,
                      msg_actualizar_driver,
                      msg_rename_file_exists)

class TestsComafi(baseClass):

    def __init__(self, datos_empresa, mes, year):
        self.user = datos_empresa["usuario"]
        self.empresa = datos_empresa["empresa"]
        self.periodo = mes[0]+' '+year
        self.month = int(mes[2])
        self.start_date = '01'+'/'+mes[2]+'/'+year
        self.last_date = mes[1]+'/'+mes[2]+'/'+year
        self.path = datos_empresa["path"][0]
        self.cuenta = datos_empresa["cuenta"][0]
        self.acceso = datos_empresa["acceso"]
        self.ident = datos_empresa["ident"]
        ingreso = 0

        try:
            if self.driver.session_id != None:
            # Si no existe el driver salta excepción y en la excepción lo crea. Esto es para usar solo un mismo driver para todos los tests. Una vez inicializado el driver con el objeto creado en la baseClass, ya no se crea mas.
                pass
        except AttributeError:
            # self.creacion_driver()
            try:
                self.creacion_driver()
            except SessionNotCreatedException:
                msg_actualizar_driver()
                sys.exit(1)

    def test_log_in(self):
        # El get() para abrir la pagina lo hacemos acá y no en el conftest porque
        # la sesión caduca. Entonces si lo ponemos en el setup() del conftest te
        # la abre una vez sola.
        log_in_page = LogInPage(self.driver)
        # Con el ".get()" al driver le estas diciendo que ingrese a esa url
        self.driver.get("https://hb.comafiempresas.com.ar/ebank2/HBE.do")
        log_in_page.enter_user(self.user)
        self.rsleep1()
        log_in_page.click_acces_key()
        self.rsleep1()
        log_in_page.enter_acceso(self.acceso)
        self.rsleep1()
        log_in_page.enter_ident(self.ident)
        self.rsleep1()
        log_in_page.click_ingresar()

    def test_get_extracto(self, report):
        main_page = MainPage(self.driver)
        # ACCES TO EXTRACTOS
        main_page.consultas()
        main_page.cuentas()

        #comprobar si lleva a la página segura

        try:
            main_page.es_seguro()
            ingreso = 1
        except NoSuchElementException:
            ingreso = 0

        if ingreso == 1:
            self.path = f"{DIRECTORY}\\paperworks\\movimientos_cuenta {self.empresa}.xlsx"
            main_page.ingresar()
            self.driver.switch_to.window(self.driver.window_handles[1])
            extracto_page = ExtractoSeguroPage(self.driver)
            extracto_page.click_movimientos()
        else:
            main_page.go_to_extracto()
            self.rsleep1()
            extracto_page = ExtractoPage(self.driver)
        extracto_page.select_start_date(self.start_date)
        self.rsleep1()
        self.rsleep2()

        if not report:
            # Si se ejecuta reporte diario (report = True), no se modifica
            # la ultima fecha, se deja la que aparece por defa  ult
            extracto_page.select_last_date(self.last_date)
        extracto_page.click_ir()
        self.rsleep2()
        # DOWNLOAD EXTRACTO
        try:
            extracto_page.check_movimientos_presence() # Si no hay movimientos
                                                       # minimiza y termina
            msg_file_not_downloaded(self.empresa)
        except TimeoutException: # Si hay movimientos, descarga, renombra y
                                 # luego minimiza si no es reporte
            extracto_page.click_exportar()

            while not (os.path.exists(f"{DIRECTORY}\\paperworks\\movimientos_cuenta.xlsx") or os.path.exists(f"{DIRECTORY}\\paperworks\\extracto.csv")):
                time.sleep(1)
            self.rsleep2()
            current_path = self.path.replace(f" {self.empresa}", "")
            try:
                os.rename(current_path, self.path)
            except FileExistsError:
                msg_rename_file_exists(self.path, self.empresa)
        self.rsleep2()

        if ingreso == 1:
            extracto_page.click_salir()
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        if not report:
            try:
                self.driver.minimize_window()
            except WebDriverException:
                msg_minimizar_manualmente()
        return ingreso

    def test_select_empresa(self):
        empresas_page = EmpresasPage(self.driver)
        empresas_page.click_cambiar_empresa()
        elements_rows_empresas = empresas_page.get_table_empresas()
        start_i = 3 # fila 1 y fila 2 son titulos (xpath no usa 0 index)
        last_i = len(elements_rows_empresas)-1 # -1 por no tener que contar la
                                               # ultima fila xq no tiene
                                               # empresa, es un botón. En el
                                               # xpath no se usa 0 index
        for i in range(start_i, last_i):
            if i % 2 != 0: # Entramos solo a las pares, xq estan las
                           # filas separadoras en las impares
                empresa_name = empresas_page.get_empresa(i).text
                if empresa_name == self.empresa:
                    empresas_page.click_empresa(i)
                    empresas_page.click_aceptar()
                    break
        # Damos por seleccionada la empresa cuando aparece su nombre en la pag
        current_empresa = empresas_page.get_current_empresa().text
        while current_empresa != self.empresa:
            current_empresa = empresas_page.get_current_empresa().text
            self.rsleep1()


    def test_download_movimientos(self):
        while True:
            try:
                # LOG IN
                self.test_log_in()
                self.rsleep2()
                if self.empresa != "WENTEK SA" and self.empresa != "DECORMEC SA":
                    self.test_select_empresa()
                ingreso = self.test_get_extracto(False)
                return ingreso
                #break
            except UnexpectedAlertPresentException:
                # Si se pone mal la clave, o falta completar algun campo salen alerts.
                # entonces lo que se hace es pasar de largo si sale el alert y volver
                # a cargar la página, se repite el test
                pass


    def test_get_saldos_movimientos(self):
        self.saldos = {}
        if self.empresa == "WENTEK SA" or self.empresa == "DECORMEC SA":
            self.test_log_in()
            self.rsleep2()
        if self.empresa != "WENTEK SA" and self.empresa != "DECORMEC SA":
            self.test_select_empresa()
        # TOMO SALDO
        main_page = MainPage(self.driver)
        saldo = main_page.get_saldo().text
        self.saldos[self.cuenta] = saldo
        # MODIFICO FECHAS PARA EXTRACTO
        self.start_date = DAYS_AGO_dt64.item().strftime(DATE_FORMAT)
        # DESCARGO EXTRACTO
        ingreso = self.test_get_extracto(True)
        #SALIR
        if self.empresa == "WENTEK SA" or self.empresa == "PEBEIRE S.A.":
            extracto_page = ExtractoPage(self.driver)
            extracto_page.click_salir()
        if self.empresa == "WENTEK SA":
            try:
                self.driver.minimize_window()
            except WebDriverException:
                msg_minimizar_manualmente()
        return ingreso
