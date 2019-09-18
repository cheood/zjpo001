from time import sleep

import page
from base.base import Base


class PageAddress(Base):
    """地址管理模块  page类"""

    def __init__(self, driver):
        """初始化 给base类传入driver"""
        super().__init__(driver)
        # 临时标记 用于判断直辖市和非直辖市
        self.temp = 0

    # 点击地址管理
    def page_click_manage(self):
        """点击地址管理"""
        self.base_click(page.address_manage)

    # 点击新增地址
    def page_add_address(self):
        """点击新增地址"""
        self.base_click(page.address_add_new)

    # 输入 收件人
    def page_input_receiver(self, name):
        """输入收件人"""
        self.base_input(page.address_receipt_name, name)

    # 输入 手机号
    def page_input_phone(self, phone):
        """输入手机号"""
        self.base_input(page.address_add_phone, phone)

    # 点击所在地址
    def page_click_area_direct(self, province, area):
        """点击所在地址  直辖市的方法"""
        # 点级所在地址
        self.base_click(page.address_province)

        # 选择 省/直辖区 直接用文本
        self.base_click_of_text(province)

        # 选择 市  框 （注：先点击市的父类 外边的大框）
        self.base_click(page.address_city_kuang)
        # 选择 市  id (点击市元素 根据id查找）
        self.base_click(page.address_city_id)

        # 选择 区 直接用文本
        self.base_click_of_text(area)

    def page_click_area(self, province, city, area):
        """点击所在地址  非直辖市的方法"""
        # 点级所在地址
        self.base_click(page.address_province)

        # 选择 省/直辖区 直接用文本
        self.base_click_of_text(province)

        # 选择 市  框 （注：先点击市的父类 外边的大框）
        # self.base_click(page.address_city_kuang)
        # # 选择 市  id (点击市元素 根据id查找）
        # self.base_click(page.address_city_id)
        self.base_click_of_text(city)
        # # 选择 区 直接用文本
        self.base_click_of_text(area)

    # 输入详细地址
    def page_input_detail_address(self, detail_address):
        """输入详细地址"""
        self.base_input(page.address_detail_addr_info, detail_address)

    # 输入邮编
    def page_input_postcode(self, code):
        """输入邮编"""
        self.base_input(page.address_post_code, code)

    # 设为默认地址
    def page_default_address(self):
        """设为默认地址"""
        self.base_click(page.address_default)

    # 点击保存
    def page_click_save(self):
        """点击保存"""
        self.base_click(page.address_save)

    # 点击编辑
    def page_click_edit(self):
        """点击编辑"""
        self.base_click(page.address_edit)

    # 获取新增地址后的文本列表
    def page_get_address_text_list(self):
        """获取新增地址后的文本列表 方法"""
        return self.base_get_text_list(page.address_name_phone)

    # 删除地址列表的方法
    def page_click_delete_address(self):
        pass

    # 点击确认删除
    def page_delete_ok(self):
        """点击确认的方法"""
        self.base_click(page.address_delete_ok)

    # 删除所有的地址列表后进行断言
    def page_delete_aseert(self):
        """删除全都的断言 方法"""
        try:
            self.base_get_text_list(page.address_name_phone)
            return False
        except:
            return True

    # 删除地址列表中的所有数据  循环单个删除一条
    def page_delete_address_all(self):
        """删除地址列表中的所有数据  循环单个删除某一条"""

        #  先得到地址列表
        els = self.base_get_text_list(page.address_name_phone)
        for i in range(len(els)):
            # 点击编辑
            self.base_click(page.address_edit)
            # 点击删除
            self.base_find_eles_by_text("删除")
            # 点击确认删除
            self.page_delete_ok()

    def page_add_address_fun(self, name, phone, detail_address, postcode, province, city, area):
        """page类 组合新增地址的方法"""

        self.page_add_address()
        self.page_input_receiver(name)
        self.page_input_phone(phone)
        # 需要判断是否是直辖市
        arrs = ["北京市", "上海市", "天津市", "重庆市"]

        for arr in arrs:
            if province in arr:
                """直辖市"""
                self.temp = 1
                break

        if self.temp == 1:
            """调用直辖市方法"""
            self.page_click_area_direct(province, area)  # 点击所在地址
        else:
            self.page_click_area(province, city, area)  # 点击所在地址

        # 重置标记
        self.temp = 0

        self.page_input_detail_address(detail_address)
        self.page_input_postcode(postcode)
        self.page_default_address()
        self.page_click_save()

    def page_update_address_fun(self, name, phone, province, city, area, detail_address, postcode):
        """page类 组合修改地址的方法"""

        sleep(2)
        self.page_click_edit()  # 点击编辑
        self.base_find_eles_by_text("修改")  # 点击修改（默认点击第一个修改）
        self.page_input_receiver(name)
        self.page_input_phone(phone)
        # 需要判断是否是直辖市
        arrs = ["北京市", "上海市", "天津市", "重庆市"]

        for arr in arrs:
            if province in arr:
                """直辖市"""
                self.temp = 1
                break

        if self.temp == 1:
            """调用直辖市方法"""
            self.page_click_area_direct(province, area)  # 点击所在地址
        else:

            self.page_click_area(province, city, area)  # 点击所在地址
            pass

        # 重置标记
        self.temp = 0

        self.page_input_detail_address(detail_address)
        self.page_input_postcode(postcode)
        self.page_click_save()
