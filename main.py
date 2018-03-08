import dankookFunction as df

if __name__ == "__main__":
    from selenium import webdriver

    driver=webdriver.Chrome('C:/Users/root/Documents/hansol/workspace/portalChecker/chromedriver.exe')
    df.getHouseInfo(driver)
    df.getHouseInfoC(driver)
    df.checkIsOrNot(driver,'03.06')

    driver.quit()

