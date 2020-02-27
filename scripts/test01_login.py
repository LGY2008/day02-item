import pytest

from page.page_login import PageLogin
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()


class TestLogin:
    # 1. 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_driver()
        # 获取PageLogin对象
        self.login = PageLogin(driver)
        # 关闭更新窗口
        self.login.page_close_alert()
        # 点击我的
        self.login.page_click_me()
        # 点击登录注册
        self.login.page_login_reg_link()

    # 2. 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 3. 测试方法
    @pytest.mark.parametrize("phone,pwd,expect", read_yaml("login.yaml"))
    def test_login(self, phone, pwd, expect):
        # 1. 调用登录业务操作
        self.login.page_login(phone, pwd)
        # 2. 获取登录按钮是否可点
        result = self.login.page_get_attribute("clickable")
        print("按钮是否可点：", result)
        try:
            assert result == "false"
        except Exception as e:
            # 1. 日志
            log.error(e)
            # 2. 截图
            self.login.base_get_img()
            # 3. 抛异常
            raise