from dankookFunction import getHouseInfo

if __name__ == "__main__":
    from selenium import webdriver

    driver=webdriver.Chrome('./chromedriver.exe')
    driver.get('https://portal.dankook.ac.kr/web/portal/-13')

    driver.implicitly_wait(5)

    getHouseInfo(driver)
    
    driver.quit()

