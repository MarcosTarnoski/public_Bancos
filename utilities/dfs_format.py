# Standard library imports
import warnings

# Third party imports
import pandas as pd

# Proyect imports


DATE_FORMAT = "%d/%m/%Y"
CREDICOOP = "SaldMovs_CC$"
COMAFI = "extracto"
COMAFI_SEGURO = "movimientos_cuenta"
PROVINCIA = "consultaMovimientosExtendidos"

class DataframesFormat:

    def get_bank_df(self, path_extracto):

        # Por la condición que hay que evaluar (existencia de substring) no se puede usar un "switch case". Si la condicion fuese una igualdad sí se podría
        if CREDICOOP in path_extracto:
            # Si se quiere acceder al extracto del CREDICOOP entra acá
            COLUMNS_DROP = ['Unnamed: 0', 'Crédito', 'Cód.']
            COLUMNS_RENAME = {'Nro.Cpbte.':'Comprobante', 'Débito':'Importe'}
            df = pd.read_excel(path_extracto)
            df = self.format_credicoop(df)

        elif COMAFI in path_extracto:
            # Si se quiere acceder al extracto del COMAFI entra acá
            COLUMNS_DROP = ['Fecha de Carga', 'Descripcion Ampliada 2']
            COLUMNS_RENAME = {'Descripcion Ampliada 1':'Descripción Ampliada', "Descripción":"Concepto"}
            df = pd.read_csv(path_extracto, encoding = "ISO-8859-1", sep = ";")
            # df = self.format_comafi(df, COLUMNS_DROP, COLUMNS_RENAME) # No es necesaria funcion "format_comafi" porque solo necesita las modificaciones comunes a todos, no tiene particulares

        elif COMAFI_SEGURO in path_extracto:
            with warnings.catch_warnings(record=True):
                warnings.simplefilter("always")
                df = pd.read_excel(path_extracto, engine="openpyxl")

            df = self.format_comafi(df)
            COLUMNS_DROP = ['Fecha de Carga', 'Moneda', 'Descripción Ampliada 2']
            COLUMNS_RENAME = {'Descripción':'Concepto', "Descripción Ampliada 1":"Descripción Ampliada", "ID Operación":"Comprobante"}

        elif PROVINCIA in path_extracto:
            # Si se quiere acceder al extracto del COMAFI entra acá
            COLUMNS_DROP = ['Unnamed: 0']
            COLUMNS_RENAME = {'Descripción':'Concepto'}
            df = pd.read_excel(path_extracto, header = 4)
            df = self.format_provincia(df)

        df['Fecha'] = pd.to_datetime(df['Fecha'], format = DATE_FORMAT)
        df.rename(columns = COLUMNS_RENAME, inplace = True)
        df.drop(COLUMNS_DROP, axis = 1, inplace = True)
        df.insert(0, "Clasificación", "")

        return df

    def format_credicoop(self, df):
        df.dropna(how = 'all', inplace = True)
        df['Débito'] = df['Crédito'] - df['Débito']
        df.insert(3, column = 'Descripción Ampliada', value = '')
        df['Nro.Cpbte.'].fillna(value = 0, inplace = True)
        df['Nro.Cpbte.'] = df['Nro.Cpbte.'].astype(int)

        return df

    def format_comafi(self, df):

        i = list(df.columns)
        a, b = i.index("ID Operación"), i.index("Descripción Ampliada 2")
        i[b], i[a] = i[a], i[b]
        df = df[i]

        return df

    def format_provincia(self, df):
        df.drop(df.tail(2).index, inplace = True)
        df.insert(3, column = 'Descripción Ampliada', value = '')
        df.insert(4, column = 'Comprobante', value = '')
        return df