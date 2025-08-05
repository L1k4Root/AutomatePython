
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


def main():
    driver = get_driver("https://quotes.toscrape.com/login")
    time.sleep(1)  # Espera a que la página cargue completamente
    driver.find_element(By.ID, value='username').send_keys('admin')
    driver.find_element(By.ID, value='password').send_keys('password' + Keys.RETURN)
    print("Login realizado con éxito")
    time.sleep(1)  # Espera a que la página cargue después del login
    print(driver.current_url)  # Imprime la URL actual para verificar el login
    time.sleep(1)  # Espera un momento para ver el resultado
    driver.find_element(By.XPATH, value='/html/body/div/div[2]/div[1]/div[1]/div/a[1]').click()
    time.sleep(1)  # Espera a que la página de logout cargue
    print(driver.current_url)
    # 4. Cierra el navegador
    driver.quit()
    
if __name__ == "__main__":
    main()
    