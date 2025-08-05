
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

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

def main():
    driver = get_driver("https://titan22.com/")
    time.sleep(2)  # Espera a que la página cargue completamente
    driver.find_element(By.XPATH, value='/html/body/header/div[1]/div[1]/div/div[3]/a[2]').click()
    time.sleep(2)  # Espera a que la página de login cargue
    driver.find_element(By.ID, value='CustomerEmail').send_keys('a.perezaraya2@uandresbello.edu', )
    time.sleep(2)  # Espera a que la página de login cargue

    driver.find_element(By.ID, value='CustomerPassword').send_keys('Qwerty123' + Keys.RETURN)
    time.sleep(2)  # Espera a que la página cargue después del login
    print("Login realizado con éxito")
    print(driver.current_url)  # Imprime la URL actual para verificar el login
    time.sleep(2)  # Espera un momento para ver el resultado
    temperature = driver.find_element(By.XPATH, value='/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
    time.sleep(2)  # Espera a que la página de logout cargue
    print(driver.current_url)
    time.sleep(3)  # Espera un momento para ver el resultado
    # 4. Cierra el navegador
    driver.quit()
    
if __name__ == "__main__":
    main()

