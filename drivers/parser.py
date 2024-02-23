from drivers.driver import BaseDriver

from selenium.webdriver.common.by import By


class Parser:
    def __init__(self):
        self.browser_driver = BaseDriver()
        self.category: dict = {}
        self.base_url = 'https://aliexpress.ru/'

    def get_category(self):
        self.browser_driver.get(self.base_url)

        self.browser_driver.driver_sleep(100, 'RedHeaderNavigationItem_RedHeaderNavigationItem_'
                                              '_root__91jxr')
        self.browser_driver.find_element(By.CLASS_NAME, 'RedHeaderNavigationItem_RedHeaderNavigationItem_'
                                                        '_root__91jxr').click()

        category_list = self.browser_driver.find_element(By.CLASS_NAME,
                                                         'RedHeaderCatalogPopup_RedHeaderCatalogPopup_'
                                                         '_categories__484gh')
        for category in category_list.find_elements(By.TAG_NAME, 'a'):
            self.category[category.text] = category.get_attribute('href')

        return self.category

