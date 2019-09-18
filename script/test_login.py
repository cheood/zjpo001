import sys
import os

sys.path.append(os.getcwd())

from tool.get_log import GetLog
from tool.read_login_data import read_login_data
from page.page_in import PageIn
from tool.driver_util import DriverUtil
import pytest

# 日志器
log = GetLog.get_log()

"""测试登陆"""


def read_login_data_fun():
    res = read_login_data("login_data.yaml")
    arr = list()
    for item in res.values():
        arr.append(tuple(item.values()))
    print("arr----->", arr)
    return arr


class TestLogin:

    def setup_class(self):
        """初始化 pagein对象 pagelogin对象"""
        self.page_login = PageIn().get_pagelogin()
        # 去除弹窗
        self.page_login.paga_click_popup()
        # 点击我
        self.page_login.paga_click_me()
        # 点击 已有账户链接
        self.page_login.page_click_username_link()

    def teardown_class(self):
        """关闭driver"""
        DriverUtil.quit_driver()

    # def test_login(self, username="13521514816", password="123456", expect="cheng_heng_fei", success=True):
    # def test_login(self, username="13521514833", password="123456", expect="此用户不存在", success=False):

    @pytest.mark.parametrize("username, password, expect, success", read_login_data_fun())
    def test_login(self, username, password, expect, success):
        """测试login方法"""
        self.page_login.page_login_fun(username, password)  # 登陆方法

        # 判断测试用例的 正向和逆向
        if success:
            try:
                # 正向获取昵称
                res = self.page_login.page_get_nickname()
                assert res == expect
                print("获取的昵称----->", res)
                log.info("获取的昵称----->{}".format(res))
            except Exception as e:
                # 截图
                self.page_login.base_scrren()
                # 抛出异常
                log.error("正向异常{}".format(e))
                raise e
            finally:
                # 无论成功与否 退回登录页

                # 登录成功 从主页退回到登录页
                self.page_login.page_index_to_login_page()
                # 点击 我
                self.page_login.paga_click_me()
                # 点击 已有账户链接
                self.page_login.page_click_username_link()
        else:
            try:
                # 逆向获取toast
                result = self.page_login.page_get_toast(expect)
                print("获取的toast----->", result)
                log.info("获取的toast----->{}".format(result))
                assert result == expect + "err"
            except Exception as e:
                # 截图
                self.page_login.base_scrren()
                # 抛出异常
                log.error("逆向异常{}".format(e))
                raise e
                # 逆向的方法 一直在登录页操作
