'''
HTML Basics - Tags and Elements: https://subslikescript.com/movie/The_Luck_of_the_Irish-274636
HTML Basics - Tree Structure: https://subslikescript.com/movie/Titanic-120338
XPath - Test Your XPath: https://scrapinghub.github.io/xpath-playground/
Installing Selenium and ChromeDriver: https://chromedriver.chromium.org/downloads
Strftime: https://strftime.org/
Crontab Guru: https://crontab.guru/
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'
path = '"C:\\Users\\ymorii\\Downloads\\chromedriver_win32\\chromedriver.exe"'  # introduce path here

# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)

# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv')

driver.quit()