"""
login模块 page类
"""
from time import sleep

import page
from base.base import Base

from tool.get_log import GetLog

# 日志器
log = GetLog.get_log()


class PageLogin(Base):

    def __init__(self, driver):
        """login模块 page类 初始化方法 给base类传参 driver"""
        super().__init__(driver)

    def paga_click_popup(self):
        """login模块 page类 去除弹窗方法"""
        self.base_click(page.login_popup)

    def paga_click_me(self):
        """login模块 page类 点击我方法"""
        self.base_click(page.login_me)

    def page_click_username_link(self):
        """点击已有账户链接"""
        self.base_click(page.login_username_link)

    def page_input_username(self, value):
        """输入用户名"""
        self.base_input(page.login_username, value)

    def page_input_password(self, value):
        """输入密码"""
        self.base_input(page.login_password, value)

    def page_click_login_btn(self):
        """点击登录按钮"""
        self.base_click(page.login_login_btn)

    def page_get_nickname(self):
        """获取昵称"""
        return self.base_get_el_text(page.login_nikename)

    def page_get_toast(self, msg):
        """获取toast"""
        return self.base_get_toast(msg)

    def page_click_setting(self):
        """login模块 page类 点击设置方法"""
        self.base_click(page.login_setting)

    def page_drag_and_drop(self):
        """设置页面的滑动 消息推送---->密码修改"""
        self.base_drag_and_drop(page.login_notification, page.login_modify_pwd)

    def page_click_logout(self):
        """page类的 点击退出的方法"""
        self.base_click(page.login_logout)

    def page_click_logout_ok(self):
        """page类的 点击确认退出的方法"""
        self.base_click(page.login_logout_ok)

    def page_login_fun(self, username, password):
        """组合登录三步骤 当不知道业务的时候 只组合公用的方法  一个页面的方法"""
        log.info("调用组合业务方法 登录 输入的用户名{}输入的密码{}".format(username, password))
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

    def page_index_to_login_page(self):
        """登录成功后 从主页退出登录状态  回到登录页面"""
        log.info("掉用组合业务方法 退出方法")
        self.page_click_setting()  # 点击设置
        self.page_drag_and_drop()  # 滑动  消息推送----》修改密码
        self.page_click_logout()  # 退出
        self.page_click_logout_ok()  # 确认退出

    def page_login_success(self, name="cheng_heng_fei", pwd="123456"):
        """登录成功方法  地址管理模块调用它"""
        self.paga_click_popup()  # 弹窗
        self.paga_click_me()  # 点击我
        self.page_click_username_link()  # 点击已有账户
        self.page_input_username(name)  # 输入用户名
        self.page_input_password(pwd)  # 输入密码
        self.page_click_login_btn()  # 点击登录按钮
        sleep(2)
        self.page_click_setting()  # 点击设置
