from openpyxl import Workbook
import openpyxl
import datetime
import numpy as np

class portalChecker:
    def __init__(self,driver):
        self.driver=driver

    def getHouseInfo(self):
        self.driver.get('https://portal.dankook.ac.kr/web/portal/-13')
        self.driver.implicitly_wait(5)
    
        elements=self.driver.find_elements_by_xpath('//*[@class="table_date"]')
        str=""
        for e in elements:
            str=str+e.text+"\n"
        print(str)

    def getHouseInfoC(self):
        self.driver.get('https://portal.dankook.ac.kr/web/portal/-20')
        self.driver.implicitly_wait(5)

        elements=self.driver.find_elements_by_xpath('//*[@id="p_p_id_Bbs_WAR_bbsportlet_"]/div/div/div/div/div[2]/ul/li')
        str=""
        for e in elements:
            m=e.find_element_by_xpath('.//div[2]/a/div[2]')
            str=str+m.text+"\n"
        print(str)

    def checkIsOrNot(self,beforeDate):
        excel_doc=openpyxl.load_workbook('portalCheck.xlsx')
        sheet=excel_doc.active

        check=False
        now=datetime.datetime.now()
        nowDate=now.strftime('%m.%d')

        self.driver.get('http://www.dankook.ac.kr/web/kor/-390')
        self.driver.implicitly_wait(5)

        elements=self.driver.find_elements_by_xpath('//*[@id="p_p_id_Bbs_WAR_bbsportlet_"]/div/div/div/div[2]/div[2]/ul/li')
        for e in elements:
            dateStr=e.find_element_by_class_name("table_date").text
            eDate=dateStr[5:]
            if(beforeDate<=eDate and eDate<=nowDate):
                check=True
        
        for i in np.arange(48):
            self.driver.get()
            elements=self.driver.find_elements_by_xpath('//*[@class="table_date"]')
            