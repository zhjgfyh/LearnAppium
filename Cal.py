# urs/bin/python
# encoding:utf-8
import time
from appium import webdriver
import unittest


class MyTestCase(unittest.TestCase):
    # 脚本初始化，获取操作实例
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3'
        desired_caps['deviceName'] = '192.168.140.101:5555'
        desired_caps['appPackage'] = 'com.android.calculator2'
        desired_caps['appActivity'] = '.Calculator'
        desired_caps['unicodeKeyboard'] = "True"
        desired_caps['resetKeyboard'] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 释放实例，释放资源
    def tearDown(self):
        self.driver.quit()

    # 测试的脚本，LOVE原则
    def testAdd(self):
        # Locate定位数字8这个元素
        number8 = self.driver.find_element_by_id("digit8")
        # Operate操作数字8这个元素
        number8.click()
        # Locate定位加号这个元素
        addoperation = self.driver.find_element_by_id("plus")
        # Operate操作加号这个元素
        addoperation.click()
        # Locate定位数字5这个元素
        number5 = self.driver.find_element_by_id("digit5")
        # Operate操作数字5这个元素
        number5.click()
        # Locate定位等号这个元素
        equal = self.driver.find_element_by_id("equal")
        # Operate操作等号这个元素
        equal.click()
        # Verify验证操作的结果
        try:
            result = self.driver.find_element_by_class_name("android.widget.EditText")
            value = result.text
            self.assertEqual("13", value)
        # Exception出理异常的情况
        except Exception:
            print u"程序出现异常了"
            self.fail("程序出现异常了")

if __name__ == '__main__':
    unittest.main()