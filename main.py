# Standard library imports
from datetime import date
import sys
# Third party imports

# Proyect imports
from menu import menu
from data import log_in_page, dates_page #Para tomar datos (switchs) empresa y mes seleccionados
from tests.test_credicoop import TestsCredicoop
from tests.test_comafi import TestsComafi
from tests.test_provincia import TestsProvincia
from errors.inputs import inputValidations as iv # iv: Input Validations
from errors.dates import dateValidations as dv # dv: date Validations
from dataprocessing.excelProcessing import ExcelProcessing

# https://www.youtube.com/watch?v=JL9RMCS4Sho&t=786s ejecutable .bat

def main():
    menu.welcome_message()

    while True:
        if len(sys.argv) > 1:
            function = str(sys.argv[1])
            type(function)
            sys.argv=''
        else:
            menu.functions_menu()
            function = input("Ingrese opción: ")

        if iv.validation_bank_menu(function):

            if function == "1":
            # Actualización de cheques (se debe ingresar a todos los bancos)
                print("\nReporte bancario diario iniciado...\n\n")
                # Ya se que será el mes y año corrientes. Por lo tanto asigno estos valores
                year = dates_page.switch_year("2")
                mes = dates_page.switch_mes(str(date.today().month))

                datos_empresa = log_in_page.seleccion_datos("1", "1")
                excel_processing = ExcelProcessing(datos_empresa, mes[2], year)
                # Creo un unico objeto para navegar, ya que no quiero que se abra una nueva ventana
                # en cada iteracion. Al crear el objeto, se crea un driver nuevo y en
                # consecuencia se abre una nueva ventana. Como lo creo afuera del "for",
                # y tengo que inicializar la clase con valores, le asigno los primeros
                # valores afuera y el resto los voy asignando con el for
                credicoop = TestsCredicoop(datos_empresa, mes, year)

                for item in range(1,6):
                    if item != 1:
                        datos_empresa = log_in_page.seleccion_datos(str(item), "1")
                        excel_processing.empresa = datos_empresa["empresa"]
                        excel_processing.banco = datos_empresa["banco"]
                        excel_processing.paths_extractos = datos_empresa["path"]
                        excel_processing.cuentas = datos_empresa["cuenta"]
                        credicoop.adherente = datos_empresa["adherente"]
                        credicoop.doc = datos_empresa["doc"]
                        credicoop.empresa = datos_empresa["empresa"]
                        credicoop.clave = datos_empresa["clave"]
                    credicoop.test_download_movimientos(True)
                    excel_processing.saldos[excel_processing.banco][credicoop.empresa] = credicoop.saldos
                    excel_processing.report_debitos_creditos()

                datos_empresa = log_in_page.seleccion_datos("1", "2")
                comafi = TestsComafi(datos_empresa, mes, year)

                for item in range(1,5):
                    if item != 1:
                        datos_empresa = log_in_page.seleccion_datos(str(item), "2")
                        comafi.user = datos_empresa["usuario"]
                        comafi.empresa = datos_empresa["empresa"]
                        comafi.cuenta = datos_empresa["cuenta"][0]
                        comafi.acceso = datos_empresa["acceso"]
                        comafi.ident = datos_empresa["ident"]
                        comafi.path = datos_empresa["path"][0]
                    excel_processing.empresa = datos_empresa["empresa"]
                    excel_processing.banco = datos_empresa["banco"]
                    excel_processing.paths_extractos = datos_empresa["path"]
                    excel_processing.cuentas = datos_empresa["cuenta"]
                    ingreso = comafi.test_get_saldos_movimientos()
                    excel_processing.saldos[excel_processing.banco][comafi.empresa] = comafi.saldos
                    excel_processing.report_debitos_creditos(ingreso)

                 # provincia
                datos_empresa = log_in_page.seleccion_datos("1", "3")
                provincia = TestsProvincia(datos_empresa, mes, year)

                excel_processing.empresa = datos_empresa["empresa"]
                excel_processing.banco = datos_empresa["banco"]
                excel_processing.paths_extractos = datos_empresa["path"]
                excel_processing.cuentas = datos_empresa["cuenta"]
                provincia.test_download_movimientos(True)
                provincia.test_get_saldos_movimientos()
                excel_processing.saldos[excel_processing.banco][provincia.empresa] = provincia.saldos
                excel_processing.report_debitos_creditos()

                excel_processing.export_debitos_creditos()
                excel_processing.report_saldos()

                menu.msg_clasificar_debitos_creditos()
                excel_processing.clasificados_debitos_creditos(datos_empresa["email_addresses"])


            elif function == "2" or function == "3":
            # Conciliación mensual
                # Se debe preguntar de qué banco, empresa, mes y año
                # Select bank menu
                menu.data_menu()
                menu.banks_menu()
                empresa = input("Indica el NUMERO de empresa: ")
                mes = input("Mes: ")
                year = input("Año: ")
                bank = input("Ingrese numero de banco: ")
                ingreso = 0

                if iv.validation_data_menu(empresa, mes, year) and iv.validation_bank_menu(bank): # Si saco esto salta error ver notas celu
                # Validados los inputs tomamos los datos
                    datos_empresa = log_in_page.seleccion_datos(empresa, bank)
                    mes = dates_page.switch_mes(mes)
                    year = dates_page.switch_year(year)

                    if dv.date_validation(mes, year) and datos_empresa is not None:
                        excel_processing = ExcelProcessing(datos_empresa, mes[2], year)

                        if function == "2":
                            menu.msg_conciliacion_bank(datos_empresa["banco"])
                            if bank == "1":
                                # Si es Conciliación COOP
                                credicoop = TestsCredicoop(datos_empresa, mes, year)
                                credicoop.test_download_movimientos(False)
                                pass
                            elif bank == "2":
                                # Si es Conciliación COMAFI
                                comafi = TestsComafi(datos_empresa, mes, year)
                                ingreso = comafi.test_download_movimientos()
                                pass
                            elif bank == "3":
                                provincia = TestsProvincia(datos_empresa, mes, year)
                                provincia.test_download_movimientos(False)
                                pass
                            excel_processing.conciliacion_file(ingreso)
                            menu.msg_conc_file_generated()
                            excel_processing.clasificados_conciliacion(datos_empresa["email_addresses"])

                        if function == "3":
                            menu.msg_calculo_saldos(datos_empresa["banco"])
                            excel_processing.calculo_saldos()
                            menu.msg_saldos_file_generated()

if __name__ == "__main__":
    main()
