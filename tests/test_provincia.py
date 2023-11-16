# Standard library imports
from datetime import date
import sys

# Third party imports
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #borrar desp de rehacer POM con seleccion fecha
from selenium.common.exceptions import NoSuchElementException, TimeoutException, SessionNotCreatedException

# Proyect imports
from utilities.baseClass import baseClass
from dataprocessing.excelProcessing import (DATE_FORMAT,
                                            TODAY_dt64,
                                            DAYS_AGO_dt64)
from page_objects.provincia.log_in_page import LogInPage
from page_objects.provincia.movimientos_page import MovimientosPage
from page_objects.provincia.perfil_page import PerfilPage
from page_objects.provincia.detalle_movimientos_page import DetalleMovimientosPage
from menu.menu import (msg_file_not_downloaded,
                      msg_minimizar_manualmente,
                      msg_actualizar_driver)
from data import dates_page

class TestsProvincia(baseClass):

    def __init__(self, datos_empresa, mes, year):
        self.usuario = datos_empresa["usuario"]
        self.cuenta = datos_empresa["cuenta"]
        self.empresa = datos_empresa["empresa"]
        self.clave = datos_empresa["clave"]
        self.periodo = mes[0]+' '+year
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
        #El get() para abrir la pagina lo hacemos acá y no en el conftest porque la sesión caduca. Entonces si lo ponemos en el setup() del conftest te la abre una vez sola
        log_in_page = LogInPage(self.driver)
        self.driver.get("https://www.bancoprovincia.bancainternet.com.ar/spa-empresas/") #Con el ".get()" al driver le estas diciendo que ingrese a esa url
        # LOG IN
        log_in_page.version_vieja()
        self.rsleep1()
        log_in_page.enter_usuario(self.usuario)
        self.rsleep1()
        log_in_page.click_usuario()
        self.rsleep1()
        log_in_page.enter_clave(self.clave)
        self.rsleep1()
        log_in_page.click_input_clave()

    def test_elegir_perfil(self):
        perfil_page = PerfilPage(self.driver)
        self.rsleep2()
        perfil_page.elegir_perfil()
        self.rsleep1()
        perfil_page.click_aceptar()

    def test_download_movimientos(self, report):
        self.saldos = {}
        self.test_log_in()
        self.rsleep2()
        self.test_elegir_perfil()
        movimientos_page = MovimientosPage(self.driver)
        movimientos_page.click_movimientos()
        if report:
            self.test_select_date_report()
        else:
            self.test_select_date_conciliacion()
        detalle_movimientos_page = DetalleMovimientosPage(self.driver)
        cuentas = len(detalle_movimientos_page.get_cuentas_elements())
        detalle_movimientos_page.elegir_cuenta()

        for i in range(cuentas):
            opciones = detalle_movimientos_page.get_cuentas_elements()
            detalle_movimientos_page.opcion_select(opciones[i])
            self.rsleep2()
            for j in range(2):
                detalle_movimientos_page.click_buscar()
            try:
                detalle_movimientos_page.click_excel()
            except NoSuchElementException:
                self.rsleep2()
            detalle_movimientos_page.elegir_cuenta()

        detalle_movimientos_page.volver()
        try:
            self.driver.minimize_window()
        except WebDriverException:
            msg_minimizar_manualmente()

    def test_select_date_report(self):
        detalle_movimientos_page = DetalleMovimientosPage(self.driver)
        fecha = DAYS_AGO_dt64.item().strftime("%d-%m-%Y")
        detalle_movimientos_page.set_fecha_inicial(fecha)

    def test_select_date_conciliacion(self):
        detalle_movimientos_page = DetalleMovimientosPage(self.driver)
        fecha_inicio, fecha_final = self.hacer_fecha()
        self.rsleep2()
        detalle_movimientos_page.set_fecha_inicial(fecha_inicio)
        self.rsleep2()
        detalle_movimientos_page.set_fecha_final(fecha_final)

    def hacer_fecha(self):
        mes = dates_page.switch_mes(str(self.month))
        ultimo_dia = mes[1]
        num_mes = mes[2]
        fecha1 = "01-" + num_mes + "-" + self.periodo.split(" ")[1]
        fecha2 = ultimo_dia + "-" + num_mes + "-" + self.periodo.split(" ")[1]
        return fecha1, fecha2

    def test_get_saldos_movimientos(self):
        self.saldos = {}
        # TOMO SALDO
        movimientos_page = MovimientosPage(self.driver)
        saldos_elements = movimientos_page.get_saldo()
        for saldo, cuenta in zip(saldos_elements, self.cuenta):
            self.saldos[cuenta] = saldo.text
        #SALIR
        movimientos_page.salir()
