def getHouseInfo(driver):
    driver.get('https://portal.dankook.ac.kr/web/portal/-13')
    driver.implicitly_wait(5)
    
    elements=driver.find_elements_by_xpath('//*[@id="p_p_id_Bbs_WAR_bbsportlet_"]/div/div/div/div/div[2]/ul/li')
    str=""
    for e in elements:
        m=e.find_element_by_xpath('.//div[2]/a/div[2]')
        str=str+m.text+"\n"
    print(str)

def getHouseInfoC(driver):
    driver.get('https://portal.dankook.ac.kr/web/portal/-20')
    driver.implicitly_wait(5)

    elements=driver.find_elements_by_xpath('//*[@id="p_p_id_Bbs_WAR_bbsportlet_"]/div/div/div/div/div[2]/ul/li')
    str=""
    for e in elements:
        m=e.find_element_by_xpath('.//div[2]/a/div[2]')
        str=str+m.text+"\n"
    print(str)
