# Standard imports

# Third imports

# Proyect imports
from menu.menu import msg_invalid_month, msg_invalid_year

def switch_mes(numero):
    try:
        switch = {
            "1": ["Enero", "31", "01"],
            "2": ["Febrero", "28", "02"],
            "3": ["Marzo", "31", "03"],
            "4": ["Abril", "30", "04"],
            "5": ["Mayo", "31", "05"],
            "6": ["Junio", "30", "06"],
            "7": ["Julio", "31", "07"],
            "8": ["Agosto", "31", "08"],
            "9": ["Septiembre", "30", "09"],
            "10": ["Octubre", "31", "10"],
            "11": ["Noviembre", "30", "11"],
            "12": ["Diciembre", "31", "12"],
        }
        return switch[numero]
    except KeyError:
        msg_invalid_month()

def switch_year(numero):
    try:
        switch = {
            "1": "2022",
            "2": "2023",
        }
        return switch[numero]
    except KeyError:
        msg_invalid_year()
