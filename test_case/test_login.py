import allure
import pytest
from common import driver
from page.loginPage import Login
import os
from common.readexcel import get_yaml_data


current_path = os.path.abspath(".")
yaml_path = os.path.join(current_path, "data\\login.yml")
data = get_yaml_data(yaml_path)
print(data)


@allure.feature('沃创云登录模块')
class TestLogin(object):
    """沃创云登录测试类"""
    def setup(self):
        self.driver = driver.browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        with allure.step('添加截图...'):
            allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        self.driver.quit()

    # 测试用户登录
    def user_login_verify(self, username='', password=''):
        Login(self.driver).user_login(username, password)

    @pytest.mark.parametrize("userinfo", data)
    def test_login1(self, userinfo):
        allure.dynamic.title(userinfo['title'])
        allure.dynamic.description(userinfo['description'])
        with allure.step(userinfo['step']['step1']):
            self.user_login_verify(username=userinfo['username'], password=userinfo['password'])
        with allure.step(userinfo['step']['step2']):
            po = Login(self.driver)
            assert po.toast_msg() == userinfo['eq'], '错误'

    # def test_login2(self):
    #     allure.dynamic.title('密码为空')
    #     allure.dynamic.description('密码为空，提示：请输入密码')
    #     with allure.step('1.切换至账密登录，只输入账号'):
    #         self.user_login_verify(username='14486595670')
    #     with allure.step('2.断言提示信息'):
    #         po = Login(self.driver)
    #         assert po.toast_msg() == '请输入密码!', '错误'
    #
    # def test_login3(self):
    #     allure.dynamic.title('账号为空')
    #     allure.dynamic.description('账号为空，提示：请输入用户名')
    #     with allure.step('1.切换至账密登录，只输入密码'):
    #         self.user_login_verify(password='123456')
    #     with allure.step('2.断言提示信息'):
    #         po = Login(self.driver)
    #         assert po.toast_msg() == '请输入用户名!', '错误'
    #
    # def test_login4(self):
    #     allure.dynamic.title('账号密码都为空')
    #     allure.dynamic.description('账号密码都为空，提示：请输入用户名')
    #     with allure.step('1.切换至账密登录，账号密码都为空'):
    #         self.user_login_verify(username='', password='')
    #     with allure.step('2.断言错误信息'):
    #         po = Login(self.driver)
    #         assert po.toast_msg() == '请输入用户名!', '提示信息错误'
    #
    # def test_login5(self):
    #     allure.dynamic.title('账号密码正确')
    #     allure.dynamic.description('账号密码正确，登录成功')
    #     with allure.step('1.切换至账密登录，输入正确账号密码'):
    #         self.user_login_verify(username='14486595670', password='123456')
    #     with allure.step('2.断言用户信息'):
    #         po = Login(self.driver)
    #         assert po.toast_msg() == '登录成功，正在跳转……!', '登录失败'
    #
    # def test_login6(self):
    #     allure.dynamic.title('输入不存在的用户')
    #     allure.dynamic.description('输入不存在的用户，提示：用户名不存在!')
    #     with allure.step('1.切换至账密登录，账号输入不存在的用户'):
    #         self.user_login_verify(username='bug', password='123456wk')
    #     with allure.step('2.断言错误信息'):
    #         po = Login(self.driver)
    #         assert po.toast_msg() == '用户名不存在！', '提示信息错误'
