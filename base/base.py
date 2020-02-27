import allure
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog
# 获取日志器
log = GetLog.get_logger()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info("正在初始化driver对象, driver: {}".format(driver))
        self.driver = driver

    # 查找 元素
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 为元组或列表
        :param timeout: 超时时间
        :param poll: 访问频率
        :return: 元素
        """
        log.info("正在查找：{} 元素，等待时间：{} 访问频率:{}".format(log, timeout, poll))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击 方法
    def base_click(self, loc):
        log.info("正在准备点击：{} 元素".format(loc))
        self.base_find(loc).click()
        log.info("{}:元素点击完成".format(loc))

    # 输入 方法
    def base_input(self, loc, value):
        # 1. 获取元素
        el = self.base_find(loc)
        # 2. 清空操作
        log.info("正在对：{}元素执行清空操作".format(loc))
        el.clear()
        log.info("{}元素执行清空操作完成".format(loc))
        # 3. 输入操作
        log.info("正对：{}元素输入:{}操作！".format(loc, value))
        el.send_keys(value)
        log.info("{}元素输入:{}操作完成！".format(loc, value))

    # 获取属性值
    def base_get_att(self, loc, value):
        # 1. 获取元素
        el = self.base_find(loc)
        log.info("正在获取{}元素的:{}属性值，获取的结果为：{}".format(loc, value, el.get_attribute(value)))
        # 2. 调用获取属性方法
        return el.get_attribute(value)

    # 截图方法
    def base_get_img(self):
        log.error("正在调用截图方法")
        # 1. 截图
        self.driver.get_screenshot_as_file("./image/err.png")
        # 2. 调用图片写入报告方法
        self.__base_write_img()

    # 将图片写入allure报告
    def __base_write_img(self):
        log.error("正在将图片写入allure报告")
        # 获取图片存储文件流
        with open("./image/err.png", "rb") as f:
            # 调用attach方法
            allure.attach("失败原因：", f.read(), allure.attach_type.PNG)
