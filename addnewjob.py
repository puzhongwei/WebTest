#coding=utf-8
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import  unittest
import  string
from selenium.webdriver.support.ui import Select


class logintest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox();
        browser = self.browser  # Get local session of firefox
        browser.get("https://hr.jianxun.io/")  # Load page
        print (browser.title)
        browser.find_element_by_class_name('login').click()
        time.sleep(3)
        browser.find_element_by_name("email").send_keys("jialezhang@huntcoder.com")  # Find the query box
        browser.find_element_by_name("password").send_keys("w123456")  # Find the query box
        time.sleep(10)  # Let the page load, will be added to the API
        browser.find_element_by_class_name('account-footer').click()
        #self.assertEqual('https://www.jianxun.io/account/login#b',browser.current_url)

    #返回随机字符
    def getRandom(self,a,b):
        x = random.randint(a, b)
        a = str(x)
        return a

    def test_addnewjob(self):
        time.sleep(3)
        driver=self.browser
        #driver=self.browser.get('https://hr.jianxun.io/talent/management/member/recommend')
        driver.find_element_by_link_text(u"职位管理").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"+ 添加新职位").click()
        time.sleep(3)
        # 职位分类
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div/a/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div/div/ul/li[{0}]'.format(self.getRandom(1,5))).click()


        #职位名称
        driver.find_element_by_css_selector("input.position-name.option-container").send_keys(u"test_初级")

        #月薪范围
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[5]/div[2]/div/div[1]/div/input').send_keys('3')
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[5]/div[2]/div/div[3]/div/input').send_keys('5')


        #工作地点
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[6]/div[2]/div/div/a/span').click()
        time.sleep(1)
        #
        lis = driver.find_elements_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[6]/div[2]/div/div/div/ul")
        print lis.__len__()
        for li in lis:
            print li.text
        #
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[6]/div[2]/div/div/div/ul/li[{0}]'.format(self.getRandom(1,10))).click()


        #工作经验
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[7]/div[2]/div/div/a/span').click();
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[7]/div[2]/div/div/div/ul/li[{0}]'.format(self.getRandom(1,7))).click()


        #最低学历
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[8]/div[2]/div/div/a/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[8]/div[2]/div/div/div/ul/li[{0}]'.format(self.getRandom(1,5))).click()

        #招聘人数
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[9]/div[2]/div/input').send_keys('3')


        #截至日期
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[10]/div[2]/div/div/a/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[10]/div[2]/div/div/div/ul/li[{0}]'.format(self.getRandom(1,4))).click()
        #岗位职责
        driver.find_element_by_name('position-duty').send_keys('this is a test')
        #岗位要求
        driver.find_element_by_name('position-requirement').send_keys('this si a test')
        #发布职位
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[4]/div[2]/input').click()

        time.sleep(3)
        self.assertEqual(driver.current_url,'https://hr.jianxun.io/position/management')

        driver.quit()

if __name__ == '__main__':
    unittest.main()