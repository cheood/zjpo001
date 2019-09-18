"""地址管理 测试类"""
import sys
import os

sys.path.append(os.getcwd())

from tool.get_log import GetLog
import pytest
from tool.read_adress_data import read_address_data
from tool.driver_util import DriverUtil
from time import sleep
from page.page_in import PageIn


def load_address_data(key):
    res = read_address_data("address_data.yaml")
    arr = list()
    arr.append(tuple(res.get(key).values()))
    print(arr)
    return arr


# 日志器
log = GetLog.get_log()


class TestAddress:

    # 初始化方法
    def setup_class(self):
        """初始化pagein对象  调用登录成功的方法"""
        # 初始化page
        self.address = PageIn().get_pageaddresss()
        # 登录成功方法
        PageIn().get_pagelogin().page_login_success()
        # 点击地址管理
        self.address.page_click_manage()

    # 关闭方法
    def teardown_class(self):
        """关闭driver"""
        sleep(2)
        DriverUtil.quit_driver()

    # 测试增加方法
    @pytest.mark.parametrize("name, phone, province, city, area, detail_address, postcode",
                             load_address_data("add_address"))
    def test01_add_address(self, name, phone, province, city, area, detail_address, postcode):
        """测试地址管理 新增方法"""
        self.address.page_add_address_fun(name, phone, detail_address, postcode, province, city, area)

        try:

            # 断言
            expect = name + " " + phone
            arr = self.address.page_get_address_text_list()
            print("断言--->expect:{}是否包含于arr{}".format(expect, arr))
            assert expect in arr
        except AssertionError as a:
            # 截图
            self.address.base_scrren()
            # 日志
            log.error(a)
            # 抛出异常
            raise

    # 测试修改方法
    @pytest.mark.parametrize("name, phone, province, city, area, detail_address, postcode",
                             load_address_data("update_address"))
    # def test02_update_address(self, name="李四", phone="13811119999", province="广东省", city="广州市", area="白云区",
    #                           detail_address="白马寺回龙观", postcode="100010"):
    def test02_update_address(self, name, phone, province, city, area, detail_address, postcode):
        """测试地址管理 修改方法"""
        self.address.page_update_address_fun(name, phone, province, city, area, detail_address, postcode)
        try:
            # 断言
            expect = name + "  " + phone
            arr = self.address.page_get_address_text_list()
            print("断言--->expect:{}是否包含于arr{}".format(expect, arr))
            assert expect in arr
        except AssertionError as a:
            # 截图
            self.address.base_scrren()
            # 日志
            log.error(a)
            # 抛出异常
            raise

    #
    # # 测试删除方法
    def test03_delete_address(self):
        self.address.page_delete_address_all()
        try:
            # 断言
            assert self.address.page_delete_aseert()
        except AssertionError as a:
            # 异常 截图
            self.address.base_scrren()
            # 日志
            log.error(a)
            # 抛出
            raise
