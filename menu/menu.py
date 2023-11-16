# Standard library imports
import sys

# Third party imports

# Proyect imports


def welcome_message():
    print('¡HOLA! Soy tu asistente virtual ROBYCOOP. Te voy a ayudar con los Bancos.')

def functions_menu():
    print("""
MENU
Seleccione la funcion a ejecutar:
1) Reporte bancario diario - saldos y transacciones
2) Descargar resumen bancario mensual y conciliar
3) Reporte de saldos mensuales bancarios
""")

def data_menu():
    print("""
EMPRESA:
1) DECORMEC
2) IKAIKA
3) PEBEIRE
4) WENTEK
5) MI ESQUINA

MES:
1) Enero
2) Febrero
3) Marzo
4) Abril
5) Mayo
6) Junio
7) Julio
8) Agosto
9) Septiembre
10) Octubre
11) Noviembre
12) Diciembre

AÑO:
1) 2022
2) 2023""")

def salir():
    input("\nEJECUCION FINALIZADA. CERRAR PROGRAMA Y VOLVER A EJECUTAR SI LO DESEA.")
    sys.exit(0)

def invalid_input():
    print("\n-VALOR INVALIDO- El valor ingresado debe ser un número entero presente en las opciones.\n")

def selected_option_main(empresa, mes, year):
    print(f"\n\n¡PERFECTO!. Elegiste {empresa}, MES {mes}, YEAR {year}.\n")

def banks_menu():
    print("""
BANCO:
1) Credicoop
2) Comafi
3) Provincia
""")

def msg_file_not_downloaded(empresa):
    print(f"\n## FILE NOT DOWNLOADED ## No hay movimientos de {empresa} para descargar.")

def msg_conciliacion_bank(bank):
    print(f"\nConciliación {bank}. Iniciando...")

def msg_calculo_saldos(bank):
    print(f"\nCalculo de saldos {bank}. Iniciando...")

def msg_bank_emp_inexistente():
    print("\n-OPCION INVALIDA- Ingrese un banco/empresa válido")

def msg_archivo_faltante():
    input("\n### ERROR ###: No se encuentran los archivos en el directorio correspondiente.\nPresione 'ENTER' para continuar")

def msg_cerrar_archivo():
    input("\n### ERROR ###: Cerrar archivos 'Excel' abiertos. Presione 'ENTER' para continuar")

def msg_conc_file_generated():
    input("\n### ARCHIVO CONCILIACION GENERADO ### Por favor, revisar registros y si es necesario clasificar para enviar email.\nPresione 'ENTER' para continuar")

def msg_saldos_file_generated():
    input("\n### ARCHIVO SALDOS GENERADO ### Presione 'ENTER' para regresar al menu principal")

def msg_colocar_mayor(empresa, banco, cuenta, item):
    input(f"\nEn caso de existir movimientos, colocar Libro Mayor {empresa} {banco} {cuenta} con nombre 'Libro{1+item}.xlsx'.\nPresione 'ENTER' para continuar")

def msg_invalid_month():
    print("\n-OPCION INVALIDA- Ingrese un mes válido")

def msg_invalid_year():
    print("\n-OPCION INVALIDA- Ingrese un año válido")

def msg_mail_file_generated(clasificacion, banco, cuenta):
    print(f"\n## ARCHIVO GENERADO ## - Se ha generado archivo '{clasificacion}' {banco} {cuenta}")

def msg_mail_file_not_generated(clasificacion, banco, cuenta):
    print(f"\n## ARCHIVO NO GENERADO ## - No hay registros '{clasificacion}' {banco} {cuenta} para corregir")

def msg_debitados_generated(empresa, banco, cuenta):
    print(f"\n### REPORTE GENERADO ### 'cheques debitados' {empresa} {banco} {cuenta} generado.")

def msg_no_debitados(empresa, banco, cuenta):
    print(f"\n### ARCHIVO NO GENERADO ### No hay cheques debitados {empresa} {banco} {cuenta}.")

def msg_debitos_creditos_generated(empresa, banco, cuenta):
    print(f"\n### REPORTE GENERADO ### 'Movimientos bancarios' {empresa} {banco} {cuenta} generado.")

def msg_no_debitos_creditos(empresa, banco, cuenta):
    print(f"\n### ARCHIVO NO GENERADO ### No hay movimientos bancarios {empresa} {banco} {cuenta}.")

def msg_report_saldos_generated():
    print("\n### REPORTE SALDOS CREDICOOP GENERADO ###\n")

def msg_minimizar_manualmente():
    print("WebDriverException: Message: unknown error: failed to change window state to 'normal', current state is 'maximized'\nPOR FAVOR MINIMIZAR MANUALMENTE")

def msg_actualizar_driver():
    input("\n## ACTUALIZACION REQUERIDA ## - Por favor, solicitar actualización de la aplicación para poder utilizarla.")

def msg_rename_file_exists(existing_path, empresa):
    input(f"""
Ya existe el archivo {existing_path}.
Eliminarlo y renombrar manualmente el archivo 'extracto.csv' como 'extracto {empresa}.csv'
Presione 'ENTER' para continuar""")

def msg_empty_table(file, empresa, banco, cuenta):
    print(f"\nNo hay {file} {empresa} {banco} {cuenta}.\nLa tabla estará vacía.")

def msg_clasificar_debitos_creditos():
    input("### ARCHIVOS MOVIMIENTOS BANCARIOS GENERADOS ###. De ser necesario, clasificar para ser enviados por mail.\nUna vez ya clasificados, guardar archivo y presione 'ENTER' para continuar.")
