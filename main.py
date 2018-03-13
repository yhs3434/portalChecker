from selenium import webdriver
import dankookFunction

if __name__ == "__main__":
    id = input('ID : ')
    pw = input('PW : ')

    driver=webdriver.Chrome('chromedriver.exe')
    driver.set_window_size(1200,500)
    pc=dankookFunction.portalChecker(driver,id,pw)

    pc.checkIsOrNot('2018.03.12')

    driver.quit()

