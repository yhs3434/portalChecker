def getHouseInfo(driver):
    elements=driver.find_elements_by_xpath('//*[@id="p_p_id_Bbs_WAR_bbsportlet_"]/div/div/div/div/div[2]/ul/li')

    count=0
    for e in elements:
        count+=1
        m=e.find_element_by_xpath('.//div[2]/a/div[2]')
        print(count,m.text)

