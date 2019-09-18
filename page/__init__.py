from selenium.webdriver.common.by import By

"""login模块配置参数"""
login_me = By.ID, 'com.yunmall.lc:id/tab_me'  # 我
login_username_link = By.ID, "com.yunmall.lc:id/textView1"  # 已有账户
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"  # 用户名
login_password = By.ID, "com.yunmall.lc:id/logon_password_textview"  # 密码
login_login_btn = By.ID, "com.yunmall.lc:id/logon_button"  # 登录按钮
login_nikename = By.ID, "com.yunmall.lc:id/tv_user_nikename"  # 昵称   cheng_heng_fei
login_setting = By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image'  # 设置
login_notification = By.ID, 'com.yunmall.lc:id/setting_notification'  # 消息推送
login_modify_pwd = By.ID, 'com.yunmall.lc:id/setting_modify_pwd'  # 修改密码
login_logout = By.ID, 'com.yunmall.lc:id/setting_logout'  # 退出
login_logout_ok = By.ID, 'com.yunmall.lc:id/ymdialog_right_button'  # 确认退出
login_popup = By.ID, 'com.yunmall.lc:id/img_close'  # 弹窗

"""地址管理模块的配置参数"""

address_manage = By.ID, 'com.yunmall.lc:id/setting_address_manage'  # 地址管理
address_add_new = By.ID, 'com.yunmall.lc:id/address_add_new_btn'  # 新增地址
address_receipt_name = By.ID, 'com.yunmall.lc:id/address_receipt_name'  # 输入 收件人
address_add_phone = By.ID, 'com.yunmall.lc:id/address_add_phone'  # 输入 手机号
address_province = By.ID, 'com.yunmall.lc:id/address_province'  # 点击所在地址
# 省 文本
# 市 大框  CLASS_NAME
address_city_kuang = By.CLASS_NAME, 'android.widget.RelativeLayout'
# 市 id
address_city_id = By.ID, 'com.yunmall.lc:id/area_title'
# 区 文本
address_detail_addr_info = By.ID, 'com.yunmall.lc:id/address_detail_addr_info'  # 输入详细地址
address_post_code = By.ID, 'com.yunmall.lc:id/address_post_code'  # 输入邮编
address_default = By.ID, 'com.yunmall.lc:id/address_default'  # 设为默认地址
address_save = By.ID, 'com.yunmall.lc:id/button_send'  # 点击保存
address_name_phone = By.ID, 'com.yunmall.lc:id/receipt_name'  # 收件人 电话
# 编辑
address_edit = By.ID, 'com.yunmall.lc:id/ymtitlebar_right_btn'
# 确认删除
address_delete_ok = By.ID, "com.yunmall.lc:id/ymdialog_left_button"
