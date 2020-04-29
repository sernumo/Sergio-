import scrapy
import csv
import time
import os
import glob
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class Selenium(scrapy.Spider):
    name = 'selenium_spider'
    start_urls = [
        'https://www.meteoblue.com/es/tiempo/archive/export/bimbaletes-aguascalientes-%28el-%c3%81lamo%29_m%c3%a9xico_4017108', 
        'https://www.meteoblue.com/es/tiempo/archive/export/nueva-baja-california_m%c3%a9xico_8675605', 
        'https://www.meteoblue.com/es/tiempo/archive/export/san-ignacio_m%c3%a9xico_3986837',
        'https://www.meteoblue.com/es/tiempo/archive/export/san-bartolo_m%c3%a9xico_3519657',
        'https://www.meteoblue.com/es/tiempo/archive/export/el-progreso-de-chiapas_m%c3%a9xico_3528380', 
        'https://www.meteoblue.com/es/tiempo/archive/export/sierra-tom%c3%b3chic_m%c3%a9xico_3981379',
        'https://www.meteoblue.com/es/tiempo/archive/export/corral-de-barrancas_m%c3%a9xico_4012821', 
        'https://www.meteoblue.com/es/tiempo/archive/export/los-alm%c3%a1rcigos_m%c3%a9xico_3998182',
        'https://www.meteoblue.com/es/tiempo/archive/export/santa-mar%c3%ada-del-oro_m%c3%a9xico_3984078',
        'https://www.meteoblue.com/es/tiempo/archive/export/abasolo_m%c3%a9xico_4019869', 
        'https://www.meteoblue.com/es/tiempo/archive/export/ayutla-de-los-libres_m%c3%a9xico_3532499', 
        'https://www.meteoblue.com/es/tiempo/archive/export/zotola_m%c3%a9xico_3813769', 
        'https://www.meteoblue.com/es/tiempo/archive/export/ojuelos-de-jalisco_m%c3%a9xico_3994216', 
        'https://www.meteoblue.com/es/tiempo/archive/export/las-ca%c3%b1adas_m%c3%a9xico_8858636', 
        'https://www.meteoblue.com/es/tiempo/archive/export/cuauchichinola_m%c3%a9xico_353000',
        'https://www.meteoblue.com/es/tiempo/archive/export/playa-novillero_m%c3%a9xico_4028455', 
        'https://www.meteoblue.com/es/tiempo/archive/export/presa-san-antonio_m%c3%a9xico_4022560', 
        'https://www.meteoblue.com/es/tiempo/archive/export/zapotitl%c3%a1n_m%c3%a9xico_3514065',
        'https://www.meteoblue.com/es/tiempo/archive/export/pe%c3%b1amiller_m%c3%a9xico_3521677', 
        'https://www.meteoblue.com/es/tiempo/archive/export/%c3%81lvaro-obreg%c3%b3n_m%c3%a9xico_3823190', 
        'https://www.meteoblue.com/es/tiempo/archive/export/armadillo-de-los-infante_m%c3%a9xico_4018237', 
        'https://www.meteoblue.com/es/tiempo/archive/export/el-espinal_m%c3%a9xico_4009878', 
        'https://www.meteoblue.com/es/tiempo/archive/export/amalia_m%c3%a9xico_4005588',
        'https://www.meteoblue.com/es/tiempo/archive/export/villa-tecolutilla_m%c3%a9xico_3516149', 
        'https://www.meteoblue.com/es/tiempo/archive/export/atlangatepec_m%c3%a9xico_3814972', 
        'https://www.meteoblue.com/es/tiempo/archive/export/cahuapan_m%c3%a9xico_3531856', 
        'https://www.meteoblue.com/es/tiempo/archive/export/samahil_m%c3%a9xico_3520011', 
        'https://www.meteoblue.com/es/tiempo/archive/export/el-nuevo-mercurio_m%c3%a9xico_4008972'
    ] 

    nombre = [
        "Bimbaletes__Aguascalientes",
        "Nueva_Baja_California__Baja_California",
        "San_Ignacio__Baja_California_Sur",
        "San_Bartolo__Campeche",
        "El_Progreso__Chiapas",
        "Sierra_Tomóchic_Chihuahua",
        "Corral_de_Barrancas__Coahuila",
        "Los_Almarcigos__Colima",
        "Santa_María_del_Oro__Durango",
        # Estado de México
        "Abasolo__Guanajuato",
        "Ayutla_de_los_Libres__Guerrero",
        "Zotola__Hidalgo",
        "Ojuelos__Jalisco",
        "Las_Cañadas__Michoacán",
        "Cuauchichinola__Morelos",
        "Playa_Novillero__Nayarit",
        "Presa_San_Antonio__Nuevo_León",
        # Oaxaca
        "Zapotitlán__Puebla",
        "PeNamiller__Queretaro",
        "Alvaro_ObregOn__Quintana_Roo",
        "Armadillo_de_los_Infante__San_Luis_Potosí",
        "El_Espinal__Sinaloa",
        "Amalia__Sonora",
        "Villa_Tecolutilla__Tabasco",
        # Tamaulipas
        "Atlangatepec__Tlaxcala",
        "Cahuapan__Veracruz",
        "Samahil_Yucatan",
        "El_Nuevo_Mercurio_Zacatecas"

        
    ] 

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {
            "download.default_directory": "C:\\Users\\USUARIO\\Documents\\Proyecto_Energia\\Meteo_Blue\\"
        }
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(chrome_options=chrome_options) # Driver de Selenium
        
    def parse(self, response):
        self.driver.get(response.url)
        time.sleep(5)
        # Buscar boton de aceptar y continuar
        try:
            boton = self.driver.find_element_by_css_selector('input[value="Aceptar y continuar"]')
        except NoSuchElementException:
            boton = None
        if boton:
            boton.click()
        time.sleep(5)
        # Buscar boton de temperatura a 2m para desactivar
        boton2 = self.driver.find_element_by_css_selector('input[value="temp2m"]')
        boton2.click()
        time.sleep(5)
        # Buscar boton de velocidad de viento a 10m para desactivar
        boton3 = self.driver.find_element_by_css_selector('input[value="wind+dir10m"]')
        boton3.click()
        time.sleep(5)
        # Buscar boton de velocidad de viento a 80m para activar
        boton4 = self.driver.find_element_by_css_selector('input[value="wind+dir80m"]')
        boton4.click()
        time.sleep(5)
        # Buscar boton de precipitacion para desactivar
        boton6 = self.driver.find_element_by_css_selector('input[value="precip"]')
        boton6.click()
        time.sleep(5)
        # Buscar boton de descarga
        boton5 = self.driver.find_element_by_css_selector("input[name=submit_csv]")
        boton5.click()
        time.sleep(5)
        # Cambiar nombre al archivo recien descargado
        lista_archivos = glob.glob(
            'C:\\Users\\USUARIO\\Documents\\Proyecto_Energia\\Meteo_Blue\\*')
        ultimo_archivo = max(lista_archivos, key=os.path.getctime)
        indice = self.start_urls.index(response.url)
        os.rename(ultimo_archivo, ultimo_archivo[:-4] + "_" + self.nombre[indice] + ".csv")
