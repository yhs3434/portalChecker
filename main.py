from selenium import webdriver
import dankookFunction

if __name__ == "__main__":
    
    driver=webdriver.Chrome('chromedriver.exe')
    pc=dankookFunction.portalChecker(driver)
    pc.getHouseInfo()
    pc.getHouseInfoC()
    pc.checkIsOrNot('03.06')

    driver.quit()

