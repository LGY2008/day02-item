from base.base import Base
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageLogin(Base):
    # 1. 关闭更新弹窗
    def page_close_alert(self):
        self.base_click(page.login_close_alert)

    # 2. 点击我
    def page_click_me(self):
        self.base_click(page.login_me)

    # 3. 点击登录/注册
    def page_login_reg_link(self):
        self.base_click(page.login_login_reg)

    # 4. 输入 手机号
    def page_input_phone(self, phone):
        self.base_input(page.login_phone, phone)

    # 5. 输入 密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 6. 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取登录按钮属性
    def page_get_attribute(self, att):
        return self.base_get_att(page.login_btn, att)

    # 7. 登录组合业务方法
    def page_login(self, phone, pwd):
        log.info("正在调用登录业务方法，手机号：{} 密码：{}".format(phone, pwd))
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
