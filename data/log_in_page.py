"""
Separamos por empresa primero y luego por banco, porque si hacemos
todo en un mismo diccionario se hace muy engorroso entenderlo. Ademas cada
banco tiene campos de datos diferentes
"""
# Standard imports
import io

# Third party imports
import msoffcrypto
import openpyxl

# Proyect imports
from menu.menu import msg_bank_emp_inexistente
from data.directory import DIRECTORY, TODAY
from data import files_paths as fp

ADRESSES_TESORERIA = ["testmail1@gmail.com","testmail2@gmail.com", "testmail3@gmail.com"]
ADRESSES_COBRANZAS = ["testmail1@gmail.com","testmail3@gmail.com", "testmail4@gmail.com"]
ADRESSES_PROVEEDORES = ["testmail1@gmail.com","testmail5@gmail.com"]
ADRESSES_CONTABILIDAD = ["testmail1@gmail.com","testmail6@gmail.com"]

#leo la contraseña desde el archivo
decrypted_workbook = io.BytesIO()

PATH_USER = fp.paths["user"]


with open(PATH_USER, 'rb') as file:
    office_file = msoffcrypto.OfficeFile(file)
    office_file.load_key(password='clave$1504', verify_password=True)
    office_file.decrypt(decrypted_workbook)

# `filename` can also be a file-like object.
workbook = openpyxl.load_workbook(filename=decrypted_workbook)

worksheet = workbook["BANCOS"]

EMPRESA = {
"DECORMEC SA":{
                "BANK_NAME_1":{"adherente":"sample_value_1",
                             "doc":"sample_value_1",
                             "cuenta":["sample_value_1", "sample_value_1"],
                             "clave":worksheet['B7'].value,
                             "path":[f"{DIRECTORY}\\paperworks\\SaldMovs_CC$-021-sample_value_1_{TODAY}.xls", f"{DIRECTORY}\\paperworks\\SaldMovs_CC$-021-sample_value_1_{TODAY}.xls"]
                },
                "BANK_NAME_2":{"usuario":"sample_value_2",
                          "cuenta":["sample_value_2"],
                          "acceso":worksheet['E6'].value,
                          "ident":worksheet['E7'].value,
                          "path":[f"{DIRECTORY}\\paperworks\\extracto DECORMEC SA.csv"]
                 },
                "BANK_NAME_3": {"usuario":"sample_value_3",
                              "cuenta":["sample_value_3","sample_value_3"],
                              "path":[f"{DIRECTORY}\\paperworks\\consultaMovimientosExtendidos.xls", f"{DIRECTORY}\\paperworks\\consultaMovimientosExtendidos (1).xls"],
                              "clave": worksheet['H6'].value.split(' ')[0],
                 },
                 "email_addresses":{"TESORERIA":ADRESSES_TESORERIA,
                          "COBRANZAS": ADRESSES_COBRANZAS,
                          "PROVEEDORES": ADRESSES_PROVEEDORES,
                          "CONTABILIDAD": ADRESSES_CONTABILIDAD
                 }
},
"WENTEK SA":{
              "BANK_NAME_1":{"adherente":"sample_value_4",
                           "doc":"sample_value_4",
                           "cuenta":["sample_value_4", "sample_value_4"],
                           "clave": worksheet['B15'].value,
                           "path":[f"{DIRECTORY}\\paperworks\\SaldMovs_CC$-021-sample_value_4_{TODAY}.xls", f"{DIRECTORY}\\paperworks\\SaldMovs_CC$-021-sample_value_4_{TODAY}.xls"]
              },
              "BANK_NAME_2":{"usuario":"sample_value_5",
                        "cuenta":["sample_value_5"],
                        "acceso": worksheet['E14'].value,
                        "ident": worksheet['E15'].value,
                        "path":[f"{DIRECTORY}\\paperworks\\extracto WENTEK SA.csv"]
              },
              "email_addresses":{"TESORERIA":ADRESSES_TESORERIA,
                       "COBRANZAS": ADRESSES_COBRANZAS,
                       "PROVEEDORES": ADRESSES_PROVEEDORES,
                       "CONTABILIDAD": ADRESSES_CONTABILIDAD
              }
},
"MI ESQUINA SA":{
                "BANK_NAME_1":{"adherente":"sample_value_6",
                             "doc":"sample_value_6",
                             "cuenta":["sample_value_6"],
                             "clave": worksheet['B39'].value,
                             "path":[f"{DIRECTORY}\\paperworks\\SaldMovs_CC$-021-sample_value_6_{TODAY}.xls"]
                  },
                  "email_addresses":{"TESORERIA":ADRESSES_TESORERIA,
                           "COBRANZAS": ADRESSES_COBRANZAS,
                           "PROVEEDORES": ADRESSES_PROVEEDORES,
                           "CONTABILIDAD": ADRESSES_CONTABILIDAD
                  }
},
"IKAIKA SA":{
            "BANK_NAME_1":{"adherente":"sample_value_7",
                          "doc":"sample_value_7",
                          "cuenta":["sample_value_7"],
                          "clave": worksheet['B23'].value,
                          "path":[f"{DIRECTORY}\\paperworks\\SaldMovs_CC$-021-sample_value_7_{TODAY}.xls"]
                          },
            "BANK_NAME_2":{"BANK_NAME_2":"sample_value_8",
                      "cuenta":["sample_value_8"],
                      "acceso": worksheet['E22'].value,
                      "ident": worksheet['E23'].value,
                      "path":[f"{DIRECTORY}\\paperworks\\extracto IKAIKA SA.csv"]
                      },
            "email_addresses":{"TESORERIA":ADRESSES_TESORERIA,
                     "COBRANZAS": ["testmail1@gmail.com","testmail2@gmail.com"],
                     "PROVEEDORES": ADRESSES_PROVEEDORES,
                     "CONTABILIDAD": ADRESSES_CONTABILIDAD
            }
},
"PEBEIRE S.A.":{
             "BANK_NAME_1":{"adherente":"sample_value_9",
                          "doc":"sample_value_9",
                          "cuenta":["sample_value_9"],
                          "clave": worksheet['B31'].value,
                          "path":[f"{DIRECTORY}\\paperworks\\SaldMovs_CC$-021-sample_value_9_{TODAY}.xls"]
              },
             "BANK_NAME_2":{"usuario":"sample_value_10",
                       "cuenta":["sample_value_10"],
                       "acceso": worksheet['E30'].value,
                       "ident": worksheet['E31'].value,
                       "path":[f"{DIRECTORY}\\paperworks\\extracto PEBEIRE S.A..csv"]
            },
            "email_addresses":{"TESORERIA":ADRESSES_TESORERIA,
                     "COBRANZAS": ADRESSES_COBRANZAS,
                     "PROVEEDORES": ADRESSES_PROVEEDORES,
                     "CONTABILIDAD": ADRESSES_CONTABILIDAD
            }
}
}

def switch_empresa(key):
    EMPRESA = {
    "1":"DECORMEC SA",
    "2":"IKAIKA SA",
    "3":"PEBEIRE S.A.",
    "4":"WENTEK SA",
    "5":"MI ESQUINA SA",
    }
    return EMPRESA[key]

def switch_bancos(key):
    EMPRESA = {
    "1":"BANK_NAME_1",
    "2":"BANK_NAME_2",
    "3":"BANK_NAME_3",
    }
    return EMPRESA[key]

def seleccion_datos(empresa, banco):
    try:
        key_empresa = switch_empresa(empresa)
        nombre_banco = switch_bancos(banco)
        datos_empresa = EMPRESA[key_empresa][nombre_banco]
        # Agrego nombre de empresa y banco al diccionario con los datos
        datos_empresa["email_addresses"] = EMPRESA[key_empresa]["email_addresses"]
        datos_empresa["empresa"] = key_empresa
        datos_empresa["banco"] = nombre_banco
        return datos_empresa
    except KeyError:
        msg_bank_emp_inexistente()
