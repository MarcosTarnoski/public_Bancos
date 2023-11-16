class dateError(Exception):
    def __init__(self):
        self.message = "\n-FECHA INVALIDA- Se debe seleccionar una fecha anterior a la actual.\n"

    def __str__(self):
        return(self.message)
