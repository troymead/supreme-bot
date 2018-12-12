from tkinter import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import sys, time

class QuickCop:
    def __init__(self, master):
        self.userInfo = {
                    "name": "",
                    "email": "",
                    "phone_number": 0,
                    "address": "",
                    "zip_code": 0,
                    "city": "",
                }

        self.itemInfo = {
            "category" : "",
            "size" : "",
            "color" : "",
            "keywords" : ""
        }

        self.ccInfo = {
            "number" : 0,
            "exp_month" : 0,
            "exp_year" : 0,
            "cvv" : 0
        }

        master.title('Quick Cop')

        topFrame = Frame(master)
        topFrame.pack(side=TOP)

        self.welcomeMessage = Text(master, fg="white", bg="red", font=("Courier", 18), width=44, height=1)
        self.welcomeMessage.insert(INSERT, "Quick Cop - A Bot for all your Supreme Needs")
        self.welcomeMessage.pack(side=TOP)

        leftFrame = Frame(master)
        leftFrame.pack(side=LEFT)

        rightFrame = Frame(master)
        rightFrame.pack(side=RIGHT)

        self.enterInfoMess = Label(leftFrame, text="Please enter your customer information below:")
        self.enterInfoMess.grid(sticky=W)

        Label(leftFrame, text="Full Name").grid(row=1)
        Label(leftFrame, text="Email").grid(row=2)
        Label(leftFrame, text="Phone Number").grid(row=3)
        Label(leftFrame, text="Address").grid(row=4)
        Label(leftFrame, text="Zip Code").grid(row=5)
        Label(leftFrame, text="City").grid(row=6)
        Label(leftFrame, text="Card Number").grid(row=7)
        Label(leftFrame, text="CVV").grid(row=8)
        Label(leftFrame, text="Expiration Date").grid(row=9)

        self.fnEntry = Entry(leftFrame)
        self.fnEntry.grid(row=1, column=1)
        self.emailEntry = Entry(leftFrame)
        self.emailEntry.grid(row=2, column=1)
        self.pNumberEntry = Entry(leftFrame)
        self.pNumberEntry.grid(row=3, column=1)
        self.addressEntry = Entry(leftFrame)
        self.addressEntry.grid(row=4, column=1)
        self.zipEntry = Entry(leftFrame)
        self.zipEntry.grid(row=5, column=1)
        self.cityEntry = Entry(leftFrame)
        self.cityEntry.grid(row=6, column=1)
        self.cardEntry = Entry(leftFrame)
        self.cardEntry.grid(row=7, column=1)
        self.cvvEntry = Entry(leftFrame)
        self.cvvEntry.grid(row=8, column=1)

        self.monthList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.monthVal = IntVar()
        self.monthVal.set("---")
        self.expMonthMenu = OptionMenu(leftFrame, self.monthVal, *self.monthList)
        self.expMonthMenu.grid(row=9, column=1)

        self.yearList = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028]
        self.yearVal = IntVar()
        self.yearVal.set("---")
        self.expYearMenu = OptionMenu(leftFrame, self.yearVal, *self.yearList)
        self.expYearMenu.grid(row=9, column=2)

        self.itemInfoMess = Label(rightFrame, text="Enter info about the item:")
        self.itemInfoMess.grid(sticky=W)

        Label(rightFrame, text="Category").grid(row=1)
        self.optionList = ["New", "Jackets", "Shirts", "Tops/Sweaters", "Sweatshirts", "Pants", "Hats", "Accessories",
                           "Shoes", "Skate"]
        self.dropVar = StringVar()
        self.dropVar.set("---")
        self.dropMenu = OptionMenu(rightFrame, self.dropVar, *self.optionList)
        self.dropMenu.grid(row=1, column=1)

        Label(rightFrame, text="Size").grid(row=2)
        self.sizeList = ["One Size", "Small", "Medium", "Large", "XLarge"]
        self.sizeDrop = StringVar()
        self.sizeDrop.set("---")
        self.sizeMenu = OptionMenu(rightFrame, self.sizeDrop, *self.sizeList)
        self.sizeMenu.grid(row=2, column=1)

        Label(rightFrame, text="Item Color").grid(row=3)
        self.itemColor = Entry(rightFrame)
        self.itemColor.grid(row=3, column=1)

        Label(rightFrame, text="Keywords (EXACT)").grid(row=4)
        self.itemName = Entry(rightFrame)
        self.itemName.grid(row=4, column=1)

        self.setButton = Button(leftFrame, text="Set Information", command=self.setButtonFunc)
        self.setButton.grid(row=10)

        self.orderButton = Button(rightFrame, text="Start Order", command=self.order)
        self.orderButton.grid(row=5)

    def getUserInfo(self):
        self.userInfo["name"] = self.fnEntry.get()
        self.userInfo["email"] = self.emailEntry.get()
        self.userInfo["phone_number"] = self.pNumberEntry.get()
        self.userInfo["address"] = self.addressEntry.get()
        self.userInfo["zip_code"] = self.zipEntry.get()
        self.userInfo["city"] = self.cityEntry.get()

    def getItemInfo(self):
        self.itemInfo["category"] = self.dropVar.get()
        self.itemInfo["size"] = self.sizeDrop.get()
        self.itemInfo["color"] = self.itemColor.get()
        self.itemInfo["keywords"] = self.itemName.get()

    def getCCInfo(self):
        self.ccInfo["number"] = self.cardEntry.get()
        self.ccInfo["cvv"] = self.cvvEntry.get()
        self.ccInfo["exp_month"] = self.monthVal.get()
        self.ccInfo["exp_year"] = self.yearVal.get()

    def setButtonFunc(self):
        self.getUserInfo()
        self.getItemInfo()
        self.getCCInfo()

    def getUrl(self):
        if self.itemInfo["category"] == "New":
            return "https://www.supremenewyork.com/shop/all/hats"
        elif self.itemInfo["category"] == "Jackets":
            return "https://www.supremenewyork.com/shop/all/jackets"
        elif self.itemInfo["category"] == "Shirts":
            return "https://www.supremenewyork.com/shop/all/shirts"
        elif self.itemInfo["category"] == "Tops/Sweaters":
            return "https://www.supremenewyork.com/shop/all/tops_sweaters"
        elif self.itemInfo["category"] == "Sweatshirts":
            return "https://www.supremenewyork.com/shop/all/sweatshirts"
        elif self.itemInfo["category"] == "Pants":
            return "https://www.supremenewyork.com/shop/all/pants"
        elif self.itemInfo["category"] == "Hats":
            return "https://www.supremenewyork.com/shop/all/hats"
        elif self.itemInfo["category"] == "Accessories":
            return "https://www.supremenewyork.com/shop/all/accessories"
        elif self.itemInfo["category"] == "Shoes":
            return "https://www.supremenewyork.com/shop/all/shoes"
        elif self.itemInfo["category"] == "Skate":
            return "https://www.supremenewyork.com/shop/all/skate"

    def getSize(self):
        if self.itemInfo["category"] == "Jackets" or self.itemInfo["category"] == "Shirts" or \
                self.itemInfo["category"] == "Tops/Sweaters" or self.itemInfo["category"] == "Sweatshirts":

            if self.itemInfo["size"] == "Small":
                return "Small"
            elif self.itemInfo["size"] == "Medium":
                return "Medium"
            elif self.itemInfo["size"] == "Large":
                return "Large"
            elif self.itemInfo["size"] == "XLarge":
                return "XLarge"

    def order(self):
        driver = webdriver.Chrome('./chromedriver')

        url = self.getUrl()
        driver.get(url)

        driver.find_element_by_link_text(self.itemInfo["keywords"] and self.itemInfo["color"]).click()

        # if self.itemInfo["category"] == "Jackets" or self.itemInfo["category"] == "Shirts" or \
        #         self.itemInfo["category"] == "Tops/Sweaters" or self.itemInfo["category"] == "Sweatshirts":
        #     size = self.getSize()
        #     select = Select(driver.find_element_by_id('s'))
        #     select.select_by_visible_text(size)
            #driver.find_element_by_xpath(size).click()

        time.sleep(1)
        
        driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()

        time.sleep(0.75)

        checkoutElement = driver.find_element_by_class_name('checkout')
        checkoutElement.click()

        driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(self.userInfo["name"])
        driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(self.userInfo["email"])

        pnumber = driver.find_element_by_xpath('//*[@id="order_tel"]')
        text1 = self.userInfo["phone_number"]
        for character in text1:
            pnumber.send_keys(character)
            time.sleep(0.0001)

        driver.find_element_by_xpath('//*[@id="bo"]').send_keys(self.userInfo["address"])

        zip = driver.find_element_by_xpath('//*[@id="order_billing_zip"]')
        text2 = self.userInfo["zip_code"]
        for character2 in text2:
            zip.send_keys(character2)
            time.sleep(0.0001)

        cc = driver.find_element_by_id('nnaerb')
        text3 = self.ccInfo["number"]
        for character3 in text3:
            cc.send_keys(character3)
            time.sleep(0.0001)

        driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(self.ccInfo["cvv"])
        driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(self.ccInfo["exp_month"])).click()
        driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(self.ccInfo["exp_year"]-2017)).click()

        driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()


root = Tk()
QC = QuickCop(root)
root.mainloop()
