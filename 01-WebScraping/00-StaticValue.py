from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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
    driver = get_driver("https://es.wikipedia.org/wiki/Bernardo_O%27Higgins")
    title = driver.find_element(By.XPATH, value='/html/body/div[2]/div/div[3]/main/header/h1/span').text
    print(title)

    # 4. Cierra el navegador
    driver.quit()
    
if __name__ == "__main__":
    main()
    