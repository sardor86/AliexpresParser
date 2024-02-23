from drivers.driver import BaseDriver

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import requests
from bs4 import BeautifulSoup


class Parser(BaseDriver):
    def __init__(self):
        super().__init__()
        self.category: dict = {}
        self.base_url = 'https://aliexpress.ru/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/111.0.0.0 Safari/537.36'}

    def get_category(self):
        self.get(self.base_url)

        self.driver_sleep(100, 'RedHeaderNavigationItem_RedHeaderNavigationItem_'
                                              '_root__91jxr')
        self.find_element(By.CLASS_NAME, 'RedHeaderNavigationItem_RedHeaderNavigationItem_'
                                                        '_root__91jxr').click()

        category_list = self.find_element(By.CLASS_NAME,
                                                         'RedHeaderCatalogPopup_RedHeaderCatalogPopup_'
                                                         '_categories__484gh')
        for category in category_list.find_elements(By.TAG_NAME, 'a'):
            self.category[category.text] = category.get_attribute('href')

        return self.category

    def get_products_list(self, category: str) -> list:
        products_list = []
        self.get(self.category[category])

        try:
            self.driver_sleep(5, 'snow-ali-kit_Button-Secondary__button__4468ot')
            self.find_elements(By.CLASS_NAME, 'snow-ali-kit_Button-Secondary__button__4468ot')[-1].click()
        except NoSuchElementException:
            pass

        self.driver_sleep(5, 'product-snippet_ProductSnippet__container__1r2its')

        for product in self.find_elements(By.CLASS_NAME, 'product-snippet_ProductSnippet__container__1r2its'):
            product_description = product.find_element(By.CLASS_NAME, 'product-snippet_ProductSnippet_'
                                                                      '_description__1r2its')
            products_list.append({
                'link': product_description.find_element(By.TAG_NAME, 'a').get_attribute('href'),
                'name': product.find_element(By.CLASS_NAME, 'product-snippet_ProductSnippet__name__1r2its').text,
                'price': product.find_element(By.CLASS_NAME, 'snow-price_SnowPrice__blockMain__1cmks6').text
            })
        print(products_list)
        return products_list
