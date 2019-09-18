"""统一入口类  管理所有的页面和模块对象"""
from page.page_address import PageAddress
from page.page_login import PageLogin
from tool.driver_util import DriverUtil


class PageIn:

    def __init__(self):
        """初始化 driver"""
        self.driver = DriverUtil.get_driver()

    def get_pagelogin(self):
        """初始化 pagelogin对象"""
        return PageLogin(self.driver)

    def get_pageaddresss(self):
        """初始化地址管理对象"""
        return PageAddress(self.driver)
