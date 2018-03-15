from selenium import webdriver
import dankookFunction
import getpass
from myLibrary import convertDateStr

if __name__ == "__main__":
    id = input('ID : ')
    pw = getpass.getpass('PW : ')
    print('--before date--')
    month=int(input('month : '))
    day=int(input('day : '))

    driver=webdriver.Chrome('chromedriver.exe')
    driver.set_window_size(1200,500)
    pc=dankookFunction.portalChecker(driver,id,pw)

    pc.checkIsOrNot(convertDateStr(month,day))

    driver.quit()

