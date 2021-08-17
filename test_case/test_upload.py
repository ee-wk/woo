import allure
import os
import pathlib
from common import driver
from page_obj.uploadPage import Upload
from page_obj.loginPage import Login
from time import sleep


@allure.feature('沃创云上传模块')
class TestLogin(object):
    """沃创云上传测试类"""
    def setup(self):
        self.driver = driver.browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        with allure.step('添加截图...'):
            allure.attach(self.driver.get_screenshot_as_png(), "截图", allure.attachment_type.PNG)
        self.driver.quit()

    # 进入首页
    def test_upload01(self):
        allure.dynamic.title('上传图片')
        allure.dynamic.description('上传图片成功')
        with allure.step('1.上传图片'):
            Login(self.driver).user_login()
            sleep(20)
            path = pathlib.Path(os.getcwd())
            Upload(self.driver).upload(str(path.parent)+"\data\photo.jpg")
