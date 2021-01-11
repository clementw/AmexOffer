import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

offers = ["932503ShopSmallTorontoJuly2019", "65397ShopSmallVancouverJuly2019", "68053ShopSmallCalgaryJuly2019",
          "66936ShopSmallMontrealJuly2019"]
rooturl = "https://offerenroll.americanexpress.com/enroll/EnrollmentSitePage?offer="

cards = [[],  # gold
         [],  # biz plat
         [],  # spg
         []  # spg biz
         [],  # scp
         []  # cobalt
         # [],
         # [],
         # []
         ]

first = ""
last = ""
email = ""


class Main:

    def __init__(self):
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': os.getcwd()}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_options=options)

    def login(self):
        offerNum = 0
        cardNum = 0

        while cardNum < len(cards):

            offerurl = "{0}{1}".format(rooturl, offers[offerNum])

            self.driver.get(offerurl)

            fill = self.driver.find_element_by_id(
                "apexPageId:headerid:HeaderFooterComponentId:form1:j_id268:j_id270:j_id271:j_id272:TextFirstName")
            fill.clear()
            fill.send_keys(first)

            fill = self.driver.find_element_by_id(
                "apexPageId:headerid:HeaderFooterComponentId:form1:j_id268:j_id270:j_id271:j_id272:TextLastName")
            fill.clear()
            fill.send_keys(last)

            fill = self.driver.find_element_by_id(
                "apexPageId:headerid:HeaderFooterComponentId:form1:j_id268:j_id270:j_id271:j_id272:TextCardNumber1")
            fill.clear()
            fill.send_keys(cards[cardNum][0].__str__())

            fill = self.driver.find_element_by_id(
                "apexPageId:headerid:HeaderFooterComponentId:form1:j_id268:j_id270:j_id271:j_id272:TextCardNumber2")
            fill.clear()
            fill.send_keys(cards[cardNum][1].__str__())

            fill = self.driver.find_element_by_id(
                "apexPageId:headerid:HeaderFooterComponentId:form1:j_id268:j_id270:j_id271:j_id272:TextCardNumber3")
            fill.clear()
            fill.send_keys(cards[cardNum][2].__str__())

            fill = self.driver.find_element_by_id(
                "apexPageId:headerid:HeaderFooterComponentId:form1:j_id268:j_id270:j_id271:j_id272:TextEmailAddress")
            fill.clear()
            fill.send_keys(email)

            fill = self.driver.find_element_by_id(
                "apexPageId:headerid:HeaderFooterComponentId:form1:j_id268:j_id270:j_id271:j_id272:TextConfirmEmailAddress")
            fill.clear()
            fill.send_keys(email)

            fill = self.driver.find_element_by_id(
                "apexPageId:headerid:HeaderFooterComponentId:form1:j_id268:j_id270:j_id271:j_id272:IAgreeRegister")
            fill.click()

            time.sleep(10)

            if offerNum < len(offers) - 1:
                offerNum += 1
            else:
                offerNum = 0
                cardNum += 1

    def full_run(self):
        self.login()


Main().full_run()
