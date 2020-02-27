from selenium.webdriver.common.by import By

"""以下为登录模块配置数据"""
# 关闭弹出
login_close_alert = (By.ID, "com.bjcsxq.chat.carfriend:id/bt_no")
# 我
login_me = (By.ID, "com.bjcsxq.chat.carfriend:id/mine_image")
# 登录/注册
login_login_reg = (By.ID, "com.bjcsxq.chat.carfriend:id/mine_username_tv")
# 手机号
login_phone = (By.ID, "com.bjcsxq.chat.carfriend:id/login_phone_et")
# 密码
login_pwd = (By.ID, "com.bjcsxq.chat.carfriend:id/login_pwd_et")
# 登录按钮
login_btn = (By.ID, "com.bjcsxq.chat.carfriend:id/login_btn")
