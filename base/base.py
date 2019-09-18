"""
基类  封装底层公共方法 13521514816 cheng_heng_fei  123456
"""
import os

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tool.get_log import GetLog

# 获取日志器
log = GetLog.get_log()


class Base:

    # 初始化driver
    def __init__(self, driver):
        """base类 初始化driver"""
        log.info("初始化的driver {}".format(driver))
        self.driver = driver

    # 查找元素
    @allure.step(title="查找元素")
    def base_find(self, loc, timeout=10, poll_frequency=0.5):
        """Base类 查找元素"""
        allure.attach("描述", f"查找元素{loc},传入的参数是：响应时间{timeout},请求的频率{poll_frequency}")
        log.info("查找的元素{} 等待时间{}查找频率{}".format(loc, timeout, poll_frequency))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_element(*loc))

        # 查找元素

    @allure.step(title="查找元素")
    def base_finds(self, loc, timeout=10, poll_frequency=0.5):
        """Base类 查找一组元素"""
        allure.attach("描述", f"查找元素{loc},传入的参数是：响应时间{timeout},请求的频率{poll_frequency}")
        log.info("查找的元素{} 等待时间{}查找频率{}".format(loc, timeout, poll_frequency))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
            lambda x: x.find_elements(*loc))

    # 点击元素
    def base_click(self, loc):
        """base类 点击元素"""
        el = self.base_find(loc)
        el.click()
        log.info("点击的元素{}", el)

    # 文本框输入文本
    def base_input(self, loc, value):
        """base类 给文本框输入文本内容"""
        log.info("正在输入信息的文本框{}，输入的信息{}".format(loc, value))
        el = self.base_find(loc)
        el.clear()
        el.send_keys(value)

    # 获取元素文本
    def base_get_el_text(self, loc):
        """base类 获取元素的文本内容"""
        log.info("获取文本的元素是{} 获取的文本内容是{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    # 获取toast
    def base_get_toast(self, msg):
        """base类  获取toast消息"""
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(msg)
        # 因为toast信息有时候获取不到 需要单独为它设置获取动作的间隔时间
        log.info("要定位toast的条件msg---{} 获取的toast的元素{}获取得到的toast是{}".format(msg, loc, self.base_find(loc, timeout=5,
                                                                                                  poll_frequency=0.2).text))
        return self.base_find(loc, timeout=5, poll_frequency=0.2).text

    # 页面滑动 消息推送----》修改密码
    def base_drag_and_drop(self, loc1, loc2):
        """base类 页面滑动  从消息推送---->修改密码"""
        self.driver.drag_and_drop(self.base_find(loc1), self.base_find(loc2))

    # 截图 当断言出现异常时 调用此方法v
    # 注  截图的路径用了./image  如果不用pytes命令（配置文件执行） 用../image

    def base_scrren(self):
        """base类的截图的方法"""
        # 截图 放到本地的image包中
        self.driver.get_screenshot_as_file("./image/err.png")

        # 截图之后立即调用 将截图写入报告的方法
        self.base_scrren_write_report()

    # 将截图写入报告
    # 注  截图的路径用了./image  如果不用pytes命令（配置文件执行） 用../image

    def base_scrren_write_report(self):
        """base类 将截图写入报告的方法"""
        # 读取本地的截图 写入报告
        path = os.path.abspath(os.path.dirname(__file__))
        with open(path+"./image/err.png", "rb") as f:
            # 写入报告
            allure.attach("失败原因", f.read(), allure.attach_type.PNG)

    # 根据文本查找元素并点击
    def base_click_of_text(self, text):
        """根据文本查找元素并点击 方法"""
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(text)
        self.base_click(loc)

    # 获取一组元素的text 并以list形式返回
    def base_get_text_list(self, loc):
        """获取一组元素的text 并以list形式返回 采用的是 行内遍历  本项目用在新增地址后的断言"""
        return [el.text for el in self.base_finds(loc, timeout=3)]

    # 根据文本查找一组元素 并且默认点击第一个元素
    def base_find_eles_by_text(self, text, num=0):
        """根据文本查找一组元素 并且默认点击第一个元素方法  用在修改地址的时候 从地址列表中选择第一个点击"""
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(text)
        # self.base_finds(loc)[num].click()
        els = self.base_finds(loc)
        if num > 0 and (num + 1) <= len(els):
            """如果下标大于0 判断元素列表下标是否不会越界  如果越界 默认返回第一个"""
            els[num].click()
        else:
            els[0].click()
