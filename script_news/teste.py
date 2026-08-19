from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()

# Firefox instalado manualmente
options.binary_location = "/opt/firefox/firefox"

# VM sem interface gráfica
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)

driver.get("https://www.google.com")

print("Título:", driver.title)

driver.quit()