import dankookFunction
from openpyxl import Workbook
from selenium import webdriver

if __name__ == "__main__":
    
    driver=webdriver.Chrome('C:/Users/root/Documents/hansol/workspace/portalChecker/chromedriver.exe')
    pc=dankookFunction.portalChecker(driver)
    pc.getHouseInfo()
    pc.getHouseInfoC()
    pc.checkIsOrNot('03.06')

    driver.quit()

