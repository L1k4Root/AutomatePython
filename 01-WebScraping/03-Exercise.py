
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def get_driver(url):
    # 1. Configura las opciones
    options = Options()
    # options.add_argument('--headless')  # Opcional: ejecuta sin abrir ventana
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('start-maximized')

    # 2. Usa la nueva función para descargar el driver automáticamente
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    # 3. Abre una web y haz scraping
    driver.get(url=url)
    return driver

def get_temperature(text):
    print(text)
    # Extrae el número de la cadena de texto
    temperature = text.split(":")[1].strip()  # Asumiendo que el formato es "XX °C"
    return int(temperature)  # Convierte a entero

def main():
    driver = get_driver("https://automated.pythonanywhere.com/")
    time.sleep(1)  # Espera a que la página cargue completamente
    driver.find_element(By.XPATH, value='/html/body/nav/div/div/div/a').click()
    time.sleep(1)  # Espera a que la página de login cargue
    driver.find_element(By.ID, value='id_username').send_keys('automated')
    driver.find_element(By.ID, value='id_password').send_keys('automatedautomated' + Keys.RETURN)
    time.sleep(1)  # Espera a que la página cargue después del login
    print("Login realizado con éxito")
    print(driver.current_url)  # Imprime la URL actual para verificar el login
    time.sleep(2)  # Espera un momento para ver el resultado
    Temperature = get_temperature(driver.find_element(By.XPATH, value='/html/body/div[1]/h1[2]').text)
    time.sleep(1)  # Espera a que la página de logout cargue
    print(driver.current_url)
    print(f"La temperatura actual es: {Temperature} °C")
    # 4. Cierra el navegador
    driver.quit()
    
if __name__ == "__main__":
    main()

