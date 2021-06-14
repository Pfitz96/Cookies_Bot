from selenium import webdriver


URL = "https://orteil.dashnet.org/cookieclicker/"
PATH = "C:\Program Files (x86)\chromedriver.exe"

def get_chrome_web_driver(options):
    return webdriver.Chrome(PATH, chrome_options=options)

def get_chrome_options():
    return webdriver.ChromeOptions()

def set_chrome_incognito(options):
    options.add_argument('--incognito')

