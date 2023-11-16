# Standard library imports

# Third party imports

# Proyect imports
from errors.dates.error import dateError
from datetime import date

def date_validation(mes, year):
    inputDate = date(int(year), int(mes[2]), 1)
    currentDate = date.today()
    try:
        if inputDate < currentDate:
            return True
        else:
            raise dateError()
    except dateError as error:
        print(error.message)
