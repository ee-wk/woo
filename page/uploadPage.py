from selenium.webdriver.common.by import By
from common.base import Page


class Upload(Page):
    """
    上传
    """

    url = '/'

    # Action
    upload_loc = (By.XPATH, '//*[@id="UploadFileBtn"]')

    # 进入主页
    def main_page(self):
        self.open()

    # 上传
    def upload(self, path):
        self.find_element(*self.upload_loc).send_keys(path)
