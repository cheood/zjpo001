"""
driver 工具类
"""
from time import sleep

from appium import webdriver


class DriverUtil:
    _driver = None

    # 初始化 driver  获取driver
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            desired_caps = {}
            # 必填-且正确
            desired_caps['platformName'] = 'Android'
            # 必填-且正确
            desired_caps['platformVersion'] = '5.1'
            # 必填
            desired_caps['deviceName'] = '192.168.56.101:5555'

            # 指定使用automationName库名 获取tosat
            desired_caps['automationName'] = 'Uiautomator2'

            # 配置输入中文
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True

            """app信息"""
            # APP包名
            desired_caps['appPackage'] = 'com.yunmall.lc'
            # 启动名
            desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'

            cls._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return cls._driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None

