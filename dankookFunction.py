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

def checkIsOrNot(driver,beforeDate):
    import datetime

    check=False
    now=datetime.datetime.now()
    nowDate=now.strftime('%m.%d')

    driver.get('http://www.dankook.ac.kr/web/kor/-390')
    driver.implicitly_wait(5)

    elements=driver.find_elements_by_xpath('//*[@id="p_p_id_Bbs_WAR_bbsportlet_"]/div/div/div/div[2]/div[2]/ul/li')
    for e in elements:
        dateStr=e.find_element_by_class_name("table_date").text
        eDate=dateStr[5:]
        if(beforeDate<=eDate and eDate<=nowDate):
            check=True
    
    print(check)
