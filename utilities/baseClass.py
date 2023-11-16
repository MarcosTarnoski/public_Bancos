#Standard library imports
import random
import time

#Third party imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Proyect imports
from tests import conftest


class baseClass:

    def creacion_driver(self):
    # Podríamos crear esta funcion directamente en el modulo de TESTS llamando al modulo CONFTESTS pero lo hacemos aca para mantener el estandar de definir el driver en la baseClass
        self.driver = conftest.setup()

    def rsleep1(self):
        time.sleep(random.uniform(1.10, 1.65))  # Delay random entre valores dados

    def rsleep2(self):
        time.sleep(random.uniform(0.55, 1.10))  # Delay random entre valores dados

    def wait_to_click(self, locator, time):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator)).click()

    def wait_element_presence(self, locator, time):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def wait_elements_presence(self, locator, time):
        WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def wait_frame_presence(self, locator, time):
        WebDriverWait(self.driver, time).until(EC.frame_to_be_available_and_switch_to_it(locator))
