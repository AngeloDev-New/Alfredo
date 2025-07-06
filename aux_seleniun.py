from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
time_wait = 120
import os

class chrome_driver(webdriver.Chrome):
    def __init__(self, *args, **kwargs):
        chrome_options = Options()

        # Diretório de perfil persistente
        perfil_path = os.path.expanduser("~/chrome-whatsapp-profile")
        chrome_options.add_argument(f"--user-data-dir={perfil_path}")
        chrome_options.add_argument("--profile-directory=Default")  # Pode ser outro nome se quiser separar

        chrome_options.add_argument("--start-maximized")

        # Se quiser passar opções adicionais
        if "options" in kwargs:
            for arg in kwargs["options"].arguments:
                chrome_options.add_argument(arg)
            kwargs.pop("options")

        # Usa o options que configuramos
        super().__init__(options=chrome_options, *args, **kwargs)

    def CliqueAqui(self, PATH):
        wait = WebDriverWait(self, time_wait)
        if ">" in PATH:
            search_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, PATH)))
        else:
            search_button = wait.until(EC.presence_of_element_located((By.XPATH, PATH)))
        search_button.click()

    def EscrevaAqui(self, PATH, texto, enviar_enter=False):
        wait = WebDriverWait(self, time_wait)
        input_field = wait.until(EC.presence_of_element_located((By.XPATH, PATH)))
        input_field.send_keys(texto)
        if enviar_enter:
            input_field.send_keys(Keys.ENTER)

    def CapturaTexto(self, PATH):
        wait = WebDriverWait(self, time_wait)
        try:
            elemento = wait.until(EC.presence_of_element_located((By.XPATH, PATH)))
            return elemento.text
        except Exception as e:
            print(f"Erro ao capturar texto: {e}")
            return None

    def getJson(self, link):
        self.get(link)
        element = WebDriverWait(self, time_wait).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cm-content.cm-lineWrapping'))
        )
        return element.get_attribute('textContent')
