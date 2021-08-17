from selenium.webdriver.common.by import By
from common.base import Page
from time import sleep
from common.driver import browser


class Login(Page):
    """
    用户登录页面
    """

    url = '/login'

    # Action
    password_login_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span[1]')
    login_username_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div[1]/input')
    login_password_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div[2]/input')
    login_button_loc = (By.XPATH, '//*[@id="login-button"]')
    remember_username_loc = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div[3]/label/span[2]')

    # 账密入口
    def woo_login(self):
        password_login_button = self.find_element(*self.password_login_loc)
        self.driver.execute_script("arguments[0].click();", password_login_button)

    # 输入用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 输入密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 点击登录按钮
    def login_button_click(self):
        login_button = self.find_element(*self.login_button_loc)
        self.driver.execute_script("arguments[0].click();", login_button)

    # 登录入口
    def user_login(self, username='14486595670', password='123456'):
        self.open()
        self.woo_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button_click()
        sleep(1)

    toast_msg_loc = (By.XPATH, '/html/body/div[2]/p')

    # toast提示
    def toast_msg(self):
        return self.find_element(*self.toast_msg_loc).text


if __name__ == "__main__":
    driver = browser()
    driver.implicitly_wait(10)
    driver.maximize_window()
    P = Login(driver)
    P.user_login()
    print(P.toast_msg())
