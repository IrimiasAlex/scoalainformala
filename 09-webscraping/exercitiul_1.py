# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import pandas as pd
#
# def browser_function():
#     driver_path = "path/to/chromedriver"
#     chr_options = Options()
#     chr_options.add_experimental_option("detach", True)
#     chr_driver = webdriver.Chrome(driver_path, options=chr_options)
#     chr_driver.get("https://target_website.com")
#
# browser = webdriver.Chrome(ChromeDriverManager().install())
# browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
# table = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]')
# table_text = table.text
# lista = table_text.split('\n')
#
#
# header_len = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]')
# header = header_len.text.split('\n')
# dictionar = {i: [] for i in header}
# for j in range(0, len(header)):
#     for i in range(len(header) + int(j), len(lista), len(header)):
#         dictionar[header[int(j)]].append(lista[i])
#
#
# df = pd.DataFrame(dictionar)
# df.to_csv("exercitiul_1excel.csv")
# print(df)
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())
for zi in range(20, 27, 1):
    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{zi}-ianuarie-ora-13-00/")
    tabel = browser.find_element(by=By.CSS_SELECTOR, value='table')
    lista = tabel.text.split(' ')
    judet = lista[18:146:4] + lista[147:186:4]
    cazuri = lista[20:143:4] + lista[145:184:4] + lista[186:187:1]
    dictionar = {'Județ': judet,  zi : cazuri}
    df = pd.DataFrame(Dictionar, columns=['Județ', zi])